from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import extract

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

@router.get("/budget/monthly-summary")
def get_monthly_budget_summary(
    year: int = Query(...),
    month: int = Query(...),
    db: Session = Depends(get_db)
):
    incomes = (
        db.query(IncomeModel)
        .filter(extract("year", IncomeModel.date) == year)
        .filter(extract("month", IncomeModel.date) == month)
        .all()
    )

    expenses = (
        db.query(ExpenseModel)
        .filter(extract("year", ExpenseModel.date) == year)
        .filter(extract("month", ExpenseModel.date) == month)
        .all()
    )

    total_income = 0
    total_expense = 0

    for income in incomes:
        total_income += income.amount

    for expense in expenses:
        total_expense += expense.amount

    balance = total_income - total_expense

    return {
        "year": year,
        "month": month,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }