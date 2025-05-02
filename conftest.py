# conftest.py
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest
import random
import string
import json

import time

with open('test_data.json') as f:
    data = json.load(f)

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "test.com"
    return f"{username}@{domain}"

@pytest.fixture
def random_email():
    return generate_random_email()


from pages.signup_page import SignUp_Page
from pages.navigation_bar_page import Navigation_Bar_Page
from pages.code_snippet_card_page import Code_Snippet_Card_Page
from pages.login_page import Login_Page
from pages.new_code_snippet_form_page import New_Code_Snippet_Page
from pages.my_dashboard import My_Dashboard_Page

@pytest.fixture(scope="function")
def setUp():
    # chrome_options = Options()
    # chrome_options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=chrome_options)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    
    # Page objects
    signUp_page = SignUp_Page(driver)
    navigation_page = Navigation_Bar_Page(driver)
    code_snippet_card = Code_Snippet_Card_Page(driver)
    login_page = Login_Page(driver)
    new_code_snippet = New_Code_Snippet_Page(driver)
    my_dashboard = My_Dashboard_Page(driver)
    

    yield {
        "driver": driver,
        "wait": wait,
        "signUp_page": signUp_page,
        "navigation_page": navigation_page,
        "code_snippet_card": code_snippet_card,
        "login_page": login_page,
        "new_code_snippet": new_code_snippet,
        "my_dashboard": my_dashboard
    }
    
    driver.quit()
    
@pytest.fixture()
def login_user(setUp):
    driver = setUp['driver']
    login_page = setUp['login_page']
    navigation_page = setUp['navigation_page']
    new_code_snippet = setUp['new_code_snippet']
    my_dashboard = setUp['my_dashboard']
    code_snippet_card = setUp['code_snippet_card']
    
    
    email = data["valid_user_signup"]["email"]
    password = data["valid_user_signup"]["password"]
    
    navigation_page.click_login_link()
    login_page.enter_valid_login_credentials(email,password)
    login_page.click_signin_btn()
    time.sleep(3)
    
    yield setUp
    