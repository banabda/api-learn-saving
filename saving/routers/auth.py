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


@router.post('/resetpassword')
def reset(request: schemas.UserPassword, db: Session = Depends(get_db)):
    return auth.reset(request, db)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth.login(request, db)
