from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.gasto import Gasto

def crear(db: Session, datos: dict) -> Gasto:
    gasto = Gasto(**datos)
    db.add(gasto)
    db.commit()
    db.refresh(gasto)
    return gasto

def listar(db: Session, categoria: Optional[str] = None):
    consulta = db.query(Gasto)
    if categoria:
        consulta = consulta.filter(func.lower(Gasto.categoria) == categoria.lower())
    return consulta.order_by(Gasto.id).all()

def obtener_por_id(db: Session, gasto_id: int):
    return db.query(Gasto).filter(Gasto.id == gasto_id).first()

def guardar(db: Session, gasto: Gasto) -> Gasto:
    db.commit()
    db.refresh(gasto)
    return gasto

def eliminar(db: Session, gasto: Gasto) -> None:
    db.delete(gasto)
    db.commit()