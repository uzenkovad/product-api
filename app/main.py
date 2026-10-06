
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="Product API",
    description="REST API for managing products",
    version="1.0.0"
)


# Product model
class Product(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


# Model for creating and updating products
class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


# In-memory storage
products = {
    1: Product(
        id=1,
        name="Gaming Mouse",
        price=79.99,
        quantity=10
    ),
    2: Product(
        id=2,
        name="Mechanical Keyboard",
        price=129.99,
        quantity=5
    )
}


# GET all products
@app.get("/api/items", response_model=list[Product])
def get_products():
    return list(products.values())


# GET product by ID
@app.get("/api/items/{product_id}", response_model=Product)
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]


# CREATE new product
@app.post(
    "/api/items",
    response_model=Product,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate):

    new_id = max(products.keys(), default=0) + 1

    new_product = Product(
        id=new_id,
        **product.model_dump()
    )

    products[new_id] = new_product

    return new_product


# UPDATE existing product
@app.put("/api/items/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    product: ProductCreate
):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    updated_product = Product(
        id=product_id,
        **product.model_dump()
    )

    products[product_id] = updated_product

    return updated_product


# DELETE product
@app.delete(
    "/api/items/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    del products[product_id]

    return None

# 11