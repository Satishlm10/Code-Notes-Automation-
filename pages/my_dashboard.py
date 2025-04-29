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
        
    def enter_title_in_search_bar(self,title):
        search_bar = self.wait.until(EC.presence_of_element_located(Locators.SEARCH_BAR))
        self.driver.execute_script("arguments[0].value = arguments[1];", search_bar, title)
    
    def click_apply_btn(self):
        search_bar = self.wait.until(EC.presence_of_element_located(Locators.SEARCH_FORM))
        self.driver.execute_script("arguments[0].submit();", search_bar)
        
    def get_title_in_code_snippet_details_page(self):
        titles = self.wait.until(EC.presence_of_all_elements_located(Locators.TITLES_IN_CODE_SNIPPET_MY_DASHBOARD))
        return titles
    

