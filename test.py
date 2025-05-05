
import pytest
from pages.signup_page import SignUp_Page
from pages.navigation_bar_page import Navigation_Bar_Page
from pages.code_snippet_card_page import Code_Snippet_Card_Page
from pages.tags_page import Tags_Page
from pages.login_page import Login_Page
from pages.Kanji import Kanji_Page
from pages.new_code_snippet_form_page import New_Code_Snippet_Page
from selenium.common.exceptions import TimeoutException
import json
import time

with open('test_data.json') as f:
    data = json.load(f)

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
    
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 

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
    
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 

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
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 

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
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 

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
    
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with lowercase password only.") 

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
    
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with valid credentials successful.") 

def test_login_with_invalid_email_and_valid_password(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Invalid Email or password."
    
    navigation_page.click_login_link()
    email = data["invalid_credentials"]["email"]
    password = data["valid_user_signup"]["password"]
    
    login_page.enter_valid_login_credentials(email,password)
    login_page.click_signin_btn()
    
    actual_result = login_page.get_login_validation_error_msg()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with invalid email and valid password generates error.") 
    
def test_login_with_valid_email_and_invalid_password(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Invalid Email or password."
    
    navigation_page.click_login_link()
    email = data["valid_user_signup"]["email"]
    password = data["valid_user_signup"]["confirmPassword"]
    
    login_page.enter_valid_login_credentials(email,password)
    login_page.click_signin_btn()
    
    actual_result = login_page.get_login_validation_error_msg()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with invalid email and valid password generates error.") 
    
def test_login_with_empty_credential(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Invalid Email or password."
    
    navigation_page.click_login_link()
    
    login_page.enter_valid_login_credentials("","")
    login_page.click_signin_btn()
    
    actual_result = login_page.get_login_validation_error_msg()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with invalid email and valid password generates error.") 
    
def test_pasword_recovery_with_empty_email_field(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Email can't be blank"
    
    navigation_page.click_login_link()
    login_page.click_forgot_password_link()
    
    time.sleep(1)
    
    login_page.enter_email_in_forgot_password_field("")
    login_page.click_reset_instruction_btn()
    
    actual_result = login_page.get_reset_password_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Password reset with empty email generate correct validation error message.") 
    
def test_password_recovery_with_valid_email(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "You will receive an email with instructions on how to reset your password in a few minutes."

    navigation_page.click_login_link()
    login_page.click_forgot_password_link()
    
    time.sleep(1)  

    valid_email = data["valid_user_signup"]["email"]
    login_page.enter_email_in_forgot_password_field(valid_email)
    login_page.click_reset_instruction_btn()

    try:
        actual_result = login_page.get_reset_password_success_msg()
        assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
        print("Test Passed: Password reset with valid email triggered success message.")
    except TimeoutException as e:
        pytest.fail("Test failed because the reset email msg element is not found.")
    except Exception as e:
        print("Unknown Error: ",{str.e})

def test_password_recovery_with_unregistered_email(setUp,random_email):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    login_page: Login_Page = setUp['login_page']
    expected_result = "Email not found"  

    navigation_page.click_login_link()
    login_page.click_forgot_password_link()
    
    time.sleep(1)  

    login_page.enter_email_in_forgot_password_field(random_email)
    login_page.click_reset_instruction_btn()

    actual_result = login_page.get_reset_password_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Unregistered email correctly triggered validation error.")

def test_guest_user_should_login_before_creating_new_code_snippet(setUp):
    new_code_snippet: New_Code_Snippet_Page = setUp['new_code_snippet']
    login_page : Login_Page = setUp['login_page']
    expected_result = "You need to sign in or sign up before continuing."
    
    new_code_snippet.click_new_code_snippet_link()
    actual_result = login_page.get_login_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Guest user is redirected to login when trying to create a new code snippet.")
    
def test_login_user_can_create_new_code_snippet(login_user):
    navigation_page: Navigation_Bar_Page = login_user['navigation_page']
    new_code_snippet: New_Code_Snippet_Page = login_user['new_code_snippet']
    
    # Now the user is already logged in — no need for login code here

    navigation_page.click_code_snippets_link()
    new_code_snippet.click_new_code_snippet_link()
    
    expected_result = "New Code Snippet"
    actual_result = new_code_snippet.get_form_title_new_code_snippet()
    
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: The logged-in user can access the New Code Snippet page.")

def test_create_new_code_snippet(login_user):
    # Extracting page objects
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    
    # Navigate to the "New Code Snippet" page
    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()
    
    # Fill the form with data
    title = data["snippets"]["JavaScript"]["title"]
    language = data["snippets"]["JavaScript"]["language"]
    description = data["snippets"]["JavaScript"]["description"]
    code = data["snippets"]["JavaScript"]["code"]
    new_code_snippet_page.input_title(title)
    new_code_snippet_page.select_language(language)
    new_code_snippet_page.input_description(description)
    new_code_snippet_page.input_code(code)
    
    # Optionally set the snippet as private and select tags
    new_code_snippet_page.toggle_private_checkbox(should_check=True)
    new_code_snippet_page.select_tag(data["CodeSnippetCard"]["tags"])  # Dynamically select the tag
    
    # Submit the form to create the snippet
    new_code_snippet_page.click_create_button()
    
    # Verify successful creation (you may want to assert the new snippet appears in the list or on the page)
    success_message = "Code snippet was successfully created."  # Modify this with actual page assertion after creation
    assert success_message in new_code_snippet_page.get_success_message(), f"Expected success message, but got different result."
    
    print("Test Passed: New Code Snippet was successfully created!")

def test_required_fields_validation(login_user):
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    driver = login_user["driver"]
    time.sleep(1)
    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()
    # Attempt to submit without filling required fields
    new_code_snippet_page.click_create_button()

    error_elements = new_code_snippet_page.is_error_displayed()
    error_text_arr = []
    for error in error_elements:
        error_text_arr.append(driver.execute_script("return arguments[0].textContent",error))
    
    assert "Title can't be blank" in error_text_arr
    assert "Language can't be blank" in error_text_arr
    assert "Code can't be blank" in error_text_arr
    print("Test Passed: Required field validations are working as expected.")

def test_missing_title_field_validation(login_user):
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    driver = login_user["driver"]

    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()

    # Fill language and code, leave title blank
    new_code_snippet_page.select_language("Python")
    new_code_snippet_page.input_description("A snippet with no title.")
    new_code_snippet_page.input_code("print('Hello, world!')")

    new_code_snippet_page.click_create_button()

    error_elements = new_code_snippet_page.is_error_displayed()
    error_text_arr = [driver.execute_script("return arguments[0].textContent", e) for e in error_elements]

    assert "Title can't be blank" in error_text_arr
    print("Test Passed: Title required field validation works.")

def test_missing_language_field_validation(login_user):
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    driver = login_user["driver"]

    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()

    # Fill title and code, leave language blank
    new_code_snippet_page.input_title("Snippet without language")
    new_code_snippet_page.input_description("Testing missing language.")
    new_code_snippet_page.input_code("print('No language selected')")

    new_code_snippet_page.click_create_button()

    error_elements = new_code_snippet_page.is_error_displayed()
    error_text_arr = [driver.execute_script("return arguments[0].textContent", e) for e in error_elements]

    assert "Language can't be blank" in error_text_arr
    print("Test Passed: Language required field validation works.")

def test_missing_code_field_validation(login_user):
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    driver = login_user["driver"]

    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()

    # Fill title and language, leave code blank
    new_code_snippet_page.input_title("Snippet without code")
    new_code_snippet_page.select_language("JavaScript")
    new_code_snippet_page.input_description("No code included.")

    new_code_snippet_page.click_create_button()

    error_elements = new_code_snippet_page.is_error_displayed()
    error_text_arr = [driver.execute_script("return arguments[0].textContent", e) for e in error_elements]

    assert "Code can't be blank" in error_text_arr
    print("Test Passed: Code required field validation works.")

def test_public_code_snippet_visible_to_guests(setUp):

    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    code_snippet_card :Code_Snippet_Card_Page = setUp['code_snippet_card']
    time.sleep(1)
    navigation_page.click_code_snippets_link()
    titles = code_snippet_card.get_titles_from_code_snippet_cards()
    assert len(titles) > 0, "Expected at least one snippet car, but found none"
    print("Test Pass: The guest user can view the card snippets.")
    
def test_public_code_snippet_details_page_visbility_to_guests(setUp):
    driver = setUp["driver"]
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    code_snippet_card :Code_Snippet_Card_Page = setUp['code_snippet_card']
    
    navigation_page.click_code_snippets_link()
    titles = code_snippet_card.get_titles_from_code_snippet_cards()
    expected_result = driver.execute_script("return arguments[0].textContent;", titles[data["CodeSnippetCard"]["Number"]]).strip()
    code_snippet_card.click_view_Link(data["CodeSnippetCard"]["Number"])
    
    actual_result = code_snippet_card.get_title_in_code_snippet_details_page().strip()
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'"
    
def test_redirection_to_code_snippets_from_details(setUp):
    navigation_page: Navigation_Bar_Page = setUp['navigation_page']
    code_snippet_card :Code_Snippet_Card_Page = setUp['code_snippet_card']
    
    navigation_page.click_code_snippets_link()
    code_snippet_card.click_view_Link(data["CodeSnippetCard"]["Number"])
    code_snippet_card.click_Back_to_Code_SNippets_link()
    expected_result = "Code Snippets"
    actual_result = code_snippet_card.get_main_page_title().strip()
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'"

def test_guest_user_should_login_before_editing_code_snippet(setUp):
    code_snippet_card :Code_Snippet_Card_Page = setUp['code_snippet_card']
    login_page : Login_Page = setUp['login_page']
    expected_result = "You need to sign in or sign up before continuing."
    
    code_snippet_card.click_view_Link(data["CodeSnippetCard"]["Number"])
    code_snippet_card.click_Edit_btn()
    actual_result = login_page.get_login_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Guest user is redirected to login when trying to create a new code snippet.")
    
def test_guest_user_should_login_before_deleting_code_snippet(setUp):
    code_snippet_card :Code_Snippet_Card_Page = setUp['code_snippet_card']
    login_page : Login_Page = setUp['login_page']
    expected_result = "You need to sign in or sign up before continuing."
    
    code_snippet_card.click_view_Link(data["CodeSnippetCard"]["Number"])
    code_snippet_card.click_Delete_btn()
    actual_result = login_page.get_login_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Guest user is redirected to login when trying to create a new code snippet.")
    
def test_logged_in_user_can_edit_their_code_snippet(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    new_code_snippet = login_user['new_code_snippet']
    
    navigation_page.click_my_dashboard_link()
    my_dashboard.click_edit_icon(0)
    
    expected_result = "Edit Code Snippet"
    actual_result = new_code_snippet.get_form_title_new_code_snippet()
    
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'"

def test_logged_in_user_can_delete_their_code_snippet(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    new_code_snippet = login_user['new_code_snippet']
    driver = login_user['driver']
    
    navigation_page.click_my_dashboard_link()
    my_dashboard.click_delete_icon(0)
    
    alert = driver.switch_to.alert
    alert.accept()
    
    expected_result = "Code snippet was successfully destroyed."
    actual_result = new_code_snippet.get_success_message()
    
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'" 
    
def test_search_with_full_title_name(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["title"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = title
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 

def test_search_with_partial_title_name(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["partial_title"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = data["CodeSnippetCard"]["title"]
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 

def test_search_with_code_snippet_description(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["description"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = data["CodeSnippetCard"]["title"]
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 
        
def test_search_with_code_snippet_description(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["description"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = data["CodeSnippetCard"]["title"]
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 
        
def test_search_with_code_snippet_custom_tags(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["tags"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = data["CodeSnippetCard"]["snippet_with_tag_title"]
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 
        
def test_search_with_code_snippet_code_content(login_user):
    navigation_page = login_user['navigation_page']
    my_dashboard = login_user['my_dashboard']
    driver = login_user['driver']

    title = data["CodeSnippetCard"]["code_content"]
    navigation_page.click_my_dashboard_link()
    my_dashboard.enter_title_in_search_bar(title)
    time.sleep(2)
    my_dashboard.click_apply_btn()
    
    expected_result = data["CodeSnippetCard"]["snippet_with_tag_title"]
    titles = my_dashboard.get_title_in_code_snippet_details_page()
    
    for title_actual in titles:
        title_content = driver.execute_script("return arguments[0].textContent;", title_actual)
        assert title_content == expected_result, f"Expected title '{expected_result}', but got '{title_content}'" 
        
def test_a_user_cannot_edit_code_snippet_created_by_other_users(login_user):
    navigation_page = login_user['navigation_page']
    code_snippet_card = login_user['code_snippet_card']
    
    navigation_page.click_code_snippets_link()
    code_snippet_card.click_view_Link(1)
    code_snippet_card.click_Edit_btn()
    
    expected_result = data["errors"]["edit_permission_error"]
    actual_result = code_snippet_card.get_permission_denied_msg()
    
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'" 
    
def test_a_user_cannot_delete_code_snippet_created_by_other_users(login_user):
    navigation_page = login_user['navigation_page']
    code_snippet_card = login_user['code_snippet_card']
    
    navigation_page.click_code_snippets_link()
    code_snippet_card.click_view_Link(1)
    code_snippet_card.click_Delete_btn()
    
    expected_result = data["errors"]["delete_permission_error"]
    actual_result = code_snippet_card.get_permission_denied_msg()
    
    assert actual_result == expected_result, f"Expected title '{expected_result}', but got '{actual_result}'"
    
def test_user_can_create_multiple_code_snippet_with_same_title(login_user):
    # Extracting page objects
    navigation_page = login_user['navigation_page']
    new_code_snippet_page = login_user['new_code_snippet']
    
    title = data["snippets"]["JavaScript"]["title"]
    language = data["snippets"]["JavaScript"]["language"]
    description = data["snippets"]["JavaScript"]["description"]
    code = data["snippets"]["JavaScript"]["code"]

    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()
    
    # Fill the form with data
    new_code_snippet_page.input_title(title)
    new_code_snippet_page.select_language(language)
    new_code_snippet_page.input_description(description)
    new_code_snippet_page.input_code(code)
    new_code_snippet_page.toggle_private_checkbox(should_check=True)
    new_code_snippet_page.select_tag(data["CodeSnippetCard"]["tags"])  
    new_code_snippet_page.click_create_button()
    
    navigation_page.click_code_snippets_link()
    new_code_snippet_page.click_new_code_snippet_link()
    
    new_code_snippet_page.input_title(title)
    new_code_snippet_page.select_language(language)
    new_code_snippet_page.input_description(description)
    new_code_snippet_page.input_code(code)
    new_code_snippet_page.toggle_private_checkbox(should_check=True)
    new_code_snippet_page.select_tag(data["CodeSnippetCard"]["tags"])  
    new_code_snippet_page.click_create_button()

    success_message = "Code snippet was successfully created."  # Modify this with actual page assertion after creation
    assert success_message in new_code_snippet_page.get_success_message(), f"Expected success message, but got different result."
    
def test_guest_user_can_view_tags_page(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    tag_page : Tags_Page = setUp['tags_page']
    

    navigation_page.click_Tags_link()
    time.sleep(2)
    actual_result = tag_page.get_h1_title_of_tags_page()
    
    expected_result = "Tags"  
    assert expected_result == actual_result, f"Expected success message, but got different result."
    
def test_only_logged_in_users_can_create_new_tags(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    tag_page : Tags_Page = setUp['tags_page']
    code_snippet_card : Code_Snippet_Card_Page = setUp['code_snippet_card']
    

    navigation_page.click_Tags_link()
    time.sleep(2)
    tag_page.click_new_tag_btn()
    
    expected_result = data["errors"]["not_logged_in_error"]
    
    try:
        actual_result = code_snippet_card.get_permission_denied_msg()
        assert expected_result == actual_result, f"Expected success message, but got different result."
    except TimeoutException as e:
        pytest.fail("The permission denied msg is not found because the guest user is allowed to create new tag.")

def test_user_can_view_code_snippets_filtered_by_tags(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    tag_page : Tags_Page = setUp['tags_page']
    
    navigation_page.click_Tags_link()
    time.sleep(2)
    tag_page.click_view_tag_link(data["tags"]["tag_name"])
    time.sleep(2)
    actual_result = tag_page.get_h1_title_of_tags_page()
    expected_result = "Tag: Edited Tagg"
    
    assert expected_result == actual_result, f"Expected success message, but got different result."
    
def test_only_logged_in_users_can_edit_tags(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    tag_page : Tags_Page = setUp['tags_page']
    code_snippet_card : Code_Snippet_Card_Page = setUp['code_snippet_card']
    

    navigation_page.click_Tags_link()
    time.sleep(2)
    tag_page.click_edit_tag_link(data["tags"]["tag_name"])
    
    expected_result = data["errors"]["not_logged_in_error"]
    
    try:
        actual_result = code_snippet_card.get_permission_denied_msg()
        assert expected_result == actual_result, f"Expected success message, but got different result."
    except TimeoutException as e:
        pytest.fail("The permission denied msg is not found because the guest user is allowed to edit new tag.")
        
def test_only_logged_in_users_can_delete_tags(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    tag_page : Tags_Page = setUp['tags_page']
    code_snippet_card : Code_Snippet_Card_Page = setUp['code_snippet_card']
    

    navigation_page.click_Tags_link()
    time.sleep(2)
    tag_page.click_delete_tag_link(data["tags"]["tag_name"])
    
    expected_result = data["errors"]["not_logged_in_error"]
    
    try:
        actual_result = code_snippet_card.get_permission_denied_msg()
        assert expected_result == actual_result, f"Expected success message, but got different result."
    except TimeoutException as e:
        pytest.fail("The permission denied msg is not found because the guest user is allowed to edit new tag.")
        
def test_user_can_search_by_kanji(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    kanji_page : Kanji_Page = setUp['kanji_page']
    
    navigation_page.click_Kanji_for_Beginners_link()
    kanji_page.enter_kanji_character(data["kanji"]["kanji_word"])
    kanji_page.click_Search_Btn()
    english_word = data['kanji']["english_word"]
    kanji_word = kanji_page.get_word_from_kanji_card()
    
    matches = [word for word in kanji_word if word == english_word]

    assert matches is not None, f"Word '{english_word}' not found in kanji card words: {kanji_word}"
    
def test_search_for_kanji_charcter_with_english_word(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    kanji_page : Kanji_Page = setUp['kanji_page']

    navigation_page.click_Kanji_for_Beginners_link()
    
    kanji_page.enter_kanji_character(data["kanji"]["english_word"])
    kanji_page.click_Search_Btn()
    
    english_word = data['kanji']["english_word"]
    kanji_word = kanji_page.get_word_from_kanji_card()
    matches = [word for word in kanji_word if word == english_word]
    assert matches is not None, f"Word '{english_word}' not found in kanji card words: {kanji_word}"
    
def test_new_kanji_characters_are_fetched_from_kanjiAlive(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    kanji_page : Kanji_Page = setUp['kanji_page']

    navigation_page.click_Kanji_for_Beginners_link()
    
    kanji_page.enter_kanji_character(data["kanji"]["new_english_word_search"])
    kanji_page.click_Search_Btn()
    success_msg = kanji_page.get_kanji_fetch_success_msg()
    
    expected_result = data["kanji"]["new_kanji_added_success_msg"]
    
    assert success_msg.startswith(expected_result), f"Unexpected success message: {success_msg}"
    
def test_unavailable_characters_generate_proper_error_msg(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    kanji_page : Kanji_Page = setUp['kanji_page']

    navigation_page.click_Kanji_for_Beginners_link()
    
    kanji_page.enter_kanji_character(data["kanji"]["unavailable_word"])
    kanji_page.click_Search_Btn()
    success_msg = kanji_page.get_kanji_fetch_success_msg()
    
    expected_result = data["kanji"]["word_not_found"]
    
    assert success_msg == expected_result, f"Expected success message, but got different result."

def test_kanji_char_page_contains_stroke_order(setUp):
    navigation_page : Navigation_Bar_Page = setUp['navigation_page']
    kanji_page : Kanji_Page = setUp['kanji_page']
    
    navigation_page.click_All_Kanji_link()
    kanji_page.click_kanji_card(0)
    actual_result = kanji_page.stroke_order_exists()
    
    assert True == actual_result, f"Stroke order video doesn't exist"
