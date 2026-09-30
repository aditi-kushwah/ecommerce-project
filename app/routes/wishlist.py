from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.wishlist import Wishlist
from app.models.product import Product
from app.models.user import User
from app.schemas.wishlist import WishlistCreate, WishlistResponse
from app.utils.dependencies import get_current_user


router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)


@router.post("/", response_model=WishlistResponse)
def add_to_wishlist(
    wishlist_data: WishlistCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(
        Product.id == wishlist_data.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    existing_item = db.query(Wishlist).filter(
        Wishlist.user_id == current_user.id,
        Wishlist.product_id == wishlist_data.product_id
    ).first()

    if existing_item:
        raise HTTPException(
            status_code=400,
            detail="Product already in wishlist"
        )

    wishlist_item = Wishlist(
        user_id=current_user.id,
        product_id=wishlist_data.product_id
    )

    db.add(wishlist_item)
    db.commit()
    db.refresh(wishlist_item)

    return wishlist_item


@router.get("/", response_model=list[WishlistResponse])
def get_wishlist(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    wishlist = db.query(Wishlist).filter(
        Wishlist.user_id == current_user.id
    ).all()

    return wishlist


@router.delete("/{product_id}")
def remove_from_wishlist(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    wishlist_item = db.query(Wishlist).filter(
        Wishlist.product_id == product_id,
        Wishlist.user_id == current_user.id
    ).first()

    if not wishlist_item:
        raise HTTPException(
            status_code=404,
            detail="Product not found in wishlist"
        )

    db.delete(wishlist_item)
    db.commit()

    return {
        "message": "Product removed from wishlist successfully"
    }