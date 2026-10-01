"""
Configuración de SQLAlchemy y sesión de base de datos.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.types import String, Integer, DateTime, Enum as SQLEnum
from typing import AsyncGenerator
import logging

from src.api.v1.config.settings import Settings

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    """Clase base para los modelos de SQLAlchemy."""
    pass


class DatabaseConfig:
    """Gestor de configuración de base de datos."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self._engine = None
        self._async_session_maker = None

    def get_async_engine(self):
        """Obtiene o crea el motor asíncrono de base de datos."""
        if self._engine is None:
            database_url = self.settings.DATABASE_URL
            if database_url.startswith("postgresql://"):
                database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
            elif database_url.startswith("postgres://"):
                database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)

            self._engine = create_async_engine(
                database_url,
                echo=self.settings.DEBUG,
                pool_size=20,
                max_overflow=10,
                pool_pre_ping=True,
                pool_recycle=3600,
            )
            logger.info(f"Motor de base de datos creado: {database_url[:30]}...")
        return self._engine

    def get_async_session_maker(self):
        """Obtiene el creador de sesiones asíncronas."""
        if self._async_session_maker is None:
            engine = self.get_async_engine()
            self._async_session_maker = async_sessionmaker(
                engine,
                class_=AsyncSession,
                expire_on_commit=False,
                autocommit=False,
                autoflush=False,
            )
            logger.info("Creador de sesiones asíncronas inicializado")
        return self._async_session_maker

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Generador de sesiones de base de datos para inyección de dependencias."""
        session_maker = self.get_async_session_maker()
        async with session_maker() as session:
            try:
                yield session
                await session.commit()
            except Exception as e:
                await session.rollback()
                logger.error(f"Error en sesión de base de datos: {e}")
                raise
            finally:
                await session.close()

    async def create_tables(self):
        """Crea todas las tablas definidas en los modelos."""
        engine = self.get_async_engine()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Tablas de base de datos creadas exitosamente")

    async def drop_tables(self):
        """Elimina todas las tablas de la base de datos."""
        engine = self.get_async_engine()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        logger.info("Tablas de base de datos eliminadas")

    async def close(self):
        """Cierra las conexiones del motor de base de datos."""
        if self._engine:
            await self._engine.dispose()
            logger.info("Conexiones de base de datos cerradas")


db_config: DatabaseConfig = None


def get_db_config(settings: Settings) -> DatabaseConfig:
    """Proveedor de configuración de base de datos."""
    global db_config
    if db_config is None:
        db_config = DatabaseConfig(settings)
    return db_config