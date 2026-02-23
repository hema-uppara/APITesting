import requests
import pytest

# Constants
PUT_URL="https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers/2054363"

headers = {
        "Accept": "application/json",
        "countrycode": "BG"
    }
 
class TestOffersAPI_put:
    REMOTE_URL = "http://localhost:4444/wd/hub" 

    @pytest.fixture(scope="function")
    def test_put_offer_payload(self):
        """Fixture to provide a standard offer payload"""
        return {
  "offerType": "GAME_MASS",
  "offerCode": "Testing Offer code",
  "rewardEngineExcluded": True,
  "assignableFrom": "2026-01-29T05:39:00+00:00",
  "assignableTo": "2026-01-29T23:30:00+00:00",
  "displayOrder": 0,
  "numberOfUsage": 1,
  "offerRewardRule": {
    "ruleType": "GAME_INVITATION"
  },
  "offerRewardConditionRule": [
    {
      "conditionRuleType": "PRODUCT_PURCHASE_VALUE",
      "productCode": "CG0000000185",
      "requiredValue": 1
    }
  ],
  "offerTitle": [
    {
      "language": "en",
      "text": "MIC-9908_future date_21/10/2025"
    }
  ],
  "offerDescription": [
    {
      "language": "en",
      "text": "<p><span>MIC-9908_future date_21/10/2025</span></p>"
    }
  ],
  "customText": [
    {
      "language": "en",
      "text": "MIC-9908_future date_21/10/2025"
    }
  ],
  "offerBackground": "265c176b-8c09-515a-8f15-fa094c82465e",
  "campaignName": "Testing CN",
  "offerMechanics": "Testing OM",
  "productType": "FU",
  "versionNumber": "V2",
  "partnerCode": "1234",
  "partnerFundingPercentage": 1,
  "gameDetails": {
    "prizeDescription": [
      {
        "language": "en",
        "text": "MIC-9908_future date_21/10/2025"
      }
    ],
    "gameURL": "ww.shell.com",
    "gameDescription": [
      {
        "language": "en",
        "text": "MIC-9908_future date_21/10/2025"
      }
    ],
    "gameIcon": "0c10ab07-0ba0-5820-b00c-daaba63d1e9e",
    "gameType": "Knowledge Game",
    "gameTANDCURL": "ww.shell.com",
    "inviteDurationDays": 2,
    "campaignOverviewImage": "0c10ab07-0ba0-5820-b00c-daaba63d1e9e"
  },
  "relatedOffers": {
    "targetedOfferId": 2054364
  }
}
        
    def test_put_all_offers_success(self,test_put_offer_payload):
    
        response = requests.get(PUT_URL, headers=headers,json=test_put_offer_payload)
        assert response.status_code in [200, 201], f"Failed with {response.status_code}: {response.text}"
        #response_data = response.json()
        #actual_id = response_data.get("offerId")
        #payload_id = test_post_offer_payload.get("offerId")
        #print(actual_id)
        #print(payload_id)
        #assert actual_id != payload_id, f"Expected different ID, but both are {actual_id}"