from httpx import AsyncClient

from ._base import HttpClientMixin


class AsyncHttpClient(HttpClientMixin, AsyncClient):
    pass
