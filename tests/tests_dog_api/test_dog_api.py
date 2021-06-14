import pytest
from unittest.mock import patch


class TestDogApi:

    def test_list_all_breeds(self, dog_api_obj):
        with patch("requests.request") as mock_request:
            r = dog_api_obj.request("list_all_breeds")
            mock_request.return_value.status_code = 200
            mock_request.return_value.json.return_value = {
                "message": {
                    "affenpinscher": [],
                    "african": []
                },
                "status": "success"
            }
            assert r.status_code == 200, f"{r.status_code} != 200"
            assert len(r.json()["message"]) >= 1, f"В списке отсутствует информация о породах"
            assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    @pytest.mark.parametrize("number_of_photos", ("1", "3", "5"))
    def test_random_image(self, dog_api_obj, number_of_photos):
        with patch("requests.request") as mock_request:
            r = dog_api_obj.request("random_image", number_of_photos=number_of_photos)
            mock_request.return_value.status_code = 200
            mock_request.return_value.json.return_value = {
                "message": list(range(int(number_of_photos))),
                "status": "success"
            }
            assert r.status_code == 200, f"{r.status_code} != 200"
            assert len(r.json()["message"]) == int(
                number_of_photos), f"В ответе от сервера количество фото != {number_of_photos}"
            assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    def test_by_breed(self, dog_api_obj):
        with patch("requests.request") as mock_request:
            r = dog_api_obj.request("by_breed")
            mock_request.return_value.status_code = 200
            mock_request.return_value.json.return_value = {
                "message": "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg",
                "status": "success"
            }
            assert r.status_code == 200, f"{r.status_code} != 200"
            assert len(r.json()["message"]) >= 1, f"В списке отсутствуют фото"
            assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    def test_list_all_sub_breeds(self, dog_api_obj):
        with patch("requests.request") as mock_request:
            r = dog_api_obj.request("list_all_sub_breeds")
            mock_request.return_value.status_code = 200
            mock_request.return_value.json.return_value = {
                "message": "afghan",
                "status": "success"
            }
            assert r.status_code == 200, f"{r.status_code} != 200"
            assert len(r.json()["message"]) >= 1, "В списке отсутствуют разновидности породы"
            assert r.json()["status"] == "success", f"{r.json()['status']} != success"

    @pytest.mark.parametrize("number_of_photos", ("1", "2", "3"))
    def test_multiple_images_from_a_sub_breed(self, dog_api_obj, number_of_photos):
        with patch("requests.request") as mock_request:
            r = dog_api_obj.request("multiple_images_from_a_sub_breed", number_of_photos=number_of_photos)
            mock_request.return_value.status_code = 200
            mock_request.return_value.json.return_value = {
                "message": list(range(int(number_of_photos))),
                "status": "success"
            }
            assert r.status_code == 200, f"{r.status_code} != 200"
            assert len(r.json()["message"]) == int(
                number_of_photos), f"В ответе от сервера количество фото != {number_of_photos}"
            assert r.json()["status"] == "success", f"{r.json()['status']} != success"
