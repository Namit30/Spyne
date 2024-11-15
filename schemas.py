from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.exc import IntegrityError
import bcrypt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User  # Add this line to import the User model

class UserCreate(BaseModel):
    username: str
    password: str

class CarCreate(BaseModel):
    title: str
    description: str
    images: List[str]  # List of image URLs or paths, max 10
    tags: List[str]

class CarUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    images: Optional[List[str]]
    tags: Optional[List[str]]

class CarOut(BaseModel):
    id: int
    title: str
    description: str
    images: List[str]
    tags: List[str]
    owner_id: int

# Create an engine and session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_user(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        raise ValueError("Username already exists")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, hashed_password=hashed_password)
    try:
        session.add(new_user)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise ValueError("Failed to create user")
