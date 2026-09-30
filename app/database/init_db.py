from app.database.database import Base, engine
from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart, CartItem
from app.models.order import Order, OrderItem
from app.models.wishlist import Wishlist

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")