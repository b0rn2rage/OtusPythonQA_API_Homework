import requests


class JsonPlaceholderApi:
    FUNCTION_MAPPING = {"get_posts": "posts",
                        "get_concrete_post": "posts/{post_number}",
                        "get_comments": "posts/{post_number}/comments"}

    def __init__(self, url):
        self.url = url

    def get_endpoint(self, url, function_name, **kwargs):
        function_mapping = self.FUNCTION_MAPPING[function_name]
        for k, v in kwargs.items():
            function_mapping = self.FUNCTION_MAPPING[function_name].replace('{' + k + '}', v)
        return url + function_mapping

    def request(self, function_name, method="GET", json=None, params=None, headers=None, **kwargs):
        endpoint = self.get_endpoint(self.url, function_name, **kwargs)
        response = requests.request(method=method, url=endpoint, params=params, json=json, headers=headers)
        return response
