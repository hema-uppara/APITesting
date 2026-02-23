import requests
import pytest


# Constants
POST_URL="https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers"

headers = {
        "Accept": "application/json",
        "countrycode": "BG"
    }
 
class TestOffersAPI_post:


    REMOTE_URL = "http://localhost:4444/wd/hub" 

    @pytest.fixture(scope="function")
    def test_post_offer_payload(self):
        """Fixture to provide a standard offer payload"""
        return {
            
    
    "offerType": "REWARD_LIMIT_MASS",
    "offerCode": "surprise limitations",
    "rewardLimitPeriod":"Value",
    "rewardLimitType":"Day",
    "rewardLimitValue":"1",
 
    "costOfReward": 1,
   
    "rewardEngineExcluded": False,
    "assignableFrom": "2026-02-09T00:00:00+03:00",
    "assignableTo": "2026-03-30T00:00:00+03:00",
    "deactivationAllowed": False,
    "displayOrder": 0,
    "initiallyActive": True,
    "numberOfAssign": 1,
    "numberOfUsage": 1,
    "offerRewardRule": {
        "ruleType": "FIX_DISCOUNT",
        "productCode": "CG0000003763",
        "rewardValue": 1
    },
    "offerTitle": [
        {
            "language": "bg",
            "text": "as"
        },
        {
            "language": "en",
            "text": "as"
        }
    ],
    "offerDescription": [
        {
            "language": "bg",
            "text": "<p><span>as</span></p>"
        },
        {
            "language": "en",
            "text": "<p><span>as</span></p>"
        }
    ],
    "customText": [
        {
            "language": "bg",
            "text": "as"
        },
        {
            "language": "en",
            "text": "as"
        }
    ],
    "offerReceiptMessage": [
        {
            "language": "bg",
            "text": "A"
        },
        {
            "language": "en",
            "text": "as"
        }
    ],
    "offerName": "Testing offername",
    "offerBackground": "0486440c-06b3-5502-8a52-30baec795efe",
    "experimentalGroups": [
        "2",
        "4",
        "6",
        "8"
    ],
    "consents": {
        "tested": True,
        "redeemed": True,
        "approved": True
    }
}
        
    def test_post_all_offers_success(self,test_post_offer_payload):
    
        response = requests.get(POST_URL, headers=headers,json=test_post_offer_payload)
        assert response.status_code in [200, 201], f"Failed with {response.status_code}: {response.text}"
       #response_data = response.json()
        #actual_id = response_data.get("offerId")
        #payload_id = test_post_offer_payload.get("offerId")
        #print(actual_id)
        #print(payload_id)
        #assert actual_id != payload_id, f"Expected different ID, but both are {actual_id}"