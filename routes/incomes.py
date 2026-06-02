from datetime import date
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from database import get_db
from models import IncomeModel
from schemas import Income

router = APIRouter()


@router.get("/incomes")
def get_incomes(db: Session = Depends(get_db)):
    incomes = (
        db.query(IncomeModel)
        .order_by(IncomeModel.date.desc(), IncomeModel.id.desc())
        .all()
    )
    return incomes

@router.get("/incomes/filter")
def filter_incomes_by_date(
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db)
):
    incomes = (
        db.query(IncomeModel)
        .filter(IncomeModel.date >= start_date)
        .filter(IncomeModel.date <= end_date)
        .order_by(IncomeModel.date.desc(), IncomeModel.id.desc())
        .all()
    )

    return incomes

@router.get("/incomes/{income_id}")
def get_income_by_id(income_id: int, db: Session = Depends(get_db)):
    income = db.query(IncomeModel).filter(IncomeModel.id == income_id).first()

    if income is None:
        raise HTTPException(status_code=404, detail="Income not found")

    return income

@router.post("/incomes")
def create_income(income: Income, db: Session = Depends(get_db)):
    new_income = IncomeModel(
        title=income.title,
        amount=income.amount,
        source=income.source,
        date=income.date
    )

    db.add(new_income)
    db.commit()
    db.refresh(new_income)

    return {
        "message": "Income created successfully",
        "income": new_income
    }

@router.put("/incomes/{income_id}")
def update_income(
    income_id: int,
    updated_income: Income,
    db: Session = Depends(get_db)
):
    income = db.query(IncomeModel).filter(IncomeModel.id == income_id).first()

    if income is None:
        raise HTTPException(status_code=404, detail="Income not found")

    income.title = updated_income.title
    income.amount = updated_income.amount
    income.source = updated_income.source
    income.date = updated_income.date

    db.commit()
    db.refresh(income)

    return {
        "message": "Income updated successfully",
        "income": income
    }


@router.delete("/incomes/{income_id}")
def delete_income(income_id: int, db: Session = Depends(get_db)):
    income = db.query(IncomeModel).filter(IncomeModel.id == income_id).first()

    if income is None:
        raise HTTPException(status_code=404, detail="Income not found")

    db.delete(income)
    db.commit()

    return {"message": "Income deleted successfully"}