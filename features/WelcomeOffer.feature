
@Regression
Feature: Submit WelcomeOffer API

  Background:
    Given the Submit WelcomeOffer API is available

  @welcome
  Scenario: Submit WelcomeOffer successfully
    When I submit a Conditional offer using "WelcomeOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"
