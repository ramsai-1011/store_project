from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .schemas import *
from .models import *
from . import models
from database_config import get_db,engine
models.Base.metadata.create_all(bind=engine)

Product_rout = APIRouter(prefix='/Products',tags=['Products'])

@Product_rout.get('/')
def home():
    return "This is Product Home page"

@Product_rout.post('/get_products')
def get_products(db:Session = Depends(get_db)):
    data = db.query(Products_model).all()
    return data
 

@Product_rout.post('/add_products')
def add_products(dat:Products_schema,db:Session = Depends(get_db)):
    db_user = Products_model(id=dat.id,P_details=dat.P_details,P_cost=dat.P_cost,P_name=dat.P_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

