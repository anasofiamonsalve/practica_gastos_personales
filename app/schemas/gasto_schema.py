from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


class GastoCrear(BaseModel):
    concepto: str = Field(min_length=1, max_length=200)
    valor: Decimal = Field(max_digits=12, decimal_places=2)
    fecha: date
    categoria: str = Field(min_length=1, max_length=100)


class GastoActualizar(GastoCrear):
    pass


class GastoRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    concepto: str
    valor: Decimal
    fecha: date
    categoria: str