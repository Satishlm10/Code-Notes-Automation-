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
    
    def click_new_tag_btn(self):
        new_tag_btn = self.wait.until(EC.presence_of_element_located(Locators.NEW_TAG_BTN))
        self.driver.execute_script('arguments[0].click();', new_tag_btn)

    def click_view_tag_link(self, tagName):
        rows = self.wait.until(EC.presence_of_all_elements_located((Locators.TAG_TD_BLOCK)))

        for row in rows:
            row_text = self.driver.execute_script("return arguments[0].textContent;", row).strip()
            if tagName in row_text:
                view_link = self.wait.until(EC.presence_of_element_located((Locators.VIEW_TAGS)))
                self.driver.execute_script('arguments[0].click();', view_link)
                return

        raise Exception(f"View link for tag '{tagName}' not found.")
    
    def click_edit_tag_link(self, tagName):
        rows = self.wait.until(EC.presence_of_all_elements_located((Locators.TAG_TD_BLOCK)))

        for row in rows:
            row_text = self.driver.execute_script("return arguments[0].textContent;", row).strip()
            if tagName in row_text:
                edit_tag = self.wait.until(EC.presence_of_element_located((Locators.EDIT_TAGS)))
                self.driver.execute_script('arguments[0].click();', edit_tag)
                return

        raise Exception(f"View link for tag '{tagName}' not found.")


    def click_delete_tag_link(self, tagName):
        rows = self.wait.until(EC.presence_of_all_elements_located((Locators.TAG_TD_BLOCK)))

        for row in rows:
            row_text = self.driver.execute_script("return arguments[0].textContent;", row).strip()
            if tagName in row_text:
                delete_tag = self.wait.until(EC.presence_of_element_located((Locators.DELETE_TAGS)))
                self.driver.execute_script('arguments[0].click();', delete_tag)
                return

        raise Exception(f"View link for tag '{tagName}' not found.")

    


