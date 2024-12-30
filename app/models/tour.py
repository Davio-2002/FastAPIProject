from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Tour(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    orders = relationship("Order", back_populates="tour")
