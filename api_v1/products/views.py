from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.model import db_helper
from . import crud
from .dependencies import get_product_by_id
from .schemas import ProductCreate, Product, ProductUpdate

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)

@router.get("/{product_id}/", response_model=Product)
async def get_product(
        product: Product = Depends(get_product_by_id),
):
    return product

@router.put("/{product_id}/", response_model=Product)
async def update_product(
        product_update:ProductUpdate,
        session: AsyncSession = Depends(db_helper.session_dependency),
        product: Product =  Depends(get_product_by_id),
):
    return await crud.update_product(
        session=session,
        product_update=product_update,
        product=product,
    )

@router.patch("/{product_id}/", response_model=Product)
async def update_product_partial(
        product_update:ProductUpdate,
        session: AsyncSession = Depends(db_helper.session_dependency),
        product: Product =  Depends(get_product_by_id),
):
    return await crud.update_product(
        session=session,
        product_update=product_update,
        product=product,
        partial=True
    )