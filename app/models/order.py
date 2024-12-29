from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    tour_id = Column(Integer, ForeignKey("tour.id"), nullable=False)
    order_date = Column(Date, nullable=False)
    status = Column(String, default="Pending")

    client = relationship("Client", back_populates="orders")
    tour = relationship("Tour", back_populates="orders")
