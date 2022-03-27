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
    availability: str  # InStock, OutOfStock
    image: str
    price_valid_until: str = Field(..., alias="priceValidUntil")
    gtin: str

    @property
    def price_per_gram(self) -> float:
        s: list[str] = self.sku.split("-")
        grams = float(s[-1])
        return self.price / grams


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
