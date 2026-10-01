# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `src/api/v1/endpoints/auth.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `src/api/v1/utils/security.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `src/api/v1/middlewares/auth_middleware.py` — El topic pide autenticacion/seguridad: este archivo es el ejercicio.
- `tests/unit/test_transaction_service.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- `tests/integration/test_transactions_endpoints.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `src/api/v1/endpoints/transactions.py` — `TransactionService.get`: Se invoca `get` sobre `TransactionService`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/endpoints/transactions.py` — `TransactionService.post`: Se invoca `post` sobre `TransactionService`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/endpoints/transactions.py` — `TransactionService.put`: Se invoca `put` sobre `TransactionService`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/endpoints/transactions.py` — `TransactionService.delete`: Se invoca `delete` sobre `TransactionService`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/config/database.py` — `Settings.info`: Se invoca `info` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/config/database.py` — `Settings.error`: Se invoca `error` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/utils/idempotency.py` — `Base.debug`: Se invoca `debug` sobre `Base`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- `src/api/v1/utils/idempotency.py` — `Base.info`: Se invoca `info` sobre `Base`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -c "import app.main"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Crear una API REST con FastAPI, SQLAlchemy y autenticación JWT

### Reto
- Tema: Python FastAPI
- Seniority: junior-l1
- Tipo: practical
- Título: Desarrollo de una API REST en el dominio de banca
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición de endpoints y autenticación — objetivo: Definir los endpoints de la API y asegurar la autenticación de los usuarios. — entregable (NO resolver): Documentación de los endpoints y la implementación de la autenticación JWT.
- Fase 2: Implementación de la lógica de negocio — objetivo: Implementar la lógica de negocio para la gestión de transacciones. — entregable (NO resolver): Implementación de la lógica de negocio para la gestión de transacciones.
- Fase 3: Integración y pruebas — objetivo: Integrar los componentes y realizar pruebas exhaustivas de la API. — entregable (NO resolver): API REST completamente funcional y documentada.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: src/main.py ===
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.config.settings import settings
from src.api.v1.endpoints import transactions, auth
import uvicorn

app = FastAPI(
    title="Banco Digital API",
    description="API REST para gestión de transacciones bancarias",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["transactions"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Banco Digital"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
"

// === ARCHIVO: src/api/v1/config/settings.py ===
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, field_validator
from typing import List, Optional

class Settings(BaseSettings):
    APP_NAME: str = "Banco Digital API"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = False

    # Configuración CORS
    CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000"]

    # Configuración JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Configuración de base de datos
    DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # Configuración de seguridad
    PASSWORD_HASH_ALGORITHM: str = "bcrypt"
    IDEMPOTENCY_KEY_EXPIRE_HOURS: int = 24

    class Config:
        env_file = ".env"
        case_sensitive = True

    @field_validator('DATABASE_URL', mode='before')
    def validate_database_url(cls, v):
        if not v:
            raise ValueError("DATABASE_URL no puede estar vacío")
        return v

    @field_validator('JWT_SECRET_KEY', mode='before')
    def validate_jwt_secret(cls, v):
        if not v or len(v) < 32:
            raise ValueError("JWT_SECRET_KEY debe tener al menos 32 caracteres")
        return v

settings = Settings()
"

// === ARCHIVO: requirements.txt ===
fastapi==0.115.0
uvicorn==0.30.6
sqlalchemy==2.0.32
pydantic==2.8.2
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.9
pydantic-settings==2.4.0
psycopg2-binary==2.9.9
alembic==1.13.2
pytest==8.3.2
httpx==0.27.0

// === ARCHIVO: src/api/v1/models/transaction.py ===
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from src.api.v1.config.database import Base


class TransactionStatus(PyEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    idempotency_key = Column(String, unique=True, nullable=True)

    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, status={self.status})>"


# Modelo User para relación (ya existe en otro lote, solo referencia)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    transactions = relationship("Transaction", back_populates="user")

// === ARCHIVO: __init__.py ===
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

// === ARCHIVO: src/api/v1/endpoints/transactions.py ===
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

// === ARCHIVO: src/api/v1/endpoints/auth.py ===
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.config.database import get_db
from src.api.v1.schemas.auth import LoginRequest, LoginResponse, TokenData

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/login", response_model=LoginResponse)
async def login(
    credentials: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Endpoint de autenticación. Superficie de práctica - implementar lógica de validación.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implementar lógica de autenticación con validación de credenciales"
    )


@router.post("/refresh", response_model=LoginResponse)
async def refresh_token(
    token_data: TokenData,
    db: AsyncSession = Depends(get_db)
):
    """
    Refresca un token JWT válido. Superficie de práctica.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implementar lógica de refresh de token"
    )


@router.post("/logout")
async def logout():
    """
    Cierra la sesión del usuario. Superficie de práctica.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implementar lógica de logout"
    )

// === ARCHIVO: src/api/v1/services/transaction_service.py ===
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

// === ARCHIVO: src/api/v1/utils/security.py ===
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

// === ARCHIVO: src/api/v1/config/database.py ===
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

// === ARCHIVO: src/api/v1/utils/idempotency.py ===
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

// === ARCHIVO: src/api/v1/middlewares/auth_middleware.py ===
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from typing import Optional

from src.api.v1.config.settings import Settings

security = HTTPBearer(auto_error=False)


async def verify_token(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    settings: Settings = Depends(lambda: Settings()),
) -> dict:
    """
    Valida el token JWT y retorna el payload decodificado.
    """
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se encontró el token de autenticación",
        )

    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.jwt_secret,
            algorithms=["HS256"],
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token JWT inválido o expirado",
        )


