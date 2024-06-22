from fastapi import FastAPI
from Buyers import Bmain
from Sellers import Smain
from Products import Pmain

app = FastAPI()
app.include_router(Bmain.Buyer_rout)
app.include_router(Smain.Seller_rout)
app.include_router(Pmain.Product_rout)

@app.get('/')
def home():
    return "This is the Home Page"