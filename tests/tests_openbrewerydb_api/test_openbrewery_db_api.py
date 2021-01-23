import pytest


class TestOpenBreweryApi:

    def test_breeds_by_city(self, open_brewery_db_obj):
        r = open_brewery_db_obj.request("breweries", params={"by_city": "san_diego"})
        assert r.status_code == 200, f"{r.status_code} != 200"
        for brewery in r.json():
            assert brewery["city"] == "San Diego", \
                f"В ответе от сервера присутствуют пивоварни, у которых {brewery['city'] != 'San Diego'}"

    @pytest.mark.parametrize("Id", ("1", "500", "1000"))
    def test_get_one_brewery(self, open_brewery_db_obj, Id):
        r = open_brewery_db_obj.request("get_one_brewery", Id=Id)
        assert r.status_code == 200, f"{r.status_code} != 200"

    @pytest.mark.parametrize("how_search", ("MadTree", "dog"))
    def test_search_brewery(self, open_brewery_db_obj, how_search):
        r = open_brewery_db_obj.request("search_brewery", params={"query": how_search})
        assert r.status_code == 200, f"{r.status_code} != 200"

    @pytest.mark.parametrize("brewery_type", ("micro", "nano", "regional"))
    def test_breeds_by_type(self, open_brewery_db_obj, brewery_type):
        r = open_brewery_db_obj.request("breweries", params={"by_type": brewery_type})
        assert r.status_code == 200, f"{r.status_code} != 200"
        for brewery in r.json():
            assert brewery["brewery_type"] == brewery_type, \
                f"В ответе от сервера присутствуют пивоварни, у которых {brewery['brewery_type']} != {brewery_type}"

    @pytest.mark.parametrize("brewery_state", ("Ohio", "New%20York", "mexico"))
    def test_breeds_by_state(self, open_brewery_db_obj, brewery_state):
        r = open_brewery_db_obj.request("breweries", params={"by_state": brewery_state})
        assert r.status_code == 200, f"{r.status_code} != 200"
        for brewery in r.json():
            assert brewery["state"] == brewery_state, \
                f"В ответе от сервера присутствуют пивоварни, у которых {brewery['state']} != {brewery_state}"
