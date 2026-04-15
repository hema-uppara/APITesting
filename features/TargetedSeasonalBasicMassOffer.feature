
@Regression
Feature: Submit TargetedSeasonalBasicMassOffer API

  Background:
    Given the Submit TargetedSeasonalBasicMassOffer API is available

  @tsbm
  Scenario: Submit TargetedSeasonalBasicMassOffer successfully
    When I submit a Conditional offer using "TargetedSeasonalBasicMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
