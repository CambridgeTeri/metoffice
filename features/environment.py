# environment.py
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.forecast_page import ForecastPage
from pages.pollen_page import PollenPage
from pages.precipitation_map_page import PrecipitationMapPage

def before_scenario(context, scenario):
    # Initialize the Playwright browser instance
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

    # Initialize page objects
    context.home_page = HomePage(context.page)
    context.forecast_page = ForecastPage(context.page)
    context.pollen_page = PollenPage(context.page)
    context.precipitation_map_page = PrecipitationMapPage(context.page)

def after_scenario(context, scenario):
    # Cleanup
    context.browser.close()
    context.playwright.stop()