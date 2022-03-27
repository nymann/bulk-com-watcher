from pydantic import BaseModel
from pydantic import Field


class Offer(BaseModel):
    class Config:
        allow_population_by_field_name = True

    _type: str = Field(..., alias="@type")
    price: float
    price_currency: str = Field(..., alias="priceCurrency")
    url: str
    sku: str
    availability: str
    image: str
    price_valid_until: str = Field(..., alias="priceValidUntil")
    gtin: str


class Model(BaseModel):
    class Config:
        allow_population_by_field_name = True

    _context: str = Field(..., alias="@context")
    type: str
    sku: str
    name: str
    image: str
    description: str
    gtin: str
    _id: str = Field(..., alias="@id")
    offers: list[Offer]
