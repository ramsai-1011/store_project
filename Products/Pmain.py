from fastapi import APIRouter,Depends,HTTPException,status
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

@Product_rout.get('/get_products')
def get_products(db:Session = Depends(get_db)):
    data = db.query(Products_model).all()
    return data
 

@Product_rout.post('/add_products')
def add_products(dat:Products_schema,db:Session = Depends(get_db)):
    db_user = Products_model(unique_id= dat.unique_id,id=dat.id,P_details=dat.P_details,P_cost=dat.P_cost,P_name=dat.P_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@Product_rout.delete('/delete_products')
def delete_products(id:str,db:Session=Depends(get_db)):
    db_users = db.query(Products_model).filter(Products_model.id==id).first()
    if not db_users:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="User not found")    
    db.delete(db_users)
    db.commit()
    return {"Message":f"following {id} is deleted","Details":"Sucessfully Deleted"}


@Product_rout.put('/update_products')
def update_products(id:str,dat:Products_schema,db:Session=Depends(get_db)):
    db_users = db.query(Products_model).filter(Products_model.id == id).first()
    if not db_users:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="User not found") 
    db_users.P_details = dat.P_details
    db_users.P_cost = dat.P_cost
    db.add(db_users)
    db.commit()
    return {"Message":f"{db_users.id} is updated"}

