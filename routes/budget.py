from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import ExpenseModel, IncomeModel

router = APIRouter()


@router.get("/budget/summary")
def get_budget_summary(db: Session = Depends(get_db)):
    incomes = db.query(IncomeModel).all()
    expenses = db.query(ExpenseModel).all()

    total_income = 0
    total_expense = 0

    for income in incomes:
        total_income += income.amount

    for expense in expenses:
        total_expense += expense.amount

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }