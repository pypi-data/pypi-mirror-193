from typing import List, Optional

from pydantic import BaseModel


class SupplierRef(BaseModel):
    id: Optional[str]
    supplierName: Optional[str]


class PurchaseOrderRef(BaseModel):
    id: Optional[str]
    purchaseOrderNumber: Optional[str]


class AccountRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class TaxRateRef(BaseModel):
    id: Optional[str]
    name: Optional[str]
    effectiveTaxRate: Optional[int]


class ItemRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class TrackingCategoryRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class CategoryRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class CustomerRef(BaseModel):
    id: Optional[str]
    companyName: Optional[str]


class ProjectRef(BaseModel):
    id: Optional[str]
    name: Optional[str]


class Tracking(BaseModel):
    categoryRefs: List[CategoryRef]
    customerRef: Optional[CustomerRef]
    projectRef: Optional[ProjectRef]
    isBilledTo: Optional[str]
    isRebilledTo: Optional[str]


class LineItem(BaseModel):
    description: Optional[str]
    unitAmount: Optional[int]
    quantity: Optional[int]
    discountAmount: Optional[int]
    subTotal: Optional[int]
    taxAmount: Optional[int]
    totalAmount: Optional[int]
    discountPercentage: Optional[int]
    accountRef: AccountRef
    taxRateRef: Optional[TaxRateRef]
    itemRef: Optional[ItemRef]
    trackingCategoryRefs: List[TrackingCategoryRef]
    tracking: Optional[Tracking]
    isDirectCost: Optional[bool]


class WithholdingTaxItem(BaseModel):
    name: Optional[str]
    amount: Optional[int]


class Payment(BaseModel):
    id: Optional[str]
    note: Optional[str]
    reference: Optional[str]
    accountRef: AccountRef
    currency: Optional[str]
    currencyRate: Optional[int]
    paidOnDate: Optional[str]
    totalAmount: Optional[int]


class Allocation(BaseModel):
    currency: Optional[str]
    currencyRate: Optional[int]
    allocatedOnDate: Optional[str]
    totalAmount: Optional[int]


class PaymentAllocation(BaseModel):
    payment: Payment
    allocation: Allocation


class Metadata(BaseModel):
    isDeleted: Optional[bool]


class Bill(BaseModel):
    id: Optional[str]
    reference: Optional[str]
    supplierRef: SupplierRef
    purchaseOrderRefs: List[PurchaseOrderRef]
    issueDate: Optional[str]
    dueDate: Optional[str]
    currency: Optional[str]
    currencyRate: Optional[int]
    lineItems: List[LineItem]
    withholdingTax: List[WithholdingTaxItem]
    status: Optional[str]
    subTotal: Optional[int]
    taxAmount: Optional[int]
    totalAmount: Optional[int]
    amountDue: Optional[int]
    modifiedDate: Optional[str]
    sourceModifiedDate: Optional[str]
    note: Optional[str]
    paymentAllocations: List[PaymentAllocation]
    metadata: Metadata
