import pytest
import logging

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

def test_show_subscription_details(paypal_config):
    client = PayPalClient(paypal_config)
    response = client.show_subscription_details(config['TestSubscriber']['subscription_id'])

    assert response.subscriber.email_address == config['TestSubscriber']['email']

def test_unsubscribe(paypal_config):
    client = PayPalClient(paypal_config)
    response = client.cancel_subscription(config['TestSubscriber']['subscription_id'], 'testing')

    assert response.status_code == 204

def test_activate(paypal_config):
    client = PayPalClient(paypal_config)
    response = client.activate_subscription(config['TestSubscriber']['subscription_id'], 'testing')

    assert response.status_code == 204
