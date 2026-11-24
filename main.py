from fastapi import FastAPI
from app.database.conexion import Base, engine
from app.models import usuario, gasto
from app.routes import usuarios, gastos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Control de Gastos",
    description="CRUD de usuarios y gastos personales con arquitectura por capas (FastAPI + Neon).",
    version="1.0.0",
)

app.include_router(usuarios.router)
app.include_router(gastos.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API de Control de Gastos funcionando. Documentación en /docs"}