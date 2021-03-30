from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import transaction

router = APIRouter(
    tags=['Transaction'],
    prefix='/transaction'
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowTransaction])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return transaction.getall(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Transaction, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    # return transaction.create(request, db)
    return oauth2.get_current_user


@router.get('/{id}', response_model=schemas.ShowTransaction)
def show(id, response: Response, db: Session = Depends(get_db)):
    return transaction.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Transaction, db: Session = Depends(get_db)):
    return transaction.update(id, request, db)


@router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db)):
    return transaction.delete(id, db)
