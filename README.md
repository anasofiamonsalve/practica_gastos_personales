# API de Control de Gastos

API REST con **FastAPI** y **PostgreSQL (Neon)** para administrar usuarios y gastos personales, con arquitectura por capas.

**Aprendiz:** Ana Sofía Monsalve Higuita

## Módulos
- **Usuarios:** CRUD completo, contraseña con hash (bcrypt), correo único.
- **Gastos:** CRUD completo + filtro por categoría (`GET /gastos/?categoria=Comida`).

## Endpoints
| Método | Endpoint | Descripción |
|---|---|---|
| POST | /usuarios/ | Registrar usuario |
| GET | /usuarios/ | Consultar usuarios |
| GET | /usuarios/{id} | Consultar usuario por ID |
| PUT | /usuarios/{id} | Actualizar usuario |
| DELETE | /usuarios/{id} | Eliminar usuario |
| POST | /gastos/ | Registrar gasto |
| GET | /gastos/ | Consultar gastos (opcional `?categoria=`) |
| GET | /gastos/{id} | Consultar gasto por ID |
| PUT | /gastos/{id} | Actualizar gasto |
| DELETE | /gastos/{id} | Eliminar gasto |

## Arquitectura
`routes` → `services` → `repositories` → `models` / `database`, con `schemas` para validar entrada y salida.

## Ejecutar en local
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Crea un archivo `.env` con tu `DATABASE_URL` de Neon.
Swagger: http://127.0.0.1:8000/docs

## Despliegue en Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Variable de entorno: `DATABASE_URL`