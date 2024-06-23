from pydantic import BaseModel

class Buyers_schema(BaseModel):
    unique_id:int
    id:int
    UserName:str
    Password:str
    