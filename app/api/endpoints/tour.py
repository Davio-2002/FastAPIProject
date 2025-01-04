from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tour import Tour
from app.schemas.tour import Tour as TourSchema, TourCreate, TourUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TourSchema])
def get_tours(db: Session = Depends(get_db)):
    return db.query(Tour).all()

@router.post("/", response_model=TourSchema)
def create_tour(tour: TourCreate, db: Session = Depends(get_db)):
    new_tour = Tour(**tour.dict())
    db.add(new_tour)
    db.commit()
    db.refresh(new_tour)
    return new_tour

@router.put("/{tour_id}", response_model=TourSchema)
def update_tour(tour_id: int, tour: TourUpdate, db: Session = Depends(get_db)):
    existing_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if existing_tour:
        for key, value in tour.dict().items():
            setattr(existing_tour, key, value)
        db.commit()
        db.refresh(existing_tour)
        return existing_tour
    return {"error": "Tour not found"}

@router.delete("/{tour_id}")
def delete_tour(tour_id: int, db: Session = Depends(get_db)):
    db.query(Tour).filter(Tour.id == tour_id).delete()
    db.commit()
    return {"message": "Tour deleted successfully"}

@router.get("/filter", response_model=list[TourSchema])
def filter_tours(
    min_price: float = Query(0),
    max_price: float = Query(10000),
    db: Session = Depends(get_db)
):
    return db.query(Tour).filter(Tour.price >= min_price, Tour.price <= max_price).all()

@router.get("/sorted", response_model=list[TourSchema])
def get_sorted_tours(sort_by: str = "price", ascending: bool = True, db: Session = Depends(get_db)):
    order = getattr(Tour, sort_by).asc() if ascending else getattr(Tour, sort_by).desc()
    return db.query(Tour).order_by(order).all()
