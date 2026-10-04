import pytest
from fastapi.testclient import TestClient

from app.main import app, products, Product


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_products():

    products.clear()

    products[1] = Product(
        id=1,
        name="Gaming Mouse",
        price=79.99,
        quantity=10
    )

    products[2] = Product(
        id=2,
        name="Mechanical Keyboard",
        price=129.99,
        quantity=5
    )

    yield


# Test GET all products
def test_get_products():

    response = client.get("/api/items")

    assert response.status_code == 200
    assert len(response.json()) == 2


# Test GET product by ID
def test_get_product():

    response = client.get("/api/items/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Gaming Mouse"


# Test GET nonexistent product
def test_get_product_not_found():

    response = client.get("/api/items/999")

    assert response.status_code == 404


# Test CREATE product
def test_create_product():

    new_product = {
        "name": "Gaming Headset",
        "price": 99.99,
        "quantity": 15
    }

    response = client.post(
        "/api/items",
        json=new_product
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Gaming Headset"
    assert response.json()["id"] == 3


# Test UPDATE product
def test_update_product():

    updated_product = {
        "name": "Wireless Mouse",
        "price": 89.99,
        "quantity": 7
    }

    response = client.put(
        "/api/items/1",
        json=updated_product
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Wireless Mouse"
    assert response.json()["price"] == 89.99


# Test DELETE product
def test_delete_product():

    response = client.delete("/api/items/1")

    assert response.status_code == 204

    response = client.get("/api/items/1")

    assert response.status_code == 404


# Test invalid product data
def test_invalid_product():

    invalid_product = {
        "name": "Invalid Product",
        "price": -10,
        "quantity": 5
    }

    response = client.post(
        "/api/items",
        json=invalid_product
    )

    assert response.status_code == 422


# Test OpenAPI specification
def test_openapi():

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "Product API"
