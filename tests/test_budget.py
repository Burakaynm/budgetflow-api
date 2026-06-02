from tests.test_expenses import SAMPLE_EXPENSE, create_expense
from tests.test_incomes import SAMPLE_INCOME, create_income


def test_budget_summary(client):
    create_income(client)
    create_expense(client)

    response = client.get("/budget/summary")

    assert response.status_code == 200
    data = response.json()
    assert data["total_income"] == 45000
    assert data["total_expense"] == 120
    assert data["balance"] == 44880


def test_monthly_budget_summary(client):
    create_income(client, {**SAMPLE_INCOME, "date": "2026-05-15"})
    create_income(
        client,
        {**SAMPLE_INCOME, "title": "Other", "date": "2026-06-01"},
    )
    create_expense(client, {**SAMPLE_EXPENSE, "date": "2026-05-20"})

    response = client.get(
        "/budget/monthly-summary",
        params={"year": 2026, "month": 5},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["year"] == 2026
    assert data["month"] == 5
    assert data["total_income"] == 45000
    assert data["total_expense"] == 120
    assert data["balance"] == 44880


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "BudgetFlow API is running"
