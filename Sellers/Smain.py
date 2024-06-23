from fastapi import APIRouter,Depends,HTTPException,status
from .models import *
from .schemas import *
from sqlalchemy.orm import Session
from database_config import engine,get_db
from . import models



models.Base.metadata.create_all(bind=engine)

Seller_rout = APIRouter(prefix='/Seller',tags=['Seller'])

@Seller_rout.get('/')
def home():
    return "This is Sellers Home page"

@Seller_rout.get('/get_all_sellers')
def get_all_sellers(db:Session=Depends(get_db)):
    db_sellers = db.query(Sellers_model).all()
    return db_sellers


@Seller_rout.post('/add_users')
def add_users(dat:Seller_schemas,db:Session=Depends(get_db)):
    db_sellers = Sellers_model(unique_id=dat.unique_id,id=dat.id,UserName=dat.UserName,Password=dat.Password,Store_name=dat.Store_name)
    db.add(db_sellers)
    db.commit()
    return db_sellers


@Seller_rout.delete('/delete_user')
def delete_user(id:str, db:Session=Depends(get_db)):
    db_sellers = db.query(Sellers_model).filter(Sellers_model.id==id).first()
    if not db_sellers:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Users doesn't exits")
    db.delete(db_sellers)
    db.commit()
    return db_sellers