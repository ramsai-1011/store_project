from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database_config import Base


class Products_model(Base):
    __tablename__ = "users"
    unique_id = Column(Integer,autoincrement='auto',unique=True)
    id = Column(Integer, primary_key=True,unique=True)
    P_details = Column(String,index=True)
    P_cost = Column(String)
    P_name = Column(String, default=True)
    seller_id = Column(Integer,ForeignKey("Sellers.id"),nullable=False)
    seller_details = relationship("Sellers_model",back_populates = "products")
    
    

    #items = relationship("Item", back_populates="owner")