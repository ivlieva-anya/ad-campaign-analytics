from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get(path="/")
async def get_products():
    return {"message": "Hello World"}