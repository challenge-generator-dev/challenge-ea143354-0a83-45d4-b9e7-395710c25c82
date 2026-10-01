from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from datetime import datetime
import logging

from src.api.v1.models.transaction import Transaction, TransactionStatus
from src.api.v1.schemas.transaction import TransactionCreate, TransactionUpdate
from src.api.v1.utils.idempotency import IdempotencyChecker

logger = logging.getLogger(__name__)


class TransactionService:
    """
    Servicio de lógica de negocio para gestión de transacciones.
    """
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.idempotency_checker = IdempotencyChecker(db)
    
    async def get_transactions(
        self,
        user_id: int,
        skip: int = 0,
        limit: int = 100,
        status: Optional[TransactionStatus] = None
    ) -> List[Transaction]:
        """
        Recupera transacciones con paginación y filtro opcional por estado.
        """
        query = select(Transaction).where(Transaction.user_id == user_id)
        
        if status is not None:
            query = query.where(Transaction.status == status)
        
        query = query.offset(skip).limit(limit).order_by(Transaction.created_at.desc())
        
        result = await self.db.execute(query)
        return list(result.scalars().all())
    
    async def get_transaction_by_id(
        self,
        transaction_id: int,
        user_id: int
    ) -> Optional[Transaction]:
        """
        Obtiene una transacción por ID verificando propiedad del usuario.
        """
        query = select(Transaction).where(
            Transaction.id == transaction_id,
            Transaction.user_id == user_id
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create_transaction(
        self,
        user_id: int,
        transaction_data: TransactionCreate
    ) -> Transaction:
        """
        Crea una nueva transacción con soporte de idempotencia.
        """
        if transaction_data.idempotency_key:
            existing = await self.idempotency_checker.check_key(
                transaction_data.idempotency_key,
                user_id
            )
            if existing:
                logger.info(f"Transacción idempotente encontrada: {transaction_data.idempotency_key}")
                return existing
        
        new_transaction = Transaction(
            user_id=user_id,
            amount=transaction_data.amount,
            description=transaction_data.description,
            status=TransactionStatus.PENDING,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        try:
            self.db.add(new_transaction)
            await self.db.commit()
            await self.db.refresh(new_transaction)
            
            if transaction_data.idempotency_key:
                await self.idempotency_checker.store_key(
                    key=transaction_data.idempotency_key,
                    user_id=user_id,
                    transaction_id=new_transaction.id
                )
            
            logger.info(f"Transacción creada: {new_transaction.id}")
            return new_transaction
            
        except IntegrityError as e:
            await self.db.rollback()
            logger.error(f"Error de integridad al crear transacción: {e}")
            raise ValueError("Error al crear la transacción")
    
    async def update_transaction(
        self,
        transaction_id: int,
        transaction_data: TransactionUpdate
    ) -> Transaction:
        """
        Actualiza una transacción existente.
        """
        update_values = {
            "updated_at": datetime.utcnow()
        }
        
        if transaction_data.description is not None:
            update_values["description"] = transaction_data.description
        if transaction_data.amount is not None:
            update_values["amount"] = transaction_data.amount
        if transaction_data.status is not None:
            update_values["status"] = transaction_data.status
        
        query = update(Transaction).where(
            Transaction.id == transaction_id
        ).values(**update_values)
        
        await self.db.execute(query)
        await self.db.commit()
        
        result = await self.db.get(Transaction, transaction_id)
        logger.info(f"Transacción actualizada: {transaction_id}")
        return result
    
    async def delete_transaction(self, transaction_id: int) -> None:
        """
        Elimina una transacción de la base de datos.
        """
        query = delete(Transaction).where(Transaction.id == transaction_id)
        await self.db.execute(query)
        await self.db.commit()
        logger.info(f"Transacción eliminada: {transaction_id}")
    
    async def complete_transaction(self, transaction_id: int) -> Transaction:
        """
        Completa una transacción cambiando su estado a COMPLETED.
        """
        return await self.update_transaction(
            transaction_id=transaction_id,
            transaction_data=TransactionUpdate(status=TransactionStatus.COMPLETED)
        )
    
    async def cancel_transaction(self, transaction_id: int) -> Transaction:
        """
        Cancela una transacción cambiando su estado a CANCELLED.
        """
        return await self.update_transaction(
            transaction_id=transaction_id,
            transaction_data=TransactionUpdate(status=TransactionStatus.CANCELLED)
        )