import pytest
import configparser
from pathlib import Path
from dog_api.dog_api import DogApi
from openbrewerydb_api.openbrewerydb_api import OpenBreweryDbApi
from json_placeholder_api.json_placeholder_api import JsonPlaceholderApi


@pytest.fixture(scope="session")
def cfg():
    config = configparser.ConfigParser()
    config.read(Path(__file__).parent / 'api_config.ini')
    return config


@pytest.fixture(scope="class")
def dog_api_obj(cfg):
    api = DogApi(cfg["dog_api"]["hostname"])
    return api


@pytest.fixture(scope="class")
def open_brewery_db_obj(cfg):
    api = OpenBreweryDbApi(cfg["open_brewery_db"]["hostname"])
    return api


@pytest.fixture(scope="class")
def json_placeholder_obj(cfg):
    api = JsonPlaceholderApi(cfg["json_placeholder"]["hostname"])
    return api


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://ya.ru/',
                     required=False)

    parser.addoption('--status_code',
                     default="200",
                     required=False)


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def my_status_code(request):
    return request.config.getoption('--status_code')
