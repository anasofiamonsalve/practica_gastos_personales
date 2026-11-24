from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from app.database.conexion import get_db
from app.schemas.gasto_schema import GastoCrear, GastoActualizar, GastoRespuesta
from app.services import gasto_service as service

router = APIRouter(prefix="/gastos", tags=["Gastos"])


@router.post("/", response_model=GastoRespuesta, status_code=status.HTTP_201_CREATED)
def registrar(datos: GastoCrear, db: Session = Depends(get_db)):
    return service.crear_gasto(db, datos)


@router.get("/", response_model=List[GastoRespuesta])
def consultar_todos(
    categoria: Optional[str] = Query(None, description="Filtrar por categoría (ej: Alimentación)"),
    db: Session = Depends(get_db),
):
    return service.listar_gastos(db, categoria)


@router.get("/{gasto_id}", response_model=GastoRespuesta)
def consultar_por_id(gasto_id: int, db: Session = Depends(get_db)):
    return service.obtener_gasto(db, gasto_id)


@router.put("/{gasto_id}", response_model=GastoRespuesta)
def actualizar(gasto_id: int, datos: GastoActualizar, db: Session = Depends(get_db)):
    return service.actualizar_gasto(db, gasto_id, datos)


@router.delete("/{gasto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(gasto_id: int, db: Session = Depends(get_db)):
    service.eliminar_gasto(db, gasto_id)