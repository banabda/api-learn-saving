from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(tags=['User'], prefix='/user')
get_db = database.get_db


@router.get('/{id}', response_model=schemas.UserDetail)
def show(id, db: Session = Depends(get_db)):
    return user.show(id, db)


@router.put('/{id}')
def profile(id, request: schemas.UserProfile, db: Session = Depends(get_db)):
    return user.update(id, request, db)
