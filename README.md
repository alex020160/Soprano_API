# Soprano Family Registry API

## Стек

- Python
- FastAPI
- SQLAlchemy
- SQLite локально / PostgreSQL в облаке
- HTML + JavaScript frontend
- Render для развёртывания

## Запуск локально

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Открыть:

- приложение: http://127.0.0.1:8000/
- Swagger: http://127.0.0.1:8000/docs

## API

- GET `/api/members`
- GET `/api/members/{id}`
- POST `/api/members`
- PUT `/api/members/{id}`
- PATCH `/api/members/{id}`
- DELETE `/api/members/{id}`
- DELETE `/api/members`
- GET `/health`

## Пример POST

```json
{
  "name": "Bobby Baccalieri",
  "nickname": "Bobby",
  "family": "DiMeo/Soprano",
  "rank": "Capo",
  "status": "active"
}
```
