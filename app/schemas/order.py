from pydantic import BaseModel
from typing import Optional
from datetime import date

class OrderBase(BaseModel):
    client_id: int
    tour_id: int
    order_date: date
    status: Optional[str] = "Pending"

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
