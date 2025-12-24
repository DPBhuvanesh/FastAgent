from pydantic import BaseModel, Field
from typing import Optional


class GameBase(BaseModel):
    
    name: str = Field(..., max_length=255, example="Wii Sports")
    
    rank: Optional[int] = Field(None, example=1)
    platform: Optional[str] = Field(None, max_length=50, example="Wii")
    year: Optional[int] = Field(None, example=2006)
    genre: Optional[str] = Field(None, max_length=50, example="Sports")
    publisher: Optional[str] = Field(None, max_length=100, example="Nintendo")
    
    # Numeric(5,2) is typically handled as float in Pydantic
    na_sales: Optional[float] = Field(None, example=41.49)
    eu_sales: Optional[float] = Field(None, example=29.02)
    jp_sales: Optional[float] = Field(None, example=3.77)
    other_sales: Optional[float] = Field(None, example=8.46)
    global_sales: Optional[float] = Field(None, example=82.74)
    
    description: Optional[str] = Field(None, example="A sports game for the Wii.")


class GameCreate(GameBase):
    pass


class GameResponse(GameBase):
    id: int

    class Config:
        
        from_attributes = True