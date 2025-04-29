from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Navigation_Bar_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_signUp_Link(self):
        sign_up_link = self.wait.until(EC.presence_of_element_located(Locators.SIGN_UP))
        self.driver.execute_script('arguments[0].click();', sign_up_link)
        
    def get_logout_text_from_nav_bar(self):
        logout = self.wait.until(EC.presence_of_element_located(Locators.LOG_OUT))
        text = self.driver.execute_script("return arguments[0].textContent",logout)
        return text
    
    def click_login_link(self):
        login_link = self.wait.until(EC.presence_of_element_located(Locators.LOGIN))
        self.driver.execute_script('arguments[0].click();', login_link)
        
    def click_code_snippets_link(self):
        code_snippets_link = self.wait.until(EC.presence_of_element_located(Locators.CODE_SNIPPETS))
        self.driver.execute_script('arguments[0].click();', code_snippets_link)
        
    def click_my_dashboard_link(self):
        my_dashboard = self.wait.until(EC.presence_of_element_located(Locators.MY_DASHBOARD))
        self.driver.execute_script('arguments[0].click();', my_dashboard)
