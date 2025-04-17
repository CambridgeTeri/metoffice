# pages/forecast_page.py
from pages.base_page import BasePage
from datetime import datetime

class ForecastPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.forecast_section = "section.day-tabs-container"
        self.temperature_unit_select = "#temperature-unit-select"
        self.detailed_view_button = "#btnDetailedView"
        self.wind_unit_select = "select#wind-unit-select"
        self.pollen_link = "a.pollen-link"
        
    def is_forecast_visible(self):
        self.page.locator(self.forecast_section).wait_for(state="visible", timeout=10000)
        return self.page.locator(self.forecast_section).is_visible()
        
    def is_today_tab_selected(self):
        today_str = datetime.today().strftime("%Y-%m-%d")
        today_tab = self.page.locator(f"#dayTab-{today_str}")
        today_tab.wait_for(state="attached", timeout=5000)
        return "active-tab" in (today_tab.get_attribute("class") or "")
        
    def change_temperature_unit(self, unit):
        unit_value = "f" if unit.lower() == "fahrenheit" else "c"
        self.page.select_option(self.temperature_unit_select, unit_value)
        
    def toggle_detailed_view(self, expand=True):
        button = self.page.locator(self.detailed_view_button)
        current_state = button.get_attribute("aria-expanded")
        if (expand and current_state == "false") or (not expand and current_state == "true"):
            button.click()
            
    def get_wind_speed_options(self):
        wind_select = self.page.locator(self.wind_unit_select)
        return wind_select.locator("option").all_inner_texts()
        
    def change_wind_speed_unit(self, unit):
        self.page.select_option(self.wind_unit_select, unit)
        
    def navigate_to_pollen_forecast(self):
        pollen_link = self.page.locator(self.pollen_link, has_text="Pollen").first
        pollen_link.wait_for(state="visible")
        with self.page.expect_navigation():
            pollen_link.click()