# Product API

Product API is a simple REST web service developed for CI/CD laboratory work.

The service provides CRUD operations for managing products.

## Technologies

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- Docker

## API Endpoints

- GET `/api/items` — get all products
- GET `/api/items/{product_id}` — get a product by ID
- POST `/api/items` — create a new product
- PUT `/api/items/{product_id}` — update a product
- DELETE `/api/items/{product_id}` — delete a product

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt