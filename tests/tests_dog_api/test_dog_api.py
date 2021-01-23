import pytest


class TestDogApi:

    def test_list_all_breeds(self, dog_api_obj):
        r = dog_api_obj.request("list_all_breeds")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()["message"]) >= 1, f"В списке отсутствует информация о породах"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    @pytest.mark.parametrize("number_of_photos", ("1", "25", "50"))
    def test_random_image(self, dog_api_obj, number_of_photos):
        r = dog_api_obj.request("random_image", number_of_photos=number_of_photos)
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()["message"]) == int(
            number_of_photos), f"В ответе от сервера количество фото != {number_of_photos}"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    def test_by_breed(self, dog_api_obj):
        r = dog_api_obj.request("by_breed")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()["message"]) >= 1, f"В списке отсутствуют фото"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    def test_list_all_sub_breeds(self, dog_api_obj):
        r = dog_api_obj.request("list_all_sub_breeds")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()["message"]) >= 1, "В списке отсутствуют разновидности породы"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    @pytest.mark.parametrize("number_of_photos", ("1", "2", "3"))
    def test_multiple_images_from_a_sub_breed(self, dog_api_obj, number_of_photos):
        r = dog_api_obj.request("multiple_images_from_a_sub_breed", number_of_photos=number_of_photos)
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()["message"]) == int(
            number_of_photos), f"В ответе от сервера количество фото != {number_of_photos}"
        assert r.json()["status"] == "success", f"{r.json()['status']} != success"
