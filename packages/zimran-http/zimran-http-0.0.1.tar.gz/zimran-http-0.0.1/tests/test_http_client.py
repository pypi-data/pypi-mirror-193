from pytest_httpx import HTTPXMock

from zimran.http import HttpClient


def test_request(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(url='http://service:8000/endpoint', status_code=200)

    client = HttpClient(service='service')
    response = client.get('/endpoint')

    assert response.status_code == 200
