from fastapi import APIRouter

Seller_rout = APIRouter(prefix='/Seller',tags=['Seller'])

@Seller_rout.get('/')
def home():
    return "This is Sellers Home page"