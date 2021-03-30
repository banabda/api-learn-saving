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


def update(id, request, db: Session):
    user = db.query(models.User).filter(
        models.User.id == id)
    if user.first():
        user.update(
            {"name": request.name, "avatar": request.avatar, "phone": request.phone, "updated_at": datetime.now()})
        db.commit()
        return {"id": id, "message": f"User with the id {id} Updated!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with the id {id} not exist!")
