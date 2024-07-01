from pydantic import BaseModel

class Products_schema(BaseModel):
    unique_id:int
    id : str
    P_details:str 
    P_cost :str
    P_name :str


