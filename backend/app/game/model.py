from sqlalchemy import Column, Integer, String, Numeric, Text
from core.database import Base

class Sale(Base):
    __tablename__ = "sales"

    
    id = Column(Integer, primary_key=True, index=True) 
    rank = Column(Integer)                             
    name = Column(String(255))                         
    platform = Column(String(50))                      
    year = Column(Integer)                             
    genre = Column(String(50))                         
    publisher = Column(String(100))                    
    
    
    na_sales = Column(Numeric(5, 2))
    eu_sales = Column(Numeric(5, 2))
    jp_sales = Column(Numeric(5, 2))
    other_sales = Column(Numeric(5, 2))
    global_sales = Column(Numeric(5, 2))
    
    description = Column(Text)