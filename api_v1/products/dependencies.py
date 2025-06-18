from typing import Annotated

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api_v1.products import crud
from core.model import db_helper, Product


async def get_product_by_id(
        product_id: Annotated[int,Path],
        session: AsyncSession = Depends(db_helper.session_dependency)
)->Product:
    prod = await crud.get_product(
        session=session,
        product_id=product_id,
    )
    if prod is not None:
        return prod
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Product {product_id} not found"
        )