from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Saving(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    savings: List[Saving] = []

    class Config():
        orm_mode = True


class ShowSaving(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
