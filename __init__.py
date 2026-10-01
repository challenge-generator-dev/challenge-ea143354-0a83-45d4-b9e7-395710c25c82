"""
Banco Digital API - Paquete raíz de la aplicación.

Este módulo inicializa la aplicación FastAPI y expone los componentes
principales para su uso desde fuera del paquete.
"""

import logging
import sys
from typing import TYPE_CHECKING

__version__ = "1.0.0"
__author__ = "Banco Digital Team"
__app_name__ = "Banco Digital API"

if TYPE_CHECKING:
    from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def get_application() -> "FastAPI":
    """
    Retorna la instancia de la aplicación FastAPI.
    
    Esta función es el punto de acceso principal para obtener
    la aplicación configurada y lista para ejecutar.
    
    Returns:
        FastAPI: Instancia configurada de la aplicación.
    """
    from src.main import app
    return app

def get_version() -> str:
    """
    Retorna la versión actual de la aplicación.
    
    Returns:
        str: Versión semántica del paquete.
    """
    return __version__

def get_app_name() -> str:
    """
    Retorna el nombre de la aplicación.
    
    Returns:
        str: Nombre oficial de la aplicación.
    """
    return __app_name__

def configure_logging(level: int = logging.INFO) -> None:
    """
    Configura el nivel de logging para toda la aplicación.
    
    Args:
        level: Nivel de logging (default: INFO).
    """
    logging.getLogger().setLevel(level)
    logger.info(f"Logging configurado a nivel: {logging.getLevelName(level)}")

def check_dependencies() -> bool:
    """
    Verifica que las dependencias principales estén instaladas.
    
    Returns:
        bool: True si todas las dependencias críticas están disponibles.
    """
    required_packages = [
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "pydantic_settings",
        "python_jose",
        "passlib",
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        logger.error(f"Dependencias faltantes: {', '.join(missing)}")
        return False
    
    logger.info("Todas las dependencias verificadas correctamente")
    return True

def initialize_app() -> None:
    """
    Inicializa la aplicación configurando logging y verificando dependencias.
    
    Esta función debe llamarse al arranque de la aplicación para
    asegurar que todo está correctamente configurado.
    """
    logger.info(f"Inicializando {__app_name__} v{__version__}")
    configure_logging()
    
    if not check_dependencies():
        logger.warning("Algunas dependencias no están instaladas correctamente")
    
    logger.info("Aplicación inicializada correctamente")

if __name__ == "__main__":
    initialize_app()
    print(f"{__app_name__} v{__version__} - Ejecución directa")