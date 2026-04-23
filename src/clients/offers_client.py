import json
import requests
from datetime import datetime, timedelta
from features.utils.config import Config

class OffersClient:

    @staticmethod
    def create_offer(headers, payload):
        # Inject dynamic future dates into payload
        payload["assignableFrom"] = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S+01:00")
        payload["assignableTo"] = (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%dT%H:%M:%S+01:00")
        url = Config.BASE_URL + Config.CREATE_OFFER_ENDPOINT
        return requests.post(
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )