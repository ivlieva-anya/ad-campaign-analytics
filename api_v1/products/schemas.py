from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):

    name:str
    description:str
    price:str

class ProductCreate (ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductUpdatePartial(ProductBase):
    name: str | None = None
    description: str | None = None
    price: str | None = None

class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id:int