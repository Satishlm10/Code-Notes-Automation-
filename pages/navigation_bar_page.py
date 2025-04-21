from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Navigation_Bar_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_signUp_Link(self):
        self.wait.until(EC.presence_of_element_located(Locators.SIGN_UP)).click()
        
   

