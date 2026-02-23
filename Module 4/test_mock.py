import pytest  
import requests
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}
    return mock

# Erro 1: Adicionado o nome 'test_api_call_1'
def test_api_call_1(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}

# Erro 2: Limpeza da linha e identação correta
def test_api_call_with_mock2(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message": "Success"}