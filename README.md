# BudgetFlow API

BudgetFlow API is a simple personal budget tracking backend application developed with Python and FastAPI. The application allows users to manage income and expense records, calculate budget summaries, analyze expenses by category, and export financial data as an Excel report.

## Features

- Add, list, update, and delete expense records
- Add, list, update, and delete income records
- Retrieve a single income or expense record by ID
- Store transaction dates for income and expense records
- Filter income and expense records by date range
- Calculate total income, total expense, and balance
- Generate monthly budget summaries
- Generate category-based expense summaries
- Export incomes, expenses, and budget summary as an Excel file
- Store data persistently using SQLite
- Validate request data using Pydantic
- Support frontend integration with CORS configuration

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

## Installation

Clone the repository:

```bash
git clone https://github.com/Burakaynm/budgetflow-api.git
cd budgetflow-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Running Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the test suite:

```bash
pytest
```

Tests use a separate SQLite database (`test_budgetflow.db`) so your local data is not affected.

## API Endpoints

### Expenses

```text
GET    /expenses
GET    /expenses/{expense_id}
POST   /expenses
PUT    /expenses/{expense_id}
DELETE /expenses/{expense_id}
GET    /expenses/filter?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
GET    /expenses/summary
GET    /expenses/summary/by-category
```

### Incomes

```text
GET    /incomes
GET    /incomes/{income_id}
POST   /incomes
PUT    /incomes/{income_id}
DELETE /incomes/{income_id}
GET    /incomes/filter?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
```

### Budget

```text
GET /budget/summary
GET /budget/monthly-summary?year=YYYY&month=MM
```

### Reports

```text
GET /reports/excel
```

## Example Expense Request

```json
{
  "title": "Coffee",
  "amount": 120,
  "category": "Food",
  "date": "2026-05-20"
}
```

## Example Income Request

```json
{
  "title": "Salary",
  "amount": 45000,
  "source": "Work",
  "date": "2026-05-20"
}
```

## Example Budget Summary Response

```json
{
  "total_income": 45000,
  "total_expense": 120,
  "balance": 44880
}
```

## Purpose of the Project

This project was developed to practice Python backend development with FastAPI. It focuses on REST API design, database operations with SQLAlchemy, data persistence with SQLite, request validation with Pydantic, date-based filtering, monthly financial summaries, Excel report generation with OpenPyXL, and frontend-ready API configuration.
