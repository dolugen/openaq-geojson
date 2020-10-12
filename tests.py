import pytest
from app import app


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_hello(client):
    response = client.get('/echo-args?key=value&foo=bar')
    assert response.status_code
    assert response.data == b'{"key":"value","foo":"bar"}\n'
