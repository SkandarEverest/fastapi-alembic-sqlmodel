import uuid
from datetime import datetime, date
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class Category(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(index=True)

    expenses: List["Expense"] = Relationship(back_populates="category")


class Expense(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)

    amount: int
    description: Optional[str] = None
    spent_at: date
    created_at: datetime = Field(default_factory=datetime.utcnow)

    category_id: uuid.UUID = Field(foreign_key="category.id", index=True)
    category: Optional[Category] = Relationship(back_populates="expenses")