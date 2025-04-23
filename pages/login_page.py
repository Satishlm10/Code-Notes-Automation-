from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators



class Login_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def enter_valid_login_credentials(self,email,password):
        send_email = self.wait.until(EC.presence_of_element_located(Locators.INPUT_EMAIL_LOGIN))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_email, email)
        
        send_password = self.wait.until(EC.presence_of_element_located(Locators.INPUT_PASSWORD_LOGIN))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_password, password)     

    def click_signin_btn(self):
        signInBtn = self.wait.until(EC.presence_of_element_located(Locators.SIGN_IN_BTN))
        self.driver.execute_script('arguments[0].click()',signInBtn)
        
    def get_login_validation_error_msg(self):
        login_validation = self.wait.until(EC.presence_of_element_located(Locators.VALIDATION_LOGIN))
        text = self.driver.execute_script("return arguments[0].textContent",login_validation)
        return text
    
    def click_forgot_password_link(self):
        forgot_password = self.wait.until(EC.presence_of_element_located(Locators.FORGOT_PASSWORD))
        self.driver.execute_script('arguments[0].click()',forgot_password)
        
    def enter_email_in_forgot_password_field(self,email):
        send_email = self.wait.until(EC.presence_of_element_located(Locators.INPUT_EMAIL_LOGIN))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_email, email)

    def click_reset_instruction_btn(self):
        forgot_password = self.wait.until(EC.presence_of_element_located(Locators.RESET_INSTRUCTION))
        self.driver.execute_script('arguments[0].click()',forgot_password)
        
    def get_reset_password_validation_error_msg(self):
        reset_validation = self.wait.until(EC.presence_of_element_located(Locators.RESET_VALIDATION))
        text = self.driver.execute_script("return arguments[0].textContent",reset_validation)
        return text

    def get_reset_password_success_msg(self):
        reset_msg = self.wait.until(EC.presence_of_element_located(Locators.VALID_RESET_MSG))
        text = self.driver.execute_script("return arguments[0].textContent",reset_msg)
        return text