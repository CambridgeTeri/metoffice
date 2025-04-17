# features/metoffice_forecast.feature
Feature: Met Office Forecast Journey

  Scenario: A user checks the weather, changes preferences, views pollen forecast and precipitation map
    Given I am on the Met Office homepage
    When I search for "Cambridge" in the forecast search bar
    And I select "Cambridge (Cambridgeshire)" from the results
    Then I should see a 7-day weather forecast for Cambridge
    And today's forecast tab should be selected by default
    
    # Test temperature unit changes
    And I change the temperature unit to "Fahrenheit"
    And I change the temperature unit back to "Celsius"
    
    # Test detailed view functionality
    And I expand the full forecast view
    Then I should see wind speed unit options
    And I change the wind speed unit to "mph"
    And I collapse the full forecast view
    
    # Navigate to pollen forecast and check
    When I click the Pollen link
    Then I should see the 5-day pollen forecast for "East of England"
    
    # Navigate to precipitation map
    When I view the precipitation map
    Then I should see the UK precipitation map


