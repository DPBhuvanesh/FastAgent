from sqlalchemy.orm import Session
from game import model
from game import schema

def get_sale(db: Session, sale_id: int):
    
    return db.query(model.Sale).filter(model.Sale.id == sale_id).first()

def get_sales(db: Session, skip: int = 0, limit: int = 100):
    
    return db.query(model.Sale).offset(skip).limit(limit).all()

def create_sale(db: Session, sale: schema.GameCreate):
    
    db_sale = model.Sale(**sale.model_dump())
    
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale) 
    return db_sale