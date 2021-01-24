import pytest


class TestJsonPlaceholderApi:

    def test_all_posts(self, json_placeholder_obj):
        r = json_placeholder_obj.request("get_posts")
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert len(r.json()) == 100, f"Сервер отдал не полный список юзеров. Их = {len(r.json())}, а должно быть 100"

    @pytest.mark.parametrize("post_number", ("1", "50", "100"))
    def test_get_concrete_post(self, json_placeholder_obj, post_number):
        r = json_placeholder_obj.request("get_concrete_post", post_number=post_number)
        assert r.status_code == 200, f"{r.status_code} != 200"
        assert r.json()["id"] == int(post_number), \
            f"Сервер отдал не верный номер поста. Он = {r.json()['id']}, а должен быть {int(post_number)}"

    @pytest.mark.parametrize("post_number", ("1", "5", "10"))
    def test_get_comments(self, json_placeholder_obj, post_number):
        r = json_placeholder_obj.request("get_comments", post_number=post_number)
        assert r.status_code == 200, f"{r.status_code} != 200"
        for comment in r.json():
            assert comment["postId"] == int(post_number), \
                f"Сервер отдал комментарий, который не приналджит к посту № {post_number}"

    def test_post_posts(self, json_placeholder_obj):
        r = json_placeholder_obj.request("get_posts", method="POST", json={"title": "random",
                                                                           "body": "qwerty",
                                                                           "userId": 1},
                                         headers={"Content-type": "application/json; charset=UTF-8"})
        assert r.status_code == 201, f"{r.status_code} != 201"
        assert r.json()["id"] == 101, "Созданный объект имеет некорректный id"

    def test_put_posts(self, json_placeholder_obj):
        r = json_placeholder_obj.request("get_concrete_post", post_number="1", method="PUT", json={"title": "random",
                                                                                                   "body": "qwerty",
                                                                                                   "userId": 1},
                                         headers={"Content-type": "application/json; charset=UTF-8"})
        assert r.status_code == 200, f"{r.status_code} != 201"
        assert r.json()["title"] == "random", f"Объект не обновился, {r.json()['title']} != random"
