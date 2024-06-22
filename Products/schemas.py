from pydantic import BaseModel

class Products_schema(BaseModel):
    id : str
    P_details:str 
    P_cost :str
    P_name :str