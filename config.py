BASE_URL = 'https://api-m.sandbox.paypal.com/'

class PayPalConfig:
    def __init__(self, client_id: str, secret: str, base_url: None) -> None:
        self.client_id = client_id
        self.secret = secret
        self.base_url = base_url

        if not self.base_url:
            self.base_url = BASE_URL
