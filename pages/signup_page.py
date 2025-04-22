from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators



class SignUp_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_signUp_Btn(self):
        sign_up_btn = self.wait.until(EC.presence_of_element_located(Locators.SIGN_UP_BTN))
        self.driver.execute_script('arguments[0].click();', sign_up_btn)
        
    def enter_signup_credentials(self,email,password,confirmPassword):
        send_email = self.wait.until(EC.presence_of_element_located(Locators.INPUT_EMAIL_SIGNUP))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_email, email)
        
        send_password = self.wait.until(EC.presence_of_element_located(Locators.INPUT_PASSWORD_LOGIN))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_password, password)

        send_confirm_password = self.wait.until(EC.presence_of_element_located(Locators.INPUT_CONFIRM_PASSWORD_SIGNUP))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_confirm_password, confirmPassword)
        
    def get_successful_login_msg(self):
        signup_success = self.wait.until(EC.presence_of_element_located(Locators.SUCCESSFUL_SIGNUP_MSG))
        text = self.driver.execute_script("return arguments[0].textContent;", signup_success)
        return text
    
    def get_validation_error_signUp(self):
        signUp_fail = self.wait.until(EC.presence_of_element_located(Locators.VALIDATION))
        text = self.driver.execute_script("return arguments[0].textContent",signUp_fail)
        return text
    
    def get_field_validation_error_msg_signUp(self):
        signUp_fail = self.wait.until(EC.presence_of_element_located(Locators.VALIDATION_ERROR_MSGS))
        text = self.driver.execute_script("return arguments[0].textContent",signUp_fail)
        return text



