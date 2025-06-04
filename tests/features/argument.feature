Feature: Arguments

  Scenario: Test Arguments
    Given there are 5 cucumbers
    When I eat 3 cucumbers
    Then I should have 2 cucumbers


   Scenario: Test Zero cucumbers
     Given there are 10 cucumbers
     When I eat 10 cucumbers
     Then I should have 0 cucumbers