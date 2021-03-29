from . import models
from .database import engine, get_db, SessionLocal
from .routers import auth, saving, user
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemyseeder.basic_seeder import BasicSeeder
from sqlalchemyseeder.resolving_seeder import ResolvingSeeder
app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(saving.router)
app.include_router(user.router)

# session = SessionLocal()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/seed')
def show(db: Session = Depends(get_db)):
    seeder = ResolvingSeeder(session=db)
    seeder.registry.register_class(models.Role)
    seeder.load_entities_from_json_file(
        "saving\\seeder\\role.json")
    db.commit()
    return 'ok'
