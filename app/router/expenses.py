from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import select

from app.models.engine import get_db
from app.models.database import Expense, Category
from app.schema.expense import ExpenseRequest

expenses_router = APIRouter(tags=["Expenses"])


@expenses_router.get("/expenses", status_code=status.HTTP_200_OK)
def get_expenses(
    db=Depends(get_db),
    month: str | None = Query(default=None, description="Format YYYY-MM"),
    category_id: str | None = Query(default=None),
):
    stmt = select(Expense)

    if category_id:
        stmt = stmt.where(Expense.category_id == category_id)

    if month:
        # parse YYYY-MM → date range [start, end)
        try:
            y_str, m_str = month.split("-")
            y = int(y_str)
            m = int(m_str)
            if m < 1 or m > 12:
                raise ValueError("invalid month")
        except Exception:
            raise HTTPException(status_code=400, detail="month must be in YYYY-MM format")

        start = date(y, m, 1)
        end = date(y + 1, 1, 1) if m == 12 else date(y, m + 1, 1)

        stmt = stmt.where(Expense.spent_at >= start).where(Expense.spent_at < end)

    stmt = stmt.order_by(Expense.spent_at.desc())
    return db.exec(stmt).all()


@expenses_router.post("/expenses", status_code=status.HTTP_201_CREATED)
def create_expense(body: ExpenseRequest, db=Depends(get_db)):
    # ensure category exists
    category = db.get(Category, body.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    new_expense = Expense(
        amount=body.amount,
        description=body.description,
        spent_at=body.spent_at,
        category_id=body.category_id,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {"message": "Expense created successfully", "expense": new_expense}