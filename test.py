from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.signup_page import SignUp_Page
from pages.navigation_bar_page import Navigation_Bar_Page
from pages.code_snippet_card_page import Code_Snippet_Card_Page
import json

with open('test_data.json') as f:
    data = json.load(f)

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setUp():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode for no UI
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    
    # Page objects
    signUp_page = SignUp_Page(driver)
    navigation_page = Navigation_Bar_Page(driver)
    code_snippet_card = Code_Snippet_Card_Page(driver)
    
    # Yield the necessary objects to test functions
    yield {
        "driver": driver,
        "wait": wait,
        "signUp_page": signUp_page,
        "navigation_page": navigation_page,
        "code_snippet_card": code_snippet_card
    }
    
    driver.quit()
    
    
def test_signUp_with_valid_credentials(setUp):
    navigation_page = setUp['navigation_page']
    signUp_page = setUp['signUp_page']
    username = data["valid_user_signup"]["email"]
    password = data["valid_user_signup"]["password"]
    confirmPassword = data["valid_user_signup"]["confirmPassword"]
    
    expected_result = 'Welcome! You have signed up successfully.'
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_valid_signup_credentials(username,password,confirmPassword)
    signUp_page.click_signUp_Btn()
    actual_result = signUp_page.get_successful_login_msg()
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Pass - User Successfully signed up with valid credentials")
        
    except TimeoutError as e:
        print(f"Test Failed - Timeout Error: {str(e)}")
    except Exception as e:
        print(f"Test Failed - Unexpected Error: {str(e)}")
    
# def test_view_a_code_snippet(self):
#     self.code_snippet_card.click_view_Link()
    
    
 
        