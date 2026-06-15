from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# earlier product class was for pydentic i.e. for data validation.

# this product clas is for database

class Product(Base) :

  __tablename__ = "product"

  id = Column(Integer,primary_key=True,index=True)
  name = Column(String)
  description = Column(String)
  price = Column(Float)
  quantity = Column(Integer)