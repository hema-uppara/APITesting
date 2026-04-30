
@Regression
Feature: Submit GameMassOffer API

  Background:
    Given the Submit GameMassOffer Offer API is available

  @gm
  Scenario: Submit GameMassOffer offer successfully
    When I submit a Conditional offer using "GameMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
