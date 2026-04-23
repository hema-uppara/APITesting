Feature: Submit PointConditionalOffer Offer API

  Background:
    Given the Submit PointConditionalOffer API is available

  @pc
  Scenario: Submit PointConditionalOffer successfully
    When I submit a Conditional offer using "PointConditionalOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"