from httpx import Client

from ._base import HttpClientMixin


class HttpClient(HttpClientMixin, Client):
    pass
