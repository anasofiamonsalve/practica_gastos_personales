from sqlalchemy import Column, Integer, String, Numeric, Date
from app.database.conexion import Base


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    concepto = Column(String(200), nullable=False)
    valor = Column(Numeric(12, 2), nullable=False)
    fecha = Column(Date, nullable=False)
    categoria = Column(String(100), nullable=False, index=True)