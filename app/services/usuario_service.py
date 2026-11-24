import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import usuario_repository as repo
from app.schemas.usuario_schema import UsuarioCrear, UsuarioActualizar


def _hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def crear_usuario(db: Session, datos: UsuarioCrear):
    if repo.obtener_por_correo(db, datos.correo):
        raise HTTPException(status.HTTP_409_CONFLICT, "El correo ya está registrado")
    return repo.crear(db, datos.nombre.strip(), datos.correo, _hash(datos.password))


def listar_usuarios(db: Session):
    return repo.listar(db)


def obtener_usuario(db: Session, usuario_id: int):
    usuario = repo.obtener_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuario no encontrado")
    return usuario


def actualizar_usuario(db: Session, usuario_id: int, datos: UsuarioActualizar):
    usuario = obtener_usuario(db, usuario_id)
    existente = repo.obtener_por_correo(db, datos.correo)
    if existente and existente.id != usuario_id:
        raise HTTPException(status.HTTP_409_CONFLICT, "El correo ya está registrado")
    usuario.nombre = datos.nombre.strip()
    usuario.correo = datos.correo
    if datos.password:
        usuario.password_hash = _hash(datos.password)
    return repo.guardar(db, usuario)


def eliminar_usuario(db: Session, usuario_id: int) -> None:
    repo.eliminar(db, obtener_usuario(db, usuario_id))