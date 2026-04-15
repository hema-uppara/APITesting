
@Regression
Feature: Submit TechTargetGroupOffer API

  Background:
    Given the Submit TechTargetGroupOffer API is available

  @ttg
  Scenario: Submit TechTargetGroupOffer successfully
    When I submit a Conditional offer using "TechTargetGroupOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
