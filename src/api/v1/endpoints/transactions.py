from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from datetime import datetime

from src.api.v1.config.database import get_db
from src.api.v1.config.settings import Settings
from src.api.v1.models.transaction import Transaction, TransactionStatus, User
from src.api.v1.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
    TransactionListResponse
)
from src.api.v1.utils.security import get_current_user
from src.api.v1.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/", response_model=TransactionListResponse)
async def list_transactions(
    skip: int = Query(0, ge=0, description="Número de registros a omitir"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros a retornar"),
    status_filter: Optional[TransactionStatus] = Query(None, description="Filtrar por estado de transacción"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Lista transacciones del usuario autenticado con paginación y filtros opcionales.
    """
    service = TransactionService(db)
    transactions = await service.get_transactions(
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        status=status_filter
    )
    return TransactionListResponse(
        transactions=[TransactionResponse.model_validate(t) for t in transactions],
        total=len(transactions),
        skip=skip,
        limit=limit
    )


@router.get("/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Obtiene una transacción específica por su ID.
    """
    service = TransactionService(db)
    transaction = await service.get_transaction_by_id(
        transaction_id=transaction_id,
        user_id=current_user.id
    )
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )
    return TransactionResponse.model_validate(transaction)


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_transaction(
    transaction_data: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Crea una nueva transacción con soporte para idempotencia.
    """
    service = TransactionService(db)
    
    try:
        transaction = await service.create_transaction(
            user_id=current_user.id,
            transaction_data=transaction_data
        )
        return TransactionResponse.model_validate(transaction)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )


@router.put("/{transaction_id}", response_model=TransactionResponse)
async def update_transaction(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Actualiza una transacción existente.
    """
    service = TransactionService(db)
    
    existing = await service.get_transaction_by_id(
        transaction_id=transaction_id,
        user_id=current_user.id
    )
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )
    
    if existing.status == TransactionStatus.COMPLETED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede modificar una transacción completada"
        )
    
    updated = await service.update_transaction(
        transaction_id=transaction_id,
        transaction_data=transaction_data
    )
    return TransactionResponse.model_validate(updated)


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Elimina una transacción pendientes.
    """
    service = TransactionService(db)
    
    existing = await service.get_transaction_by_id(
        transaction_id=transaction_id,
        user_id=current_user.id
    )
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )
    
    if existing.status == TransactionStatus.COMPLETED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar una transacción completada"
        )
    
    await service.delete_transaction(transaction_id=transaction_id)
    return None