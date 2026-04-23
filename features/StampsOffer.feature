
@Regression
Feature: Submit StampsOffer API

  Background:
    Given the Submit StampsOffer API is available

  @s
  Scenario: Submit SeasonalBasicMassOffer successfully
    When I submit a Conditional offer using "StampsOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
