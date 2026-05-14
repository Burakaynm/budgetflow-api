# BudgetFlow API

BudgetFlow API is a simple personal budget tracking backend application developed with Python and FastAPI. The application allows users to manage income and expense records, calculate budget summaries, analyze expenses by category, and export financial data as an Excel report.

## Features

- Add, list, update, and delete expense records
- Add, list, update, and delete income records
- Calculate total income, total expense, and balance
- Generate category-based expense summaries
- Export incomes, expenses, and budget summary as an Excel file
- Store data persistently using SQLite

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- OpenPyXL
- Uvicorn

## Project Structure

```text
budgetflow-api/
│
├── routes/
│   ├── budget.py
│   ├── expenses.py
│   ├── incomes.py
│   └── reports.py
│
├── database.py
├── main.py
├── models.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── README.md
```
