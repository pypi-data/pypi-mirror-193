from pytest_httpx import HTTPXMock

from zimran.http import AsyncHttpClient


async def test_request(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(url='http://service:8000/endpoint', status_code=200)

    async with AsyncHttpClient(service='service') as client:
        response = await client.get('/endpoint')

    assert response.status_code == 200
