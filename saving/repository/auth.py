from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime, timedelta
from ..hashing import Hashing
from ..token import create_access_token


def register(request, db: Session):
    if not db.query(models.User).filter(models.User.email == request.email).first():
        user = models.User(name=request.name,
                           email=request.email, password=hashing.Hashing.bcrypt(request.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"This {request.email} already exist!")


def login(request, db: Session):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User not found!")
    if not Hashing.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Wrong credentials!")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
