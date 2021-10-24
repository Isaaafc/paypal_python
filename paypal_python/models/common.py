from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel

class CustomerName(BaseModel):
    given_name: Optional[str]
    surname: Optional[str]
    full_name: Optional[str]

class Address(BaseModel):
    address_line_1: Optional[str]
    address_line_2: Optional[str]
    admin_area_1: Optional[str]
    admin_area_2: Optional[str]
    postal_code: Optional[str]
    country_code: Optional[str]

class ShippingAddress(BaseModel):
    name: Optional[CustomerName]
    address: Optional[Address]

class Subscriber(BaseModel):
    name: CustomerName
    email_address: str
    shipping_address: Optional[ShippingAddress]

class Amount(BaseModel):
    currency_code: str
    value: str

class PaymentMethod(BaseModel):
    payer_selected: str
    payee_preferred: str

class ApplicationContext(BaseModel):
    brand_name: str
    locale: Optional[str]
    shipping_preference: Optional[str]
    payment_method: Optional[PaymentMethod]
    return_url: Optional[str]
    cancel_url: Optional[str]

class Link(BaseModel):
    href: str
    rel: str
    method: str

class Plan(BaseModel):
    id: str
    status: str
    name: str
    usage_type: str
    create_time: datetime
    links: List[Link]

class CycleExecution(BaseModel):
    tenure_type: str
    sequence: int
    cycles_completed: int
    cycles_remaining: int
    total_cycles: int

class Payment(BaseModel):
    amount: Amount
    time: datetime

class BillingInfo(BaseModel):
    outstanding_balance: Amount
    cycle_executions: List[CycleExecution]
    last_payment: Optional[Payment]
    next_billing_time: datetime
    failed_payments_count: int
