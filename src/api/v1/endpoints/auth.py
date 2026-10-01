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