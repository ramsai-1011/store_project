from fastapi import APIRouter

Buyer_rout = APIRouter(prefix='/buyers',tags=['Buyers'])

@Buyer_rout.get('/')
def home():
    return "This is buyers Home page"