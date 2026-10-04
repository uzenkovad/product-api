# Product API

Product API is a simple REST web service developed for CI/CD laboratory work.

The service provides CRUD operations for managing products.

## Technologies

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- Docker

## API Endpoints

| Method | Endpoint                  | Description          |
|--------|---------------------------|----------------------|
| GET    | `/api/items`              | Get all products     |
| GET    | `/api/items/{product_id}` | Get a product by ID  |
| POST   | `/api/items`              | Create a new product |
| PUT    | `/api/items/{product_id}` | Update a product     |
| DELETE | `/api/items/{product_id}` | Delete a product     |

## Run locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI specification:

```
http://127.0.0.1:8000/openapi.json
```

## Run tests

Run unit tests with:

```bash
python -m pytest tests/ -v
```

## Docker

Build the Docker image:

```bash
docker build -t product-api:latest .
```

Run the Docker container:

```bash
docker run -d --name product-api-container -p 8000:8000 product-api:latest
```

Check running containers:

```bash
docker ps
```

After starting the container, Swagger UI will be available at:

```
http://localhost:8000/docs
```

Stop the container:

```bash
docker stop product-api-container
```

Start the container again:

```bash
docker start product-api-container
```

Remove the container if necessary:

```bash
docker rm -f product-api-container
```