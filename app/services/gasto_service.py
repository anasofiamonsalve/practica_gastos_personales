from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import gasto_repository as repo
from app.schemas.gasto_schema import GastoCrear, GastoActualizar


def crear_gasto(db: Session, datos: GastoCrear):
    return repo.crear(db, {
        "concepto": datos.concepto.strip(),
        "valor": datos.valor,
        "fecha": datos.fecha,
        "categoria": datos.categoria.strip(),
    })


def listar_gastos(db: Session, categoria: Optional[str] = None):
    return repo.listar(db, categoria.strip() if categoria else None)


def obtener_gasto(db: Session, gasto_id: int):
    gasto = repo.obtener_por_id(db, gasto_id)
    if not gasto:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Gasto no encontrado")
    return gasto


def actualizar_gasto(db: Session, gasto_id: int, datos: GastoActualizar):
    gasto = obtener_gasto(db, gasto_id)
    gasto.concepto = datos.concepto.strip()
    gasto.valor = datos.valor
    gasto.fecha = datos.fecha
    gasto.categoria = datos.categoria.strip()
    return repo.guardar(db, gasto)


def eliminar_gasto(db: Session, gasto_id: int) -> None:
    repo.eliminar(db, obtener_gasto(db, gasto_id))