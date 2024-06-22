from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database_config import Base


class Products_model(Base):
    __tablename__ = "users"
    unique_id = Column(Integer, primary_key=True,autoincrement='auto')
    id = Column(Integer, primary_key=True,unique=True)
    P_details = Column(String, unique=True, index=True)
    P_cost = Column(String)
    P_name = Column(String, default=True)

    #items = relationship("Item", back_populates="owner")