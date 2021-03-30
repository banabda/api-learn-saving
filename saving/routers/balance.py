from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import balance

router = APIRouter(
    tags=['Balance'],
    prefix='/balance'
)
get_db = database.get_db


@router.get('/')
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return balance.getall(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Balance, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return balance.create(request, current_user, db)


@router.get('/{id}')
def show(id, response: Response, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return balance.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Balance, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return balance.update(id, request, db)


@router.delete('/{id}')
def destroy(id, current_user: schemas.User = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    return balance.delete(id, db)
