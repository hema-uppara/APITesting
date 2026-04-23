Feature: Submit PartnerBasicMass Offer API

  Background:
    Given the Submit PartnerBasicMass Offer API is available

  @pbm
  Scenario: Submit PartnerBasicMass offer successfully
    When I submit a Conditional offer using "PartnerBasicMassOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"