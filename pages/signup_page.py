from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators



class SignUp_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_signUp_Btn(self):
        self.wait.until(EC.presence_of_element_located(Locators.SIGN_UP_BTN)).click()
        
    def enter_valid_signup_credentials(self,email,password,confirmPassword):
        self.wait.until(EC.presence_of_element_located(Locators.INPUT_EMAIL_SIGNUP)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(Locators.INPUT_PASSWORD_LOGIN)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(Locators.INPUT_CONFIRM_PASSWORD_SIGNUP)).send_keys(confirmPassword)

