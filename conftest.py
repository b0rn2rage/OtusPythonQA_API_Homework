import pytest
import configparser
from pathlib import Path
from dog_api.dog_api import DogApi
from openbrewerydb_api.openbrewerydb_api import OpenBreweryDbApi


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
