Feature: Submit PartnerSurprise Offer API

  Background:
    Given the Submit PartnerSurprise Offer API is available

  @ps
  Scenario: Submit PartnerSurprise offer successfully
    When I submit a Conditional offer using "PartnerSurpriseOffer.json"
    Then the response status code should be 201
    And the response should contain offerId
    And the response should contain offerCode
    And the response status should be "LoadedToCampaign"