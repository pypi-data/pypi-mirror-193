class HttpClientMixin:
    def __init__(self, service: str, **kwargs):
        super().__init__(base_url=f'http://{service}:8000', **kwargs)
