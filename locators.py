from selenium.webdriver.common.by import By

class Locators:
    
    # code snippet cards
    SNIPPET_CARDS = (By.CSS_SELECTOR,'div.bg-white.shadow-md.rounded-lg.overflow-hidden.border.border-gray-200')
    VIEW_LINKS = (By.XPATH,'(//a[contains(text(), "View")])[1]')
    EDIT_LINKS = (By.XPATH,'//a[contains(text(),"Edit")]')
    DELETE_LINKS = (By.XPATH,'//a[contains(text(),"Delete")]')
    SNIPPET_CREATOR = (By.CSS_SELECTOR,'span.text-gray-500.text-xs')
    CUSTOM_TAGS = (By.CSS_SELECTOR,'a.bg-blue-100.rounded-full.text-blue-700')
    
    # NavBar Links
    CODE_NOTES = (By.XPATH,'//a[contains(text(),"Code Notes")]')
    CODE_SNIPPETS = (By.XPATH,'//a[contains(text(),"Code Snippets")]')
    MY_DASHBOARD = (By.XPATH,'//a[contains(text(),"My Dashboard")]')
    TAGS = (By.XPATH,'//a[contains(text(),"Tags")]')
    KANJI_FOR_BEGINEERS = (By.XPATH,'//a[contains(text(),"Kanji for Beginners")]')
    ALL_KANJI = (By.XPATH,'//a[contains(text(),"All Kanji")]')
    LOGIN =(By.XPATH,'//a[contains(text(),"Login")]')
    SIGN_UP = (By.XPATH,'//a[contains(text(),"Sign Up")]')
    LOG_OUT = (By.XPATH,'//a[contains(text(),"Logout")]')
    
    # New code snippet
    NEW_CODE_SNIPPET = (By.CSS_SELECTOR,'a[href="/code_snippets/new"]')
    INPUT_TITLE = (By.ID,'code_snippet_title')
    INPUT_LANGUAGE = (By.ID,'code_snippet_language')
    INPUT_DESCRIPTION = (By.ID,'code_snippet_description')
    INPUT_CODE = (By.ID,'code_snippet_code')
    INPUT_PRIVATE = (By.XPATH,'//label[@for="code_snippet_private"]')
    INPUT_TAGS = (By.XPATH,'//input[@type="checkbox" and @name="code_snippet[tag_ids][]"]/following-sibling::label')
    CREATE_BTN = (By.XPATH,'//input[@type="submit" and @name="commit"]')
    MANAGE_TAG_LINK = (By.XPATH,'//a[contains(text(),"Manage Tags")]')
    
    # sign up and sign up validation
    INPUT_EMAIL_SIGNUP = (By.ID,'user_email')
    INPUT_PASSWORD_SIGNUP = (By.ID,'user_password')
    INPUT_CONFIRM_PASSWORD_SIGNUP = (By.ID,'user_password_confirmation')
    SIGN_UP_BTN = (By.XPATH,'//input[@data-disable-with]')
    SIGN_IN_LINK = (By.XPATH,'//a[contains(text(),"Sign in")]')
    VALIDATION = (By.CSS_SELECTOR,'div.bg-red-100.border.border-red-400.text-red-700')
    VALIDATION_ERROR_MSGS = (By.CSS_SELECTOR,'p.mt-2.text-red-500.text-sm') # this can be a single or multiple elements later it will be defined in page Object
    SUCCESSFUL_SIGNUP_MSG = (By.CSS_SELECTOR,'span.block.sm\\:inline')
    
    # login and login validation
    INPUT_EMAIL_LOGIN = (By.ID,'user_email')
    INPUT_PASSWORD_LOGIN = (By.ID,'user_password')
    REMEMBER_ME = (By.XPATH,'//input[@type="checkbox" and @name="user[remember_me]"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR,'a[href="/users/password/new"')
    SIGN_IN_BTN = (By.XPATH,'//input[@type="submit" and @name="commit" and @value="Sign in"]')
    SIGN_UP_LINK = (By.XPATH,'//a[contains(text(),"Sign up")]')
    VALIDATION_LOGIN = (By.CSS_SELECTOR,'span.block.sm\\:inline')
    RESET_INSTRUCTION = (By.XPATH,'//input[@data-disable-with]')
    RESET_VALIDATION = (By.XPATH,'//input[@id="user_email"]/following-sibling::p[1]')
    VALID_RESET_MSG = (By.XPATH,'//input[@id="user_email"]/following-sibling::p[1]')
    
    # create, edit code snippet
    FORM_TITLE = (By.CSS_SELECTOR,'h1.xh-highlight')
    
   