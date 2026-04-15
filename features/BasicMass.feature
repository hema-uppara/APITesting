
@Regression
Feature: Submit BasicMass Offer API

  Background:
    Given the Submit BasicMass Offer API is available

   @bm
  Scenario: Submit BasicMass offer successfully
    When I submit a BasicMass offer using "BasicMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"