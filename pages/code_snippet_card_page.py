from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Code_Snippet_Card_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    def click_view_Link(self):
        view_link = self.wait.until(EC.presence_of_element_located(Locators.VIEW_LINKS))
        self.driver.execute_script('arguments[0].click();', view_link)
