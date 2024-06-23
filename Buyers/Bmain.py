from fastapi import APIRouter,Depends,HTTPException,status
from .models import *
from .schemas import *
from sqlalchemy.orm import Session
from database_config import engine,get_db
from . import models



models.Base.metadata.create_all(bind=engine)

Buyer_rout = APIRouter(prefix='/buyers',tags=['Buyers'])

@Buyer_rout.get('/')
def home():
    return "This is Buyers Home page"

@Buyer_rout.get('/get_all_buyers')
def get_all_buyers(db:Session=Depends(get_db)):
    db_sellers = db.query(Buyers_mode).all()
    return db_sellers


@Buyer_rout.post('/add_Buyers')
def add_Buyers(dat:Buyers_schema,db:Session=Depends(get_db)):
    db_sellers = Buyers_mode(unique_id=dat.unique_id,id=dat.id,UserName=dat.UserName,Password=dat.Password)
    db.add(db_sellers)
    db.commit()
    return db_sellers


@Buyer_rout.delete('/delete_buyer')
def delete_buyer(id:str, db:Session=Depends(get_db)):
    db_sellers = db.query(Buyers_mode).filter(Buyers_mode.id==id).first()
    if not db_sellers:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Buyers doesn't exits")
    db.delete(db_sellers)
    db.commit()
    return db_sellers


@Buyer_rout.put('/update_buyer')
def update_buyer(id:str,dat:Buyers_schema,db:Session= Depends(get_db)):
    db_sellers = db.query(Buyers_mode).filter(Buyers_mode.id == id).first()
    if not db_sellers:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Buyers doesn't exits")
    db_sellers.UserName = dat.UserName
    db_sellers.Password = dat.Password
    db.add(db_sellers)
    db.commit()
    return db_sellers