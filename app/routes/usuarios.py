from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.usuario_schema import UsuarioCrear, UsuarioActualizar, UsuarioRespuesta
from app.services import usuario_service as service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar(datos: UsuarioCrear, db: Session = Depends(get_db)):
    return service.crear_usuario(db, datos)


@router.get("/", response_model=List[UsuarioRespuesta])
def consultar_todos(db: Session = Depends(get_db)):
    return service.listar_usuarios(db)


@router.get("/{usuario_id}", response_model=UsuarioRespuesta)
def consultar_por_id(usuario_id: int, db: Session = Depends(get_db)):
    return service.obtener_usuario(db, usuario_id)


@router.put("/{usuario_id}", response_model=UsuarioRespuesta)
def actualizar(usuario_id: int, datos: UsuarioActualizar, db: Session = Depends(get_db)):
    return service.actualizar_usuario(db, usuario_id, datos)


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(usuario_id: int, db: Session = Depends(get_db)):
    service.eliminar_usuario(db, usuario_id)