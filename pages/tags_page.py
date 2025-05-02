from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Tags_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
    
    def get_h1_title_of_tags_page(self):
        title = self.wait.until(EC.presence_of_element_located(Locators.TAG_PAGE_TITLE))
        text = self.driver.execute_script("return arguments[0].textContent",title)
        return text



