from fastapi import FastAPI

from database import engine
from models import Base

from routes.expenses import router as expenses_router
from routes.incomes import router as incomes_router
from routes.budget import router as budget_router
from routes.reports import router as reports_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(expenses_router)
app.include_router(incomes_router)
app.include_router(budget_router)
app.include_router(reports_router)

@app.get("/")
def read_root():
    return {"message": "BudgetFlow API is running"}