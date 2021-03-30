from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from .token import verify_token
from . import schemas, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # user = db.query(models.User).filter(models.User.email == request.email)
    # if user is None:
    #     raise credentials_exception
    return verify_token(data, credentials_exception)
    # return dict("user": user, "token": verify_token(data, credentials_exception))
    # return user


def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
