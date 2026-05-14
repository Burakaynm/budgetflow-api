from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import ExpenseModel
from schemas import Expense

router = APIRouter()


@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseModel).all()
    return expenses


@router.post("/expenses")
def create_expense(expense: Expense, db: Session = Depends(get_db)):
    new_expense = ExpenseModel(
        title=expense.title,
        amount=expense.amount,
        category=expense.category
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {
        "message": "Expense created successfully",
        "expense": new_expense
    }


@router.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: Expense,
    db: Session = Depends(get_db)
):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()
    db.refresh(expense)

    return {
        "message": "Expense updated successfully",
        "expense": expense
    }


@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()

    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}


@router.get("/expenses/summary")
def get_expense_summary(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseModel).all()

    total_amount = 0

    for expense in expenses:
        total_amount += expense.amount

    return {
        "total_expense": total_amount,
        "expense_count": len(expenses)
    }


@router.get("/expenses/summary/by-category")
def get_expense_summary_by_category(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseModel).all()

    category_summary = {}

    for expense in expenses:
        category = expense.category
        amount = expense.amount

        if category in category_summary:
            category_summary[category] += amount
        else:
            category_summary[category] = amount

    return category_summary