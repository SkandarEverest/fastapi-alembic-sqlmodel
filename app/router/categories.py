from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select

from app.models.engine import get_db
from app.models.database import Category
from app.schema.category import CategoryRequest

categories_router = APIRouter(tags=["Categories"])


@categories_router.get("/categories", status_code=status.HTTP_200_OK)
def get_categories(db=Depends(get_db)):
    stmt = select(Category)
    return db.exec(stmt).all()


@categories_router.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(body: CategoryRequest, db=Depends(get_db)):
    # simple duplicate check
    exists = db.exec(
        select(Category).where(Category.name == body.name)
    ).first()

    if exists:
        raise HTTPException(status_code=409, detail="Category already exists")

    new_category = Category(name=body.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {
        "message": "Category created successfully",
        "category": new_category
    }