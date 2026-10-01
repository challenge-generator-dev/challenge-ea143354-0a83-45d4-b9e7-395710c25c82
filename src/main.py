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