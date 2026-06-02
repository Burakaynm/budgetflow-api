SAMPLE_INCOME = {
    "title": "Salary",
    "amount": 45000,
    "source": "Work",
    "date": "2026-05-20",
}


def create_income(client, payload=None):
    body = payload or SAMPLE_INCOME
    response = client.post("/incomes", json=body)
    assert response.status_code == 200
    return response.json()["income"]


def test_create_and_list_incomes(client):
    create_income(client)

    response = client.get("/incomes")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Salary"


def test_get_income_by_id(client):
    created = create_income(client)

    response = client.get(f"/incomes/{created['id']}")

    assert response.status_code == 200
    assert response.json()["amount"] == 45000


def test_get_income_not_found(client):
    response = client.get("/incomes/999")

    assert response.status_code == 404


def test_update_income(client):
    created = create_income(client)

    response = client.put(
        f"/incomes/{created['id']}",
        json={
            "title": "Bonus",
            "amount": 5000,
            "source": "Work",
            "date": "2026-05-25",
        },
    )

    assert response.status_code == 200
    assert response.json()["income"]["title"] == "Bonus"


def test_delete_income(client):
    created = create_income(client)

    client.delete(f"/incomes/{created['id']}")

    response = client.get("/incomes")
    assert response.json() == []


def test_filter_incomes_by_date(client):
    create_income(client, {**SAMPLE_INCOME, "date": "2026-05-10"})
    create_income(
        client,
        {**SAMPLE_INCOME, "title": "Freelance", "date": "2026-07-01"},
    )

    response = client.get(
        "/incomes/filter",
        params={"start_date": "2026-05-01", "end_date": "2026-05-31"},
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
