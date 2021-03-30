from sqlalchemy.orm import Session
from .. import schemas, models
from fastapi import status, Response, HTTPException
from datetime import datetime


def getall(db: Session):
    transactions = db.query(models.Transaction).all()
    return transactions


def create(request, db: Session):
    new_Transaction = models.Transaction(
        title=request.title, body=request.body, user_id=1)
    db.add(new_Transaction)
    db.commit()
    db.refresh(new_Transaction)
    return new_Transaction


def show(id, db: Session):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == id).first()
    if transaction:
        transaction.code = 200
        return transaction
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Transaction with the id {id} not exist!")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"id": id, "message": f"Transaction with the id {id} not exist!", "code": 404}


def update(id, request, db: Session):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == id)
    if transaction.first():
        transaction.update(
            {"title": request.title, "body": request.body, "updated_at": datetime.now()})
        db.commit()
        return {"id": id, "message": f"Transaction with the id {id} Updated!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Transaction with the id {id} not exist!")


def delete(id, db: Session):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == id)
    if transaction.first():
        transaction.delete(synchronize_session=False)
        db.commit()
        # db.refresh(transaction)
        return {"id": id, "message": f"Transaction with the id {id} Deleted!", "code": 204}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Transaction with the id {id} doesn't exist!")
