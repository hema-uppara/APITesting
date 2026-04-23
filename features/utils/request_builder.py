import requests

class RequestBuilder:

    def __init__(self, base_url, headers, timeout=30):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def post(self, endpoint, payload):
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
