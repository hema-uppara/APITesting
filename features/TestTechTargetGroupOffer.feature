
@Regression
Feature: Submit TestTechTargetGroupOffer API

  Background:
    Given the Submit TestTechTargetGroupOffer API is available

  @tttg
  Scenario: Submit TestTechTargetGroupOffer successfully
    When I submit a Conditional offer using "TestTechTargetGroupOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
