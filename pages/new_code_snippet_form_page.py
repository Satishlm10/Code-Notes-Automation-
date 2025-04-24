from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import JavascriptException



class New_Code_Snippet_Page:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
    def click_new_code_snippet_link(self):
        new_code_snippet = self.wait.until(EC.presence_of_element_located(Locators.NEW_CODE_SNIPPET))
        self.driver.execute_script('arguments[0].click();', new_code_snippet)
        
    def get_form_title_new_code_snippet(self):
        form_title = self.wait.until(EC.presence_of_element_located(Locators.FORM_TITLE))
        text = self.driver.execute_script('return arguments[0].textContent',form_title)
        return text
    

    def input_title(self, title):
        title_field = self.wait.until(EC.presence_of_element_located(Locators.INPUT_TITLE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", title_field)  # Scroll into view
        self.driver.execute_script("arguments[0].value = '';", title_field)  # Clear the field using JS
        self.driver.execute_script("arguments[0].value = arguments[1];", title_field, title)  # Set the title using JS
    
    def select_language(self, language):
        language_element = self.wait.until(EC.presence_of_element_located(Locators.INPUT_LANGUAGE))
        self.driver.execute_script(f"arguments[0].value = '{language}';", language_element)
        
    
    def input_description(self, description):
        description_field = self.wait.until(EC.presence_of_element_located(Locators.INPUT_DESCRIPTION))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", description_field)  # Scroll into view
        self.driver.execute_script("arguments[0].value = '';", description_field)  # Clear the field using JS
        self.driver.execute_script("arguments[0].value = arguments[1];", description_field, description)  # Set description using JS
    
    def input_code(self, code):
        code_field = self.wait.until(EC.presence_of_element_located(Locators.INPUT_CODE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", code_field)  # Scroll into view
        self.driver.execute_script("arguments[0].value = '';", code_field)  # Clear the field using JS
        self.driver.execute_script("arguments[0].value = arguments[1];", code_field, code)  # Set code using JS
    
    def toggle_private_checkbox(self, should_check=True):
        private_checkbox = self.wait.until(EC.presence_of_element_located(Locators.INPUT_PRIVATE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", private_checkbox)  # Scroll into view
        is_selected = self.driver.execute_script("return arguments[0].checked;", private_checkbox)
        if is_selected != should_check:
            self.driver.execute_script('arguments[0].click();', private_checkbox)  # Click using JS if checkbox needs to be toggled
    
    def select_tag(self, tag_name):
        # Use the method from Locators to get the correct locator
        tag_checkbox_locator = Locators.get_tag_checkbox_locator(tag_name)
        tag_checkbox = self.wait.until(EC.presence_of_element_located(tag_checkbox_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tag_checkbox)  # Scroll into view
        is_selected = self.driver.execute_script("return arguments[0].checked;", tag_checkbox)
        if not is_selected:
            self.driver.execute_script('arguments[0].click();', tag_checkbox)  # Select tag using JS
    
    def click_create_button(self):
        create_button = self.wait.until(EC.presence_of_element_located(Locators.CREATE_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_button)  # Scroll into view
        self.driver.execute_script('arguments[0].click();', create_button)  # Submit the form using JS
    
    def click_manage_tags_link(self):
        manage_tags_link = self.wait.until(EC.presence_of_element_located(Locators.MANAGE_TAG_LINK))
        self.driver.execute_script('arguments[0].click();', manage_tags_link)  # Click on Manage Tags link using JS
    
    def get_success_message(self):
        success_message_element = self.wait.until(EC.presence_of_element_located(Locators.SUCCESS_MSG))
        return self.driver.execute_script('return arguments[0].textContent', success_message_element)  # Get success message text using JS
    
    def is_error_displayed(self):
        error_msg = self.wait.until(EC.presence_of_all_elements_located(Locators.VALIDATION_ERROR_MSGS))
        return error_msg