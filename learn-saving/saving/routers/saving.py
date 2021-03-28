from typing import List
from fastapi import APIRouter, Depends, status, Response
from saving import schemas, database, oauth2
from sqlalchemy.orm import Session
from saving.repository import saving

router = APIRouter(
    tags=['saving'],
    prefix='/saving'
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowSaving])
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return saving.getall(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Saving, db: Session = Depends(get_db)):
    return saving.create(request, db)


@router.get('/{id}', response_model=schemas.ShowSaving)
def show(id, response: Response, db: Session = Depends(get_db)):
    return saving.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Saving, db: Session = Depends(get_db)):
    return saving.update(id, request, db)


@router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db)):
    return saving.delete(id, db)
