
@Regression
Feature: Submit Conditional Offer API

  Background:
    Given the Submit Conditional Offer API is available

  @c
  Scenario: Submit Conditional offer successfully
    When I submit a Conditional offer using "ConditionalOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
