from app.database.database import Base, engine
from app.models.user import User
from app.models.product import Product

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")