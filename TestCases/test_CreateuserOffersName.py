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
            
    "offerID": 2054602,
    "status": "Draft",
    "dateTimeCreated": "2026-02-16T04:31:02.899Z",
    "dateTimeUpdated": "2026-02-16T04:35:50.177Z",
    "countryCode": "GB",
    "offerType": "GAME_MASS",
    "campaignName": "Hema CN",
    "offerMechanics": "Hema OM",
    "productType": "CR",
    "versionNumber": "V3",
    "offerName": "GB_Hema CN_Hema OM_CR_V3",
    "offerCode": "surprise limitations",
    "rewardEngineExcluded": True,
    "displayOrder": 0,
    "numberOfUsage": 2,
    "offerRewardRule": {
        "ruleType": "GAME_INVITATION"
    },
    "offerRewardConditionRule": [
        {
            "conditionRuleType": "PRODUCT_PURCHASE_MULTI_VALUE",
            "requiredValue": 1,
            "conditionType": "COST_ENDS_WITH",
            "endingValue": 23,
            "endingValueUpperLimit": 2000
        }
    ],
    "offerTitle": [
        {
            "language": "en",
            "text": "Test offer"
        }
    ],
    "offerDescription": [
        {
            "language": "en",
            "text": "\u003cp\u003e\u003cspan\u003eTest offer\u003c/span\u003e\u003c/p\u003e"
        }
    ],
    "customText": [
        {
            "language": "en",
            "text": "Test offer"
        }
    ],
    "partnerCode": "Playable",
    "partnerFundingPercentage": 1,
    "offerBackground": "77ff4b5f-b0e8-5918-8253-751a433a5aa6",
    "gameDetails": {
        "prizeDescription": [
            {
                "language": "en",
                "text": "Test offer"
            }
        ],
        "gameURL": "ww.shell.com",
        "gameDescription": [
            {
                "language": "en",
                "text": "Test offer"
            }
        ],
        "gameIcon": "90e7eada-371d-535a-8692-31696964b505",
        "gameType": "Knowledge Game",
        "gameTANDCURL": "ww.shell.com",
        "inviteDurationDays": 2,
        "campaignOverviewImage": "265c176b-8c09-515a-8f15-fa094c82465e"
    },
    "assignableFrom": "2026-02-16T04:37:00+00:00",
    "assignableTo": "2026-02-16T23:30:00+00:00",
    "assign": {
        "counter": 0,
        "consumers": []
    },
    "external": {}
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