# pages/pollen_page.py
from pages.base_page import BasePage

class PollenPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def verify_region_forecast(self, region):
        region_heading = self.page.locator(f"h3.region-heading", has_text=region)
        region_heading.wait_for(state="visible")
        if not region_heading.is_visible():
            return False
            
        table = region_heading.locator("xpath=following-sibling::table[1]")
        if not table.is_visible():
            return False
            
        icons = table.locator("tbody tr td .weather-icons span.icon[data-type='pollen']")
        return icons.count() == 5
