from pydantic import BaseModel
from typing import Optional
from datetime import date

class TourBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    start_date: date
    end_date: date

class TourCreate(TourBase):
    pass

class TourUpdate(TourBase):
    pass

class Tour(TourBase):
    id: int

    class Config:
        orm_mode = True
