from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
