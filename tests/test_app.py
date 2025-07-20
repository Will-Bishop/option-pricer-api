from fastapi.testclient import TestClient
from app.app import app   

client = TestClient(app)

def test_call_option():
    response = client.post("/price", json={
        "S": 100,
        "K": 90,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "call"
    })
    assert response.status_code == 200
    assert "price" in response.json()


def test_put_option():
    response = client.post("/price", json={
        "S": 100,
        "K": 110,
        "T": 1,
        "r": 0.05,
        "sigma": 0.25,
        "option_type": "put"
    })
    assert response.status_code == 200
    assert "price" in response.json()


def test_invalid_option_type():
    response = client.post("/price", json={
        "S": 100,
        "K": 90,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "banana"
    })
    assert response.status_code == 400
    assert "option_type must be 'call' or 'put'" in response.json()["detail"]


def test_zero_stock_price():
    response = client.post("/price", json={
        "S": 0,  # not realistic
        "K": 100,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "call"
    })
    assert response.status_code == 422


def test_string_instead_of_float():
    response = client.post("/price", json={
        "S": "one hundred",  # invalid
        "K": 90,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "call"
    })
    assert response.status_code == 422


def test_negative_sigma():
    response = client.post("/price", json={
        "S": 100,
        "K": 90,
        "T": 1,
        "r": 0.05,
        "sigma": -0.2,
        "option_type": "call"
    })
    assert response.status_code == 422


def test_missing_strike_price():
    response = client.post("/price", json={
        "S": 100,
        # "K" is missing
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "call"
    })
    assert response.status_code == 422


def test_uppercase_option_type():
    response = client.post("/price", json={
        "S": 100,
        "K": 90,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "option_type": "CALL"
    })
    assert response.status_code == 200
    assert "price" in response.json()