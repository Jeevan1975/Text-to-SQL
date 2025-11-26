from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime)
    

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user = Column(String, ForeignKey("users.id"))
    total = Column(Float)
    created_at = Column(DateTime)
    
