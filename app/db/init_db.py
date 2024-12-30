from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.client import Client
from app.models.tour import Tour
from app.models.order import Order
from datetime import date

def init_db():
    Base.metadata.create_all(bind=engine)

def populate_data():
    db = SessionLocal()

    if db.query(Client).count() == 0:
        clients = [
            Client(first_name="John", last_name="Doe", phone="1234567890", email="john.doe@example.com"),
            Client(first_name="Jane", last_name="Smith", phone="9876543210", email="jane.smith@example.com"),
        ]
        db.add_all(clients)

    if db.query(Tour).count() == 0:
        tours = [
            Tour(title="Beach Paradise", description="A relaxing beach vacation", price=500.0,
                 start_date=date(2024, 6, 1), end_date=date(2024, 6, 7)),
            Tour(title="Mountain Adventure", description="A thrilling hike through the mountains", price=800.0,
                 start_date=date(2024, 7, 1), end_date=date(2024, 7, 10)),
        ]
        db.add_all(tours)

    if db.query(Order).count() == 0:
        orders = [
            Order(client_id=1, tour_id=1, order_date=date(2024, 5, 15), status="Paid"),
            Order(client_id=2, tour_id=2, order_date=date(2024, 5, 16), status="Pending"),
        ]
        db.add_all(orders)

    db.commit()
    print("Database populated successfully!")
    db.close()
