from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database_config import Base


class Sellers_model(Base):
    __tablename__ = "Sellers"
    unique_id = Column(Integer,autoincrement='auto',unique=True)
    id = Column(Integer, primary_key=True,unique=True)
    UserName = Column(String,unique=True)
    Password = Column(String)
    Store_name = Column(String,unique=True)
    #items = relationship("Item", back_populates="owner")