from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class New_Code_Snippet_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    def click_new_code_snippet_link(self):
        new_code_snippet = self.wait.until(EC.presence_of_element_located(Locators.NEW_CODE_SNIPPET))
        self.driver.execute_script('arguments[0].click();', new_code_snippet)
        
    def get_form_title_new_code_snippet(self):
        form_title = self.wait.until(EC.presence_of_element_located(Locators.FORM_TITLE))
        text = self.driver.execute_script("return arguments[0].textContent",form_title)
        return text