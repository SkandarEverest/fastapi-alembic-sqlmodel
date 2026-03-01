from datetime import date
import uuid
from pydantic import BaseModel


class ExpenseRequest(BaseModel):
    amount: int
    description: str | None = None
    spent_at: date
    category_id: uuid.UUID


class ExpenseResponse(BaseModel):
    id: str
    amount: int
    description: str | None = None
    spent_at: date
    category_id: str