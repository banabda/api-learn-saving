from . import models
from .database import engine, get_db, SessionLocal
from .routers import auth, transaction, user
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemyseeder.basic_seeder import BasicSeeder
from sqlalchemyseeder.resolving_seeder import ResolvingSeeder
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(transaction.router)
app.include_router(user.router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/seed')
def set(db: Session = Depends(get_db)):
    seeder = ResolvingSeeder(session=db)
    status = []
    if len(db.query(models.Role).all()) == 0:
        seeder.registry.register_class(models.Role)
        seeder.load_entities_from_json_file(
            "saving\\seeder\\role.json")
        status.append('role seeder created')
    if len(db.query(models.User).all()) == 0:
        seeder.registry.register_class(models.User)
        seeder.load_entities_from_json_file(
            "saving\\seeder\\user.json")
        status.append('user seeder created')
    if len(status) > 0:
        db.commit()
        return {'status': 'seed success', 'table': status}
    return {'status': 'nothing to migrate, all set on your table'}
