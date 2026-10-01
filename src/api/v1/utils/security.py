"""
Utilidades para manejo de tokens JWT.
"""
from datetime import datetime, timedelta
from typing import Optional


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Genera un token JWT con los datos proporcionados.
    """
    raise NotImplementedError("Implementar generación de token JWT")


def verify_token(token: str) -> dict:
    """
    Valida un token JWT y retorna los datos decodificados.
    """
    raise NotImplementedError("Implementar validación de token JWT")


def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.
    """
    raise NotImplementedError("Implementar hasheo de contraseña")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica una contraseña contra su hash.
    """
    raise NotImplementedError("Implementar verificación de contraseña")