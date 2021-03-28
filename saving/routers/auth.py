from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, hashing, database, token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..repository import auth

router = APIRouter(
    tags=['auth'],
    # prefix='/auth'
)
get_db = database.get_db


@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def register(request: schemas.User, db: Session = Depends(get_db)):
    return auth.register(request, db)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hashing.Hashing.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
