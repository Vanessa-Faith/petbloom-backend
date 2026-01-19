from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ProductResponse, ProductCreate
from app.services.prisma_client import prisma_client

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/categories/list")
async def get_categories_list():
    try:
        products = await prisma_client.product.find_many(select={"category": True})
        categories = list(set([p.category for p in products]))
        return categories
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/brands/list")
async def get_brands_list():
    try:
        products = await prisma_client.product.find_many(select={"brand": True})
        brands = list(set([p.brand for p in products if p.brand]))
        return brands
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("")
async def get_products(skip: int = 0, limit: int = 20, category: str = None, petType: str = None):
    try:
        where_clause = {}
        if category:
            where_clause["category"] = category
        if petType:
            where_clause["petType"] = petType
        
        products = await prisma_client.product.find_many(where=where_clause, skip=skip, take=limit, order={"createdAt": "desc"})
        total = await prisma_client.product.count(where=where_clause)
        
        return {"data": products, "total": total}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    try:
        product = await prisma_client.product.find_unique(where={"id": product_id})
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    try:
        new_product = await prisma_client.product.create(data=product.dict())
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: str, product_update: ProductCreate):
    try:
        updated_product = await prisma_client.product.update(where={"id": product_id}, data=product_update.dict())
        return updated_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    try:
        await prisma_client.product.delete(where={"id": product_id})
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
