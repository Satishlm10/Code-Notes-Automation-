from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class My_Dashboard_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_edit_icon(self,codeSnippetNumber):
        edit_icon = self.wait.until(EC.presence_of_all_elements_located(Locators.EDIT_ICON))
        self.driver.execute_script('arguments[0].click();', edit_icon[codeSnippetNumber])

    def click_delete_icon(self,codeSnippetNumber):
        delete_icon = self.wait.until(EC.presence_of_all_elements_located(Locators.DELETE_ICON))
        self.driver.execute_script('arguments[0].click();', delete_icon[codeSnippetNumber])
        

    

