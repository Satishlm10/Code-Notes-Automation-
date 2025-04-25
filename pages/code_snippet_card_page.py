from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Code_Snippet_Card_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    def get_main_page_title(self):
        title = self.wait.until(EC.presence_of_element_located(Locators.H1_MAIN_PAGE_TITLE))
        text = self.driver.execute_script('return arguments[0].textContent',title)
        return text
        
    def click_view_Link(self,codeSnippetCardNumber):
        view_link = self.wait.until(EC.presence_of_all_elements_located(Locators.VIEW_LINKS))
        self.driver.execute_script('arguments[0].click();', view_link[codeSnippetCardNumber])
        
    def get_titles_from_code_snippet_cards(self):
        titles = self.wait.until(EC.presence_of_all_elements_located(Locators.SNIPPET_CARDS_TITLE))
        return titles
    
    def get_title_in_code_snippet_details_page(self):
        title = self.wait.until(EC.presence_of_element_located(Locators.H1_TITLE))
        text = self.driver.execute_script('return arguments[0].textContent',title)
        return text
    
    def click_Back_to_Code_SNippets_link(self):
        back_link = self.wait.until(EC.presence_of_element_located(Locators.BACK_CODE_SNIPPET))
        self.driver.execute_script('arguments[0].click();', back_link)
        
    def click_Edit_btn(self):
        edit_btn = self.wait.until(EC.presence_of_element_located(Locators.DETAILS_EDIT_BTN))
        self.driver.execute_script('arguments[0].click();', edit_btn)
        
    def click_Delete_btn(self):
        delete_btn = self.wait.until(EC.presence_of_element_located(Locators.DETAILS_DELETE_BTN))
        self.driver.execute_script('arguments[0].click();', delete_btn)
        
