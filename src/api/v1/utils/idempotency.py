"""
Mecanismo para garantizar idempotencia en las solicitudes de creación de transacciones.
"""
from sqlalchemy import String, DateTime, Text, Index
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Optional
import hashlib
import json
import logging

from src.api.v1.config.database import Base

logger = logging.getLogger(__name__)


class IdempotencyKey(Base):
    """
    Modelo para almacenar claves de idempotencia.
    Garantiza que una solicitud pueda procesarse una sola vez.
    """
    __tablename__ = "idempotency_keys"

    key: Mapped[str] = mapped_column(String(255), primary_key=True)
    request_method: Mapped[str] = mapped_column(String(10), nullable=False)
    request_path: Mapped[str] = mapped_column(String(500), nullable=False)
    request_body_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    response_status: Mapped[Optional[int]] = mapped_column(nullable=True)
    response_body: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    processed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    __table_args__ = (
        Index("ix_idempotency_created_at", "created_at"),
        Index("ix_idempotency_request_path", "request_path"),
    )

    def __repr__(self):
        return f"<IdempotencyKey(key='{self.key}', method='{self.request_method}', path='{self.request_path}')>"


def generate_idempotency_key(
    method: str,
    path: str,
    body: Optional[dict] = None,
    client_id: Optional[str] = None
) -> str:
    """
    Genera una clave de idempotencia basada en el método, ruta, cuerpo y cliente.
    
    Args:
        method: Método HTTP de la solicitud
        path: Ruta de la solicitud
        body: Cuerpo de la solicitud (se hashea)
        client_id: Identificador del cliente para aislamiento
    
    Returns:
        Clave de idempotencia generada
    """
    components = [method.upper(), path]
    
    if client_id:
        components.append(client_id)
    
    if body:
        body_str = json.dumps(body, sort_keys=True, default=str)
        body_hash = hashlib.sha256(body_str.encode()).hexdigest()
        components.append(body_hash)
    
    key_input = "|".join(components)
    key_hash = hashlib.sha256(key_input.encode()).hexdigest()[:32]
    
    logger.debug(f"Clave de idempotencia generada: {key_hash}")
    return key_hash


def compute_body_hash(body: Optional[dict]) -> str:
    """
    Computa el hash del cuerpo de la solicitud.
    
    Args:
        body: Cuerpo de la solicitud
    
    Returns:
        Hash SHA-256 del cuerpo
    """
    if body is None:
        return ""
    
    body_str = json.dumps(body, sort_keys=True, default=str)
    return hashlib.sha256(body_str.encode()).hexdigest()


async def check_idempotency_key(session, key: str) -> Optional[IdempotencyKey]:
    """
    Verifica si una clave de idempotencia ya existe y fue procesada.
    
    Args:
        session: Sesión de base de datos
        key: Clave de idempotencia a verificar
    
    Returns:
        El registro de idempotencia si existe, None otherwise
    """
    from sqlalchemy import select
    
    result = await session.execute(
        select(IdempotencyKey).where(IdempotencyKey.key == key)
    )
    existing = result.scalar_one_or_none()
    
    if existing:
        logger.info(f"Clave de idempotencia encontrada: {key}")
    else:
        logger.debug(f"Nueva clave de idempotencia: {key}")
    
    return existing


async def store_idempotency_key(
    session,
    key: str,
    method: str,
    path: str,
    body: Optional[dict] = None,
    response_status: Optional[int] = None,
    response_body: Optional[str] = None
) -> IdempotencyKey:
    """
    Almacena una clave de idempotencia con su resultado.
    
    Args:
        session: Sesión de base de datos
        key: Clave de idempotencia
        method: Método HTTP
        path: Ruta de la solicitud
        body: Cuerpo de la solicitud
        response_status: Código de estado de la respuesta
        response_body: Cuerpo de la respuesta
    
    Returns:
        El registro de idempotencia creado
    """
    body_hash = compute_body_hash(body)
    
    idempotency_record = IdempotencyKey(
        key=key,
        request_method=method.upper(),
        request_path=path,
        request_body_hash=body_hash,
        response_status=response_status,
        response_body=response_body,
        processed_at=datetime.utcnow() if response_status else None
    )
    
    session.add(idempotency_record)
    await session.flush()
    
    logger.info(f"Clave de idempotencia almacenada: {key}")
    return idempotency_record


async def update_idempotency_response(
    session,
    key: str,
    response_status: int,
    response_body: str
):
    """
    Actualiza el registro de idempotencia con la respuesta procesada.
    
    Args:
        session: Sesión de base de datos
        key: Clave de idempotencia
        response_status: Código de estado de la respuesta
        response_body: Cuerpo de la respuesta
    """
    from sqlalchemy import select
    
    result = await session.execute(
        select(IdempotencyKey).where(IdempotencyKey.key == key)
    )
    record = result.scalar_one_or_none()
    
    if record:
        record.response_status = response_status
        record.response_body = response_body
        record.processed_at = datetime.utcnow()
        await session.flush()
        logger.info(f"Respuesta actualizada para clave de idempotencia: {key}")