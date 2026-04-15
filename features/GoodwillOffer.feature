
@Regression
Feature: Submit Goodwill Offer API

  Background:
    Given the Submit Goodwill Offer API is available

  @gw
  Scenario: Submit Goodwill offer successfully
    When I submit a Conditional offer using "GoodwillOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
