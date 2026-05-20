from datetime import date
from pydantic import BaseModel, Field


class Expense(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    date: date


class Income(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    source: str = Field(..., min_length=1, max_length=50)
    date: date