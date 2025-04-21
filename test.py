from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from pages.signup_page import SignUp_Page
from pages.navigation_bar_page import Navigation_Bar_Page
from pages.code_snippet_card_page import Code_Snippet_Card_Page
import json

from selenium.webdriver.chrome.options import Options


class CodeNotes_Test(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        # self.driver = webdriver.Chrome()
        
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
        self.signUp_page = SignUp_Page(self.driver)
        self.navigation_page = Navigation_Bar_Page(self.driver)
        self.code_snippet_card = Code_Snippet_Card_Page(self.driver)
        
        
    def test_signUp_with_valid_credentials(self):
        expected_result = 'Welcome! You have signed up successfully.'
        self.navigation_page.click_signUp_Link()
        self.signUp_page.enter_valid_signup_credentials("test@test1.com","Test@123","Test@123")
        self.signUp_page.click_signUp_Btn()
        actual_result = self.signUp_page.get_successful_login_msg()
        try:
            self.assertEqual(actual_result,expected_result)
            print("Test Pass - User Successfully signed up  with valid credentials")
        except AssertionError as e:
            print("Test Failed - User cannot sign up with valid credentials")
        
    def test_view_a_code_snippet(self):
        self.code_snippet_card.click_view_Link()
        
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()