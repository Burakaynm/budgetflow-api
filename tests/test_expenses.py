SAMPLE_EXPENSE = {
    "title": "Coffee",
    "amount": 120,
    "category": "Food",
    "date": "2026-05-20",
}


def create_expense(client, payload=None):
    body = payload or SAMPLE_EXPENSE
    response = client.post("/expenses", json=body)
    assert response.status_code == 200
    return response.json()["expense"]


def test_create_and_list_expenses(client):
    create_expense(client)

    response = client.get("/expenses")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Coffee"
    assert data[0]["amount"] == 120


def test_get_expense_by_id(client):
    created = create_expense(client)

    response = client.get(f"/expenses/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Coffee"


def test_get_expense_not_found(client):
    response = client.get("/expenses/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found"


def test_update_expense(client):
    created = create_expense(client)

    response = client.put(
        f"/expenses/{created['id']}",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-05-21",
        },
    )

    assert response.status_code == 200
    assert response.json()["expense"]["title"] == "Lunch"
    assert response.json()["expense"]["amount"] == 250


def test_delete_expense(client):
    created = create_expense(client)

    delete_response = client.delete(f"/expenses/{created['id']}")
    assert delete_response.status_code == 200

    list_response = client.get("/expenses")
    assert list_response.json() == []


def test_filter_expenses_by_date(client):
    create_expense(client, {**SAMPLE_EXPENSE, "date": "2026-05-10"})
    create_expense(
        client,
        {**SAMPLE_EXPENSE, "title": "Bus", "date": "2026-06-01"},
    )

    response = client.get(
        "/expenses/filter",
        params={"start_date": "2026-05-01", "end_date": "2026-05-31"},
    )

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_expense_summary(client):
    create_expense(client)
    create_expense(
        client,
        {**SAMPLE_EXPENSE, "title": "Taxi", "amount": 80, "category": "Transport"},
    )

    response = client.get("/expenses/summary")

    assert response.status_code == 200
    assert response.json()["total_expense"] == 200
    assert response.json()["expense_count"] == 2


def test_expense_summary_by_category(client):
    create_expense(client)
    create_expense(
        client,
        {**SAMPLE_EXPENSE, "title": "Taxi", "amount": 80, "category": "Transport"},
    )

    response = client.get("/expenses/summary/by-category")

    assert response.status_code == 200
    assert response.json() == {"Food": 120, "Transport": 80}


def test_create_expense_rejects_invalid_amount(client):
    response = client.post(
        "/expenses",
        json={**SAMPLE_EXPENSE, "amount": 0},
    )

    assert response.status_code == 422
