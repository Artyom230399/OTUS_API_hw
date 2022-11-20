import pytest
import requests


# Фикстуры для API по собакам
@pytest.fixture
def status_code_all_dogs():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    if response.ok:
        return response.json()
    else:
        print("Error_Status_Code")


@pytest.fixture
def status_code_random_dogs():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    if response.ok:
        return response.json()
    else:
        print("Error_Status_Code")


# Фикстуры для API для JSONPlaceholder
@pytest.fixture
def status_code_JSONPlaceholder():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1/users')
    if response.ok:
        return response
    else:
        print("Error_Status_Code")


def pytest_addoption(parser):
    """Параметры для тестов"""
    parser.addoption('--url',
                     action='store',
                     default='https://ya.ru',
                     help='Передайте url с помощью параметра --url')

    parser.addoption('--status_code',
                     action='store',
                     default='200',
                     help='Передайте status_code с помощью параметра --status_code')


@pytest.fixture
def url_param(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    """Фикстура для перадачи url"""
    return request.config.getoption('--status_code')
