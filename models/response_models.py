from typing import Any, List, Optional
from datetime import datetime, timedelta

from pydantic import BaseModel

from enums import SubscriptionStatusEnum

from .common import BillingInfo, Link, Plan, Amount, Subscriber

class AccessTokenResponse(BaseModel):
    scope: str
    access_token: str
    token_type: str
    app_id: str
    expires_in: int
    nonce: str
    expires_utc: Optional[datetime]

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        self.expires_utc = datetime.utcnow() + timedelta(seconds=self.expires_in)

    def is_expired(self) -> bool:
        return datetime.utcnow() >= self.expires_utc

class ListPlansResponse(BaseModel):
    total_items: Optional[int]
    total_pages: Optional[int]
    plans: List[Plan]

class SubscriptionDetailsResponse(BaseModel):
    id: str
    plan_id: str
    start_time: datetime
    quantity: str
    shipping_amount: Amount
    subscriber: Subscriber
    billing_info: BillingInfo
    create_time: datetime
    update_time: datetime
    links: List[Link]
    status: SubscriptionStatusEnum
    status_update_time: datetime
