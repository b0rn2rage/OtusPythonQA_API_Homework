import requests


def test_addoption(url, my_status_code):
    r = requests.get(url, my_status_code)
    assert r.status_code == int(my_status_code)
