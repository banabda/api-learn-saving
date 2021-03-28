from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime


def show(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user:
        user.code = 200
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with the id {id} not exist!")
