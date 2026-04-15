
@Regression
Feature: Submit TargetedGameMass Offer API

  Background:
    Given the Submit TargetedGameMass Offer API is available

  @tgm
  Scenario: Submit TargetedGameMass offer successfully
    When I submit a Conditional offer using "TargetedGameMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
