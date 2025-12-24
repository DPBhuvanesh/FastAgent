from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List


from game.schema import GameCreate, GameResponse
from game.service import get_sale, get_sales, create_sale as create_sale_service
from core.database import get_db

router = APIRouter(
    prefix="/sales",
    tags=["sales"]
)



@router.post("/", response_model=GameResponse, status_code=status.HTTP_201_CREATED)
def create_new_sale(sale: GameCreate, db: Session = Depends(get_db)):
    return create_sale_service(db=db, sale=sale)


@router.get("/", response_model=List[GameResponse])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = get_sales(db, skip=skip, limit=limit)
    return sales


@router.get("/{sale_id}", response_model=GameResponse)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = get_sale(db, sale_id=sale_id)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale