from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(tags=['User'], prefix='/user')
get_db = database.get_db


@router.get('/{id}', response_model=schemas.ShowUser)
def show(id, db: Session = Depends(get_db)):
    return user.show(id, db)
