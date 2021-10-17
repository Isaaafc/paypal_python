from typing import Dict
from urllib.parse import urljoin, urlencode

from requests.auth import HTTPBasicAuth
import requests

from .config import PayPalConfig
from .models.response_models import AccessTokenResponse, ListPlansResponse, SubscriptionDetailsResponse

class PayPalClient:
    def __init__(self, config: PayPalConfig) -> None:
        self.config = config
        self.access_token = None

    def __get_authorization(self) -> str:
        if not self.access_token or self.access_token.is_expired():
            self.request_access_token()

        return f'{self.access_token.token_type} {self.access_token.access_token}'

    def __get_json_headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'Authorization': self.__get_authorization()
        }

    def request_access_token(self) -> None:
        url = urljoin(self.config.base_url, 'v1/oauth2/token')

        headers = {
            'Accept-Language': 'en_US',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, headers=headers, auth=HTTPBasicAuth(self.config.client_id, self.config.secret), data=body)

        self.access_token = AccessTokenResponse.parse_obj(response.json())

    def list_plans(self, product_id: str) -> ListPlansResponse:
        url = urljoin(self.config.base_url, 'v1/billing/plans')

        headers = self.__get_json_headers()

        query = {
            'product_id': product_id
        }

        url = f'{url}?{urlencode(query)}'

        response = requests.get(url, headers=headers)

        return ListPlansResponse.parse_obj(response.json())

    def show_subscription_details(self, subscription_id: str):
        url = urljoin(self.config.base_url, f'/v1/billing/subscriptions/{subscription_id}')
        headers = self.__get_json_headers()

        response = requests.get(url, headers=headers)

        return SubscriptionDetailsResponse.parse_obj(response.json())
