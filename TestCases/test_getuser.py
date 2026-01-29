import requests
import pytest

# Constants
GET_URL = "https://ms-api-gateway-qa.azurewebsites.net/offers/v1/offers"

headers = {
        "Accept": "application/json",
        "countrycode": "BG"
    }
 
class TestOffersAPI:

    def test_get_all_offers_success(self):
     
        response = requests.get(GET_URL, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        
        # Assert: Validate response content type
        assert "application/json" in response.headers["Content-Type"]
        
    def test_get_offers_performance(self):
        """
        Scenario: Verify API response time is within acceptable limits
        """
        response = requests.get(GET_URL)
        # Assert response time is less than 2 seconds
        assert response.elapsed.total_seconds() < 2.0, "API response is too slow"