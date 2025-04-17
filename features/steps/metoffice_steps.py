from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from datetime import datetime
import time as time_module

@given("I am on the Met Office homepage")
def step_impl(context):
    # The page objects are already created in environment.py
    # Just use them directly
    context.home_page.navigate("https://www.metoffice.gov.uk")
    context.home_page.handle_cookies()

@when('I search for "{location}" in the forecast search bar')
def step_impl(context, location):
    context.home_page.search_for_location(location)

@when('I select "{location}" from the results')
def step_impl(context, location):
    context.home_page.select_location_from_results(location)

@then("I should see a 7-day weather forecast for Cambridge")
def step_impl(context):
    # Use the forecast page object to verify the forecast is visible
    assert context.forecast_page.is_forecast_visible(), "7-day forecast section not visible on the page"

@then("today's forecast tab should be selected by default")
def step_impl(context):
    # Use the forecast page object to verify today's tab is selected
    assert context.forecast_page.is_today_tab_selected(), "Today's tab is not selected by default"

@then('I change the temperature unit to "Fahrenheit"')
def step_impl(context):
    context.forecast_page.change_temperature_unit("Fahrenheit")

@then('I change the temperature unit back to "Celsius"')
def step_impl(context):
    context.forecast_page.change_temperature_unit("Celsius")

@then('I expand the full forecast view')
def step_impl(context):
    context.forecast_page.toggle_detailed_view(expand=True)

@then('I should see wind speed unit options')
def step_impl(context):
    wind_options = context.forecast_page.get_wind_speed_options()
    expected_options = ['mph', 'km/h', 'knots', 'm/s', 'Beaufort']
    for opt in expected_options:
        assert any(opt in option for option in wind_options), f"Missing wind option: {opt}"

@then('I change the wind speed unit to "mph"')
def step_impl(context):
    context.forecast_page.change_wind_speed_unit("mph")
    wind_select = context.page.locator("select#wind-unit-select")
    selected = wind_select.input_value()
    assert selected == "mph", f"Expected wind unit to be 'mph', but got {selected}"

@then('I collapse the full forecast view')
def step_impl(context):
    context.forecast_page.toggle_detailed_view(expand=False)

@when("I click the Pollen link")
def step_impl(context):
    context.forecast_page.navigate_to_pollen_forecast()

@then('I should see the 5-day pollen forecast for "{region}"')
def step_impl(context, region):
    # Use the pollen page object to verify the forecast
    assert context.pollen_page.verify_region_forecast(region), f"Could not verify 5-day pollen forecast for {region}"

@when("I view the precipitation map")
def step_impl(context):
    # Navigate to the Maps & charts section and select precipitation map
    # We need to use the home page to get to the Maps & charts section
    context.home_page.navigate_to_precipitation_map()

@then("I should see the UK precipitation map")
def step_impl(context):
    # Wait for the map loading spinner to disappear, if present
    loading_selector = ".loading-map"
    try:
        context.page.locator(loading_selector).wait_for(state="detached", timeout=10000)
        print("Map loading spinner has disappeared.")
    except:
        print("Map loading spinner still present or took too long.")

    # Wait for the map to be visible and assert it
    map_element = context.page.locator("#map")
    
    try:
        map_element.wait_for(state="visible", timeout=15000)
        print("Precipitation map is visible.")
    except:
        print("Map not visible within timeout.")
    
    assert map_element.is_visible(), "Precipitation map (#map) is not visible"
    
    # Optional: check dimensions to ensure it’s rendered correctly
    map_box = map_element.bounding_box()
    assert map_box, "Map bounding box is not available."
    assert map_box["width"] > 0 and map_box["height"] > 0, "Map appears to be hidden or not rendered properly."

    print(f"Map dimensions: {map_box['width']} x {map_box['height']}")