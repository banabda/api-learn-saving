from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime


def getall(db: Session):
    savings = db.query(models.Saving).all()
    return savings


def create(request, db: Session):
    new_Saving = models.Saving(
        title=request.title, body=request.body, user_id=1)
    db.add(new_Saving)
    db.commit()
    db.refresh(new_Saving)
    return new_Saving


def show(id, db: Session):
    saving = db.query(models.Saving).filter(models.Saving.id == id).first()
    if saving:
        saving.code = 200
        return saving
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Saving with the id {id} not exist!")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"id": id, "message": f"Saving with the id {id} not exist!", "code": 404}


def update(id, request, db: Session):
    saving = db.query(models.Saving).filter(models.Saving.id == id)
    if saving.first():
        saving.update(
            {"title": request.title, "body": request.body, "updated_at": datetime.now()})
        db.commit()
        return {"id": id, "message": f"Saving with the id {id} Updated!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Saving with the id {id} not exist!")


def delete(id, db: Session):
    saving = db.query(models.Saving).filter(models.Saving.id == id)
    if saving.first():
        saving.delete(synchronize_session=False)
        db.commit()
        # db.refresh(saving)
        return {"id": id, "message": f"Saving with the id {id} Deleted!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Saving with the id {id} not exist!")
