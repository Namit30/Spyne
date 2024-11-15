from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    images = Column(Text)  # Store URLs or paths as JSON-encoded list
    tags = Column(String)  # Store tags as JSON-encoded list or comma-separated string
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")
