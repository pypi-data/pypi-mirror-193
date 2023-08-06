from typing import Optional

from pydantic import BaseModel


class AccountRef(BaseModel):
    id: str
    name: Optional[str]


class CategoryRef(BaseModel):
    id: str
    name: Optional[str]


class CustomerRef(BaseModel):
    id: str
    companyName: Optional[str]


class ItemRef(BaseModel):
    id: str
    name: Optional[str]


class ProjectRef(BaseModel):
    id: str
    name: Optional[str]


class SalesOrderRef(BaseModel):
    id: str
    dataType: Optional[str]


class TaxRateRef(BaseModel):
    id: str
    name: Optional[str]
    effectiveTaxRate: Optional[float]


class TrackingCategoryRef(BaseModel):
    id: str
    name: Optional[str]
