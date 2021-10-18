from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .common import Amount, Subscriber

class CreateSubscriptionRequest(BaseModel):
    plan_id: str
    start_time: Optional[datetime]
    quantity: Optional[str]
    shipping_amount: Optional[Amount]
    subscriber: Optional[Subscriber]
