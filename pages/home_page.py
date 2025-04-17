# pages/home_page.py
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input_selector = "input[aria-label='Search for a place']"
        self.maps_charts_menu = "text=Maps & charts"
        self.precipitation_map_link = "text=Precipitation map"
        
        # Add a forecast items locator (adjust the selector based on the actual page structure)
        self.forecast_items_locator = ".forecast-item"  # Update this with the correct selector

    def search_for_location(self, location):
        search_box = self.page.get_by_label("Search for a place")
        search_box.click()
        search_box.fill(location)
        
    def select_location_from_results(self, location):
        self.page.get_by_role("menuitem", name=location).wait_for()
        self.page.get_by_role("menuitem", name=location).click()
        
    def navigate_to_precipitation_map(self):
        self.page.click(self.maps_charts_menu)
        self.page.click(self.precipitation_map_link)

    def get_forecast_items(self):
        """Return the forecast items (7-day forecast)"""
        return self.page.locator(self.forecast_items_locator)
