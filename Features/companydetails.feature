Feature: Company Details

  Scenario: Fetching Company Details
    Given He Opened Google Page
    When He Search Company Name "Actualize Consulting Engineers"
    When He Look For Card Apperance
    Then He Save Details Of Company

  Scenario Outline: Details Of Company
    Given He Opened Google Page
    When He Search Company Name "<company_name>"
    When He Look For Card Apperance
    Then He Save Details Of Company
    Examples:
      | company_name               |
      | g7cr                       |
      | Fime India Private Limited |
      |TCS                         |