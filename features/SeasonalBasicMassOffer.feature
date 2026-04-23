
@Regression
Feature: Submit SeasonalBasicMassOffer API

  Background:
    Given the Submit SeasonalBasicMassOffer API is available

  @sbm
  Scenario: Submit SeasonalBasicMassOffer successfully
    When I submit a Conditional offer using "SeasonalBasicMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
