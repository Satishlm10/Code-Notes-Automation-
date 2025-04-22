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
        self.driver.execute_script('arguments[0].click();', signInBtn)



