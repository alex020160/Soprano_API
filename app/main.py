from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .database import Base, engine, SessionLocal
from .models import Member
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Soprano Family Registry API",
    version="1.0.0",
    description="REST API для управления участниками мафиозных семей",
)

app.include_router(router)

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.on_event("startup")
def seed_database():
    db = SessionLocal()
    try:
        if db.query(Member).count() == 0:
            db.add_all(
                [
                    Member(
                        name="Tony Soprano",
                        nickname="Tony",
                        family="DiMeo/Soprano",
                        rank="Boss",
                        status="active",
                    ),
                    Member(
                        name="Silvio Dante",
                        nickname="Sil",
                        family="DiMeo/Soprano",
                        rank="Consigliere",
                        status="active",
                    ),
                    Member(
                        name="Paulie Gualtieri",
                        nickname="Paulie Walnuts",
                        family="DiMeo/Soprano",
                        rank="Capo",
                        status="active",
                    ),
                    Member(
                        name="Christopher Moltisanti",
                        nickname="Chrissy",
                        family="DiMeo/Soprano",
                        rank="Soldier",
                        status="active",
                    ),
                ]
            )
            db.commit()
    finally:
        db.close()


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse(STATIC_DIR / "index.html")
