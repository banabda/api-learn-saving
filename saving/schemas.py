from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Transaction(BaseModel):
    user_id: int
    balance_id: int
    amount: int
    type: str
    description: str

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str = "example name"
    email: str = 'example@example.com'
    password: str = '123123123'

    class Config():
        orm_mode = True


class Role(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True


class RoleName(BaseModel):
    name: str

    class Config():
        orm_mode = True


class UserDetail(BaseModel):
    id: int
    name: str
    email: str
    avatar: Optional[str] = None
    phone: Optional[str] = None
    token: Optional[str] = None
    verified: bool
    the_role: RoleName

    class Config():
        orm_mode = True


class UserProfile(BaseModel):
    name: str
    avatar: Optional[str] = None
    phone: Optional[str] = None

    class Config():
        orm_mode = True


class UserPassword(BaseModel):
    email: str
    password_old: str
    password_new: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    transactions: List[Transaction] = []

    class Config():
        orm_mode = True


class ShowTransaction(BaseModel):
    title: str
    body: str
    creator: UserProfile

    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
