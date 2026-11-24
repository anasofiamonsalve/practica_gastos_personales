from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UsuarioCrear(BaseModel):
    nombre: str = Field(min_length=1, max_length=150)
    correo: EmailStr
    password: str = Field(min_length=6, max_length=72)


class UsuarioActualizar(BaseModel):
    nombre: str = Field(min_length=1, max_length=150)
    correo: EmailStr
    password: Optional[str] = Field(None, min_length=6, max_length=72)


class UsuarioRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    correo: EmailStr