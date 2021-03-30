from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime


def getall(db: Session):
    balance = db.query(models.Balance).all()
    return balance


def create(request, user, db: Session):
    new_balance = models.Balance(
        user_id=user.id,
        amount=request.amount,
        description=request.description)
    db.add(new_balance)
    db.commit()
    db.refresh(new_balance)
    return new_balance


def show(id, db: Session):
    balance = db.query(models.Balance).filter(
        models.Balance.id == id).first()
    if balance:
        balance.code = 200
        return balance
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"balance with the id {id} not exist!")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"id": id, "message": f"balance with the id {id} not exist!", "code": 404}


def update(id, request, db: Session):
    balance = db.query(models.Balance).filter(
        models.Balance.id == id)
    if balance.first():
        balance.update(
            {"balance_id": request.balance_id, "amount": request.amount, "type": request.type, "description": request.description, "updated_at": datetime.now()})
        db.commit()
        return {"id": id, "message": f"balance with the id {id} Updated!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"balance with the id {id} not exist!")


def delete(id, db: Session):
    balance = db.query(models.balance).filter(
        models.balance.id == id)
    if balance.first():
        balance.delete(synchronize_session=False)
        db.commit()
        # db.refresh(balance)
        return {"id": id, "message": f"balance with the id {id} Deleted!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"balance with the id {id} doesn't exist!")
