from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database_config import Base


class Products_model(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    P_details = Column(String, unique=True, index=True)
    P_cost = Column(String)
    P_name = Column(String, default=True)

    #items = relationship("Item", back_populates="owner")