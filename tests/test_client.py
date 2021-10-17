import pytest

from paypal_python.config import PayPalConfig
from paypal_python.client import PayPalClient

from .config import config

@pytest.fixture
def paypal_config():
    return PayPalConfig(config['client_id'], config['secret'], config['base_url'])

def test_get_access_token(paypal_config):
    client = PayPalClient(paypal_config)
    client.request_access_token()

    assert not client.access_token.is_expired()

def test_list_plans(paypal_config):
    client = PayPalClient(paypal_config)
    response = client.list_plans(config['product_id'])

    assert response.plans[0].id == config['plan_id']