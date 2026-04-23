Feature: Submit RewardLimitMassOffer Offer API

  Background:
    Given the Submit RewardLimitMassOffer Offer API is available

  @rlm
  Scenario: Submit RewardLimitMassOffer offer successfully
    When I submit a Conditional offer using "RewardLimitMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"