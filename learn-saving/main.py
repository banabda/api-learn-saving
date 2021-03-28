from fastapi import FastAPI
from saving import models
from saving.database import engine
from saving.routers import auth, saving, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(saving.router)
app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
