from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.db.session import SessionLocal
from app.models.order import Order
from app.schemas.order import Order as OrderSchema, OrderCreate, OrderUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[OrderSchema])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(**order.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.put("/{order_id}", response_model=OrderSchema)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    existing_order = db.query(Order).filter(Order.id == order_id).first()
    if existing_order:
        for key, value in order.dict().items():
            setattr(existing_order, key, value)
        db.commit()
        db.refresh(existing_order)
        return existing_order
    return {"error": "Order not found"}

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db.query(Order).filter(Order.id == order_id).delete()
    db.commit()
    return {"message": "Order deleted successfully"}

@router.put("/{order_id}/update-status")
def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id, Order.status != "Paid").first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found or already paid")
    order.status = status
    db.commit()
    return {"message": f"Order {order_id} updated to {status}"}

# GROUP BY
@router.get("/group-by-status", response_model=dict)
def group_orders_by_status(db: Session = Depends(get_db)):
    grouped = db.query(Order.status, func.count(Order.id)).group_by(Order.status).all()
    return {status: count for status, count in grouped}
