from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.cart import Cart
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderResponse
from app.utils.dependencies import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/checkout", response_model=OrderResponse)
def checkout(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart = db.query(Cart).filter(
        Cart.user_id == current_user.id
    ).first()

    if not cart or not cart.items:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )

    total_amount = 0

    for cart_item in cart.items:
        product = db.query(Product).filter(
            Product.id == cart_item.product_id
        ).first()

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if cart_item.quantity > product.stock:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for product: {product.name}"
            )

        total_amount += product.price * cart_item.quantity

    order = Order(
        user_id=current_user.id,
        total_amount=total_amount,
        status="Pending"
    )

    db.add(order)
    db.flush()

    for cart_item in cart.items:
        product = db.query(Product).filter(
            Product.id == cart_item.product_id
        ).first()

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=cart_item.quantity,
            price=product.price
        )

        product.stock -= cart_item.quantity

        db.add(order_item)

    for cart_item in cart.items:
        db.delete(cart_item)

    db.commit()
    db.refresh(order)

    return order


@router.get("/", response_model=list[OrderResponse])
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    orders = db.query(Order).filter(
        Order.user_id == current_user.id
    ).all()

    return orders


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order