async def get_current_user(payload: dict = Depends(verify_token)) -> dict:
    """
    Extrae la información del usuario del payload del token.
    """
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token sin información de usuario",
        )
    return {"user_id": user_id, "email": payload.get("email")}


def require_role(allowed_roles: list[str]):
    """
    Dependencia para verificar roles del usuario.
    """
    async def role_checker(user: dict = Depends(get_current_user)):
        user_role = user.get("role", "user")
        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permiso para realizar esta acción",
            )
        return user
    return role_checker

// === ARCHIVO: tests/unit/test_transaction_service.py ===
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from decimal import Decimal
from datetime import datetime

from src.api.v1.models.transaction import Transaction, TransactionStatus
from src.api.v1.services.transaction_service import TransactionService


@pytest.fixture
def mock_db_session():
    """Fixture que proporciona un mock de la sesión de base de datos."""
    session = AsyncMock()
    return session


@pytest.fixture
def transaction_service(mock_db_session):
    """Fixture que proporciona una instancia del servicio de transacciones."""
    return TransactionService(db_session=mock_db_session)


@pytest.fixture
def sample_transaction_data():
    """Fixture que proporciona datos de ejemplo para una transacción."""
    return {
        "user_id": "user-123",
        "amount": Decimal("1000.00"),
        "description": "Pago de servicios",
        "transaction_type": "debit",
    }


class TestCreateTransaction:
    """Tests para el método de creación de transacciones."""

    @pytest.mark.asyncio
    async def test_create_transaction_success(
        self,
        transaction_service,
        sample_transaction_data,
    ):
        """
        Verifica que se puede crear una transacción exitosamente.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_invalid_amount(
        self,
        transaction_service,
    ):
        """
        Verifica que se rechaza una transacción con monto inválido.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_idempotency(
        self,
        transaction_service,
        sample_transaction_data,
    ):
        """
        Verifica la idempotencia en la creación de transacciones.
        """
        pass


class TestGetTransactions:
    """Tests para el método de obtención de transacciones."""

    @pytest.mark.asyncio
    async def test_get_transactions_by_user(
        self,
        transaction_service,
    ):
        """
        Verifica que se pueden obtener todas las transacciones de un usuario.
        """
        pass

    @pytest.mark.asyncio
    async def test_get_transaction_by_id(
        self,
        transaction_service,
    ):
        """
        Verifica que se puede obtener una transacción por su ID.
        """
        pass

    @pytest.mark.asyncio
    async def test_get_transactions_with_filters(
        self,
        transaction_service,
    ):
        """
        Verifica el filtrado de transacciones por estado y fecha.
        """
        pass


class TestUpdateTransaction:
    """Tests para el método de actualización de transacciones."""

    @pytest.mark.asyncio
    async def test_update_transaction_status(
        self,
        transaction_service,
    ):
        """
        Verifica que se puede actualizar el estado de una transacción.
        """
        pass

    @pytest.mark.asyncio
    async def test_update_completed_transaction_fails(
        self,
        transaction_service,
    ):
        """
        Verifica que no se puede actualizar una transacción completada.
        """
        pass


class TestDeleteTransaction:
    """Tests para el método de eliminación de transacciones."""

    @pytest.mark.asyncio
    async def test_delete_transaction(
        self,
        transaction_service,
    ):
        """
        Verifica que se puede eliminar una transacción.
        """
        pass

    @pytest.mark.asyncio
    async def test_delete_completed_transaction_fails(
        self,
        transaction_service,
    ):
        """
        Verifica que no se puede eliminar una transacción completada.
        """
        pass

// === ARCHIVO: tests/integration/test_transactions_endpoints.py ===
import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from decimal import Decimal
from datetime import datetime

from src.main import app
from src.api.v1.models.transaction import TransactionStatus


@pytest.fixture
def mock_auth_headers():
    """
    Fixture que proporciona headers de autenticación válidos.
    """
    return {"Authorization": "Bearer test-token-valid"}


@pytest.fixture
def mock_invalid_headers():
    """
    Fixture que proporciona headers de autenticación inválidos.
    """
    return {"Authorization": "Bearer invalid-token"}


@pytest.fixture
def sample_transaction_payload():
    """
    Fixture que proporciona el payload para crear una transacción.
    """
    return {
        "user_id": "user-123",
        "amount": 1000.00,
        "description": "Pago de servicios",
        "transaction_type": "debit",
    }


class TestCreateTransactionEndpoint:
    """Tests de integración para el endpoint de creación de transacciones."""

    @pytest.mark.asyncio
    async def test_create_transaction_success(
        self,
        mock_auth_headers,
        sample_transaction_payload,
    ):
        """
        Verifica que el endpoint de creación retorna 201 exitosamente.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_unauthorized(
        self,
        sample_transaction_payload,
    ):
        """
        Verifica que el endpoint rechaza solicitudes sin autenticación.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_invalid_token(
        self,
        mock_invalid_headers,
        sample_transaction_payload,
    ):
        """
        Verifica que el endpoint rechaza tokens inválidos.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_invalid_payload(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que el endpoint valida el payload correctamente.
        """
        pass

    @pytest.mark.asyncio
    async def test_create_transaction_idempotent(
        self,
        mock_auth_headers,
        sample_transaction_payload,
    ):
        """
        Verifica que el endpoint maneja idempotencia correctamente.
        """
        pass


class TestGetTransactionsEndpoint:
    """Tests de integración para el endpoint de obtención de transacciones."""

    @pytest.mark.asyncio
    async def test_get_all_transactions(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que se pueden obtener todas las transacciones del usuario.
        """
        pass

    @pytest.mark.asyncio
    async def test_get_transaction_by_id(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que se puede obtener una transacción específica.
        """
        pass

    @pytest.mark.asyncio
    async def test_get_transactions_with_status_filter(
        self,
        mock_auth_headers,
    ):
        """
        Verifica el filtrado de transacciones por estado.
        """
        pass

    @pytest.mark.asyncio
    async def test_get_transactions_not_found(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que el endpoint retorna 404 para transacciones inexistentes.
        """
        pass


class TestUpdateTransactionEndpoint:
    """Tests de integración para el endpoint de actualización de transacciones."""

    @pytest.mark.asyncio
    async def test_update_transaction_status(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que se puede actualizar el estado de una transacción.
        """
        pass

    @pytest.mark.asyncio
    async def test_update_transaction_not_found(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que el endpoint retorna 404 para transacciones inexistentes.
        """
        pass


class TestDeleteTransactionEndpoint:
    """Tests de integración para el endpoint de eliminación de transacciones."""

    @pytest.mark.asyncio
    async def test_delete_transaction_success(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que se puede eliminar una transacción exitosamente.
        """
        pass

    @pytest.mark.asyncio
    async def test_delete_transaction_not_found(
        self,
        mock_auth_headers,
    ):
        """
        Verifica que el endpoint retorna 404 para transacciones inexistentes.
        """
        pass
```
