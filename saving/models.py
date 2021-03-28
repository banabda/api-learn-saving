from .database import Base
from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Saving(Base):
    __tablename__ = 'savings'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    creator = relationship('User', back_populates='savings')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    savings = relationship('Saving', back_populates='creator')
