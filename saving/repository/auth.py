from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime, timedelta
from ..hashing import Hashing
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


def register(request, db: Session):
    if not db.query(models.User).filter(models.User.email == request.email).first():
        avatar = f'https://avatars.dicebear.com/api/initials/{request.name}.svg'
        user = models.User(name=request.name,
                           email=request.email, avatar=avatar, password=Hashing.bcrypt(request.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"This {request.email} already exist!")


def reset(request, db: Session):
    user = db.query(models.User).filter(
        models.User.email == request.email)
    if user.first():
        password = user.first().password
        if Hashing.verify(request.password_old, password):
            user.update({"password": Hashing.bcrypt(
                request.password_new), "updated_at": datetime.now()})
            db.commit()
            return {"detail": "password changed!"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Password not match!")
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User not found!")


def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(
        models.User.email == request.username)
    _user = user.first()
    if not _user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User not found!")
    if not Hashing.verify(request.password, _user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Wrong credentials!")
    access_token = create_access_token(data={"sub": _user.email})
    user.update({'token': access_token})
    db.commit()
    return {"access_token": access_token, "token_type": "bearer"}
