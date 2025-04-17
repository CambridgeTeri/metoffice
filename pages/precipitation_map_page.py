# pages/precipitation_map_page.py
from pages.base_page import BasePage

class PrecipitationMapPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.loading_indicator = ".loading-map"
        self.precipitation_label = "text=Precipitation type"
        
    def is_map_visible(self):
        self.page.locator(self.loading_indicator).wait_for(state="detached", timeout=10000)
        return self.page.locator(self.precipitation_label).is_visible()