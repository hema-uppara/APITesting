
@Regression
Feature: Submit SurpriseOffer Offer API

  Background:
    Given the Submit SurpriseOffer Offer API is available

  @surprise
  Scenario: Submit SurpriseOffer offer successfully
    When I submit a Conditional offer using "SurpriseOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"