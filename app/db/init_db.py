from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.client import Client

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if not db.query(Client).first():
        test_client = Client(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="john.doe@example.com"
        )
        db.add(test_client)
        db.commit()
    db.close()
