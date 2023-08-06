import datetime
from typing import List, Optional

from pydantic import BaseModel

from pycompanydata.data_types.pagination import PaginatedResponse


class BankAccountRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class RecordRef(BaseModel):
    id: str
    dataType: Optional[str]


class Line(BaseModel):
    description: Optional[str]
    recordRef: Optional[RecordRef]
    amount: int


class Metadata(BaseModel):
    isDeleted: bool


class AccountTransaction(BaseModel):
    id: Optional[str]
    transactionId: Optional[str]
    note: Optional[str]
    bankAccountRef: BankAccountRef
    date: datetime.datetime
    status: str
    currency: Optional[str]
    currencyRate: Optional[int]
    lines: Optional[List[Line]]
    totalAmount: int
    modifiedDate: Optional[datetime.datetime]
    sourceModifiedDate: Optional[datetime.datetime]
    metadata: Optional[Metadata]


class AccountTransactionsPaginatedResponse(PaginatedResponse):
    results: List[AccountTransaction] = []
