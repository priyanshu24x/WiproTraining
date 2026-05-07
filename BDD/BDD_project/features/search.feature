

Feature: Search
  Scenario: Search for product
    Given Buyer is on the OLX home page
    When Buyer types product in searchbar
    Then search results should be displayed

  Scenario: Search for a product with no results
    Given buyer is on the OLX homepage
    When buyer types product in searcher
    Then Error message should be displayed
