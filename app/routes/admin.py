from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.models.product import Product
from app.models.order import Order
from app.utils.dependencies import get_current_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin Dashboard"]
)


@router.get("/dashboard")
def get_admin_dashboard(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    total_users = db.query(User).count()
    total_products = db.query(Product).count()
    total_orders = db.query(Order).count()

    pending_orders = db.query(Order).filter(
        Order.status == "Pending"
    ).count()

    confirmed_orders = db.query(Order).filter(
        Order.status == "Confirmed"
    ).count()

    shipped_orders = db.query(Order).filter(
        Order.status == "Shipped"
    ).count()

    delivered_orders = db.query(Order).filter(
        Order.status == "Delivered"
    ).count()

    cancelled_orders = db.query(Order).filter(
        Order.status == "Cancelled"
    ).count()

    total_revenue = db.query(Order).filter(
        Order.status != "Cancelled"
    ).with_entities(
        func.sum(Order.total_amount)
    ).scalar() or 0

    return {
        "total_users": total_users,
        "total_products": total_products,
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "confirmed_orders": confirmed_orders,
        "shipped_orders": shipped_orders,
        "delivered_orders": delivered_orders,
        "cancelled_orders": cancelled_orders,
        "total_revenue": total_revenue
    }