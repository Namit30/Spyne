from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Car, User
from schemas import UserCreate, CarCreate, CarUpdate, CarOut
from auth import create_access_token, authenticate_user, get_current_user
from typing import List
from auth import get_password_hash


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"msg": "User created successfully"}

@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token({"sub": db_user.id})
    return {"access_token": access_token}

@app.post("/cars/", response_model=CarOut)
def create_car(car: CarCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_car = Car(title=car.title, description=car.description, images=car.images[:10], tags=car.tags, owner_id=current_user.id)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.get("/cars/", response_model=List[CarOut])
def read_cars(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Car).filter(Car.owner_id == current_user.id).all()

@app.get("/cars/search/")
def search_cars(query: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Car).filter(
        Car.owner_id == current_user.id,
        (Car.title.contains(query) | Car.description.contains(query) | Car.tags.contains(query))
    ).all()

@app.get("/cars/{car_id}", response_model=CarOut)
def read_car(car_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_car = db.query(Car).filter(Car.id == car_id, Car.owner_id == current_user.id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@app.put("/cars/{car_id}", response_model=CarOut)
def update_car(car_id: int, car: CarUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_car = db.query(Car).filter(Car.id == car_id, Car.owner_id == current_user.id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    for field, value in car.dict(exclude_unset=True).items():
        setattr(db_car, field, value)
    db.commit()
    return db_car

@app.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_car = db.query(Car).filter(Car.id == car_id, Car.owner_id == current_user.id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(db_car)
    db.commit()
    return {"msg": "Car deleted"}

@app.get("/api/docs")
def get_api_docs():
    # Swagger UI can be used as default documentation for this endpoint
    pass
