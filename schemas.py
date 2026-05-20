from datetime import date
from pydantic import BaseModel


class Expense(BaseModel):
    title: str
    amount: float
    category: str
    date: date


class Income(BaseModel):
    title: str
    amount: float
    source: str
    date: date