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