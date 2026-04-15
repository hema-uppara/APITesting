import requests


class ApiClient:

    @staticmethod
    def post(base_url, endpoint, headers, payload):
        url = f"{base_url}{endpoint}"
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            verify=False
        )
        return response