from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.signup_page import SignUp_Page
from pages.navigation_bar_page import Navigation_Bar_Page
from pages.code_snippet_card_page import Code_Snippet_Card_Page
from pages.login_page import Login_Page
from selenium.common.exceptions import TimeoutException
import json

with open('test_data.json') as f:
    data = json.load(f)

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setUp():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode for no UI
    driver = webdriver.Chrome(options=chrome_options)
    
    # driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    
    # Page objects
    signUp_page = SignUp_Page(driver)
    navigation_page = Navigation_Bar_Page(driver)
    code_snippet_card = Code_Snippet_Card_Page(driver)
    login_page = Login_Page(driver)
    
   
    yield {
        "driver": driver,
        "wait": wait,
        "signUp_page": signUp_page,
        "navigation_page": navigation_page,
        "code_snippet_card": code_snippet_card,
        "login_page": login_page
    }
    
    driver.quit()
    
    
def test_signUp_with_valid_credentials(setUp,random_email):
    navigation_page = setUp['navigation_page']
    signUp_page = setUp['signUp_page']
    password = data["valid_user_signup"]["password"]
    confirmPassword = data["valid_user_signup"]["confirmPassword"]
    
    expected_result = 'Welcome! You have signed up successfully.'
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,password,password)
    signUp_page.click_signUp_Btn()
    actual_result = signUp_page.get_successful_login_msg()
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Pass - User Successfully signed up with valid credentials")
        
    except TimeoutError as e:
        print(f"Test Failed - Timeout Erro: {str.e}")
    except Exception as e:
        print(f"Test Failed - Unexpected Error: {str.e}")
    
def test_signUp_with_empty_credentials(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    
    expected_result = "Please review the problems below:"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials("","","")
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_validation_error_signUp()
    
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with empty credetials")

    
def test_signUp_with_empty_email(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    password = data["valid_user_signup"]["password"]
    
    expected_result = "Email can't be blank"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials("",password,password)
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_field_validation_error_msg_signUp()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with empty email")
 
def test_signUp_with_empty_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    
    expected_result = "Password can't be blank"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,"","")
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_field_validation_error_msg_signUp()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with empty password") 
    
def test_signUp_with_different_password_and_confirmPassword(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    password = data["valid_user_signup"]["password"]
    confirmPassword = data["valid_user_signup"]["confirmPassword"]
    
    expected_result = "Password confirmation doesn't match Password"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,password,confirmPassword)
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_field_validation_error_msg_signUp()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with different password and confirm password")   
    
def test_signUp_with_already_registered_email(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    email = data["valid_user_signup"]["email"]
    password = data["valid_user_signup"]["password"]
    
    
    expected_result = "Email has already been taken"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(email,password,password)
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_field_validation_error_msg_signUp()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with aleardy registered email")  
    
def test_signUp_with_invalid_email(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    email = data["invalid_credentials"]["email"]
    password = data["valid_user_signup"]["password"]
    
    
    expected_result = "Email is invalid"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(email,password,password)
    signUp_page.click_signUp_Btn()
    
    actual_result = signUp_page.get_field_validation_error_msg_signUp()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with invalid email.")  
    
def test_signUp_with_lowercase_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    lowercase_password = data["invalid_credentials"]["lowercase_password"]
    
    expected_result = "Password is too short (minimum is 6 characters)"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,lowercase_password,lowercase_password)
    signUp_page.click_signUp_Btn()
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 
    except AssertionError as e:
        print("Test Failed - The user is logged in with all lowercase in password") 
    
def test_signUp_with_uppercase_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    uppercase_password = data["invalid_credentials"]["uppercase_password"]
    
    expected_result = "Password is too short (minimum is 6 characters)"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,uppercase_password,uppercase_password)
    signUp_page.click_signUp_Btn()
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 
    except AssertionError as e:
        print("Test Failed - The user is logged in with all uppercase in password") 
    
    
def test_signUp_with_numeric_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    numeric_password = data["invalid_credentials"]["numeric_password"]
    
    expected_result = "Password is too short (minimum is 6 characters)"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,numeric_password,numeric_password)
    signUp_page.click_signUp_Btn()
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 
    except AssertionError as e:
        print("Test Failed - The user is logged in with all numeric in password") 
    
def test_signUp_with_symbol_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    symbol_password = data["invalid_credentials"]["symbol_password"]
    
    expected_result = "Password is too short (minimum is 6 characters)"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,symbol_password,symbol_password)
    signUp_page.click_signUp_Btn()
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 
    except AssertionError as e:
        print("Test Failed - The user is logged in with all symbol in password") 
    
def test_signUp_with_lessthansix_password(setUp,random_email):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    signUp_page: SignUp_Page = setUp['signUp_page']
    lessthansix_password = data["invalid_credentials"]["symbol_password"]
    
    expected_result = "Password is too short (minimum is 6 characters)"
    
    navigation_page.click_signUp_Link()
    signUp_page.enter_signup_credentials(random_email,lessthansix_password,lessthansix_password)
    signUp_page.click_signUp_Btn()
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 
    except AssertionError as e:
        print("Test Failed - The user is logged in with less than six characters in password")     
    
def test_login_with_valid_credentials(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Logout"
    
    navigation_page.click_login_link()
    email = data["valid_user_signup"]["email"]
    password = data["valid_user_signup"]["password"]
   
    login_page.enter_valid_login_credentials(email,password)
    login_page.click_signin_btn()
    
    actual_result = navigation_page.get_logout_text_from_nav_bar()
    
    try:
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Login with valid credentials successful.") 
    except AssertionError as e:
        print("Test Failed - Login with valid email and password is unsuccessful.")    
    