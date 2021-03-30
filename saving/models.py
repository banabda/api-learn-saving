from .database import Base
from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    the_user = relationship('User', back_populates='the_role')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    avatar = Column(String)
    password = Column(String)
    phone = Column(String)
    token = Column(String)
    verified = Column(Boolean, default=False)
    role = Column(Integer, ForeignKey(Role.id), default=1)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    transactions = relationship('Transaction', back_populates='creator')
    the_role = relationship('Role', back_populates='the_user')


class Balance(Base):
    __tablename__ = 'balances'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    amount = Column(Integer)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    transac = relationship('Transaction', back_populates='balan')


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    balance_id = Column(Integer, ForeignKey(Balance.id))
    amount = Column(Integer)
    type = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=None)
    creator = relationship('User', back_populates='transactions')
    balan = relationship('Balance', back_populates='transac')
