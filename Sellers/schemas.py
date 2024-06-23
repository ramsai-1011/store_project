from pydantic import BaseModel

class Seller_schemas(BaseModel):
    unique_id:int
    id:int
    UserName:str
    Password:str
    Store_name:str
    