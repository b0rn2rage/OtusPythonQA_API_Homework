import pytest


class TestOpenBreweryApi:

    def test_list_all_breeds(self, open_brewery_db_obj):
        r = open_brewery_db_obj.request("breweries", params={"by_city": "san_diego"})
        assert r.status_code == 200, f"{r.status_code} != 200"
        for brewery in r.json():
            assert brewery["city"] == "San Diego", \
                f"В ответе от сервера присутствуют пивоварни, у которых {brewery['city'] != 'San Diego'}"

    @pytest.mark.parametrize("Id", ("1", "500", "1000"))
    def test_get_one_brewery(self, open_brewery_db_obj, Id):
        r = open_brewery_db_obj.request("get_one_brewery", Id=Id)
        assert r.status_code == 200, f"{r.status_code} != 200"
