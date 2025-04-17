# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url)
        
    def handle_cookies(self):
        try:
            self.page.wait_for_selector("button:has-text('Accept All')", timeout=5000)
            self.page.click("button:has-text('Accept All')")
        except:
            print("Cookie banner not shown or already handled")