from sqlalchemy.orm import Session
from app.models.usuario import Usuario


def crear(db: Session, nombre: str, correo: str, password_hash: str) -> Usuario:
    usuario = Usuario(nombre=nombre, correo=correo, password_hash=password_hash)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def listar(db: Session):
    return db.query(Usuario).order_by(Usuario.id).all()


def obtener_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def obtener_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def guardar(db: Session, usuario: Usuario) -> Usuario:
    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar(db: Session, usuario: Usuario) -> None:
    db.delete(usuario)
    db.commit()