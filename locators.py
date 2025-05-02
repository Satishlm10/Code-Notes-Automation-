from selenium.webdriver.common.by import By

class Locators:
    
    # code snippet cards
    SNIPPET_CARDS = (By.CSS_SELECTOR,'div.bg-white.shadow-md.rounded-lg.overflow-hidden.border.border-gray-200')
    SNIPPET_CARDS_TITLE = (By.CSS_SELECTOR,'div.bg-white.shadow-md.rounded-lg div.px-6.py-4 > div.font-bold.text-xl.mb-2')
    VIEW_LINKS = (By.XPATH,'(//a[contains(text(), "View")])')
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
    SUCCESS_MSG = (By.CSS_SELECTOR,'span.block.sm\\:inline')

    # Select options for languages in the dropdown
    LANGUAGE_OPTIONS = {
        "JavaScript": (By.XPATH, "//option[text()='JavaScript']"),
        "Ruby": (By.XPATH, "//option[text()='Ruby']"),
        "Python": (By.XPATH, "//option[text()='Python']"),
        "Java": (By.XPATH, "//option[text()='Java']"),
        "C#": (By.XPATH, "//option[text()='C#']"),
        "PHP": (By.XPATH, "//option[text()='PHP']"),
        "Go": (By.XPATH, "//option[text()='Go']"),
        "Swift": (By.XPATH, "//option[text()='Swift']"),
        "Kotlin": (By.XPATH, "//option[text()='Kotlin']"),
        "TypeScript": (By.XPATH, "//option[text()='TypeScript']"),
        "HTML": (By.XPATH, "//option[text()='HTML']"),
        "CSS": (By.XPATH, "//option[text()='CSS']"),
        "SQL": (By.XPATH, "//option[text()='SQL']"),
        "Shell": (By.XPATH, "//option[text()='Shell']"),
        "Other": (By.XPATH, "//option[text()='Other']")
    }
    
    TAG_CHECKBOX = (By.XPATH, "//label[text()='{tag_name}']/preceding-sibling::input")
    @staticmethod
    def get_tag_checkbox_locator(tag_name):
        """Returns the XPath for the tag checkbox, replacing the tag_name placeholder."""
        return Locators.TAG_CHECKBOX[0], Locators.TAG_CHECKBOX[1].format(tag_name=tag_name)
    
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
    FORM_TITLE = (By.CSS_SELECTOR,'h1.font-bold.text-3xl')
    
    
    # code snippet details page
    H1_TITLE = (By.CSS_SELECTOR,'h1.font-bold.text-3xl')
    BACK_CODE_SNIPPET = (By.CSS_SELECTOR,'div.mb-6 > a.text-blue-500')
    H1_MAIN_PAGE_TITLE = (By.CSS_SELECTOR,'h1.font-bold.text-4xl')
    DETAILS_EDIT_BTN = (By.CSS_SELECTOR,'a.bg-yellow-500.font-bold')
    DETAILS_DELETE_BTN = (By.CSS_SELECTOR,'form > input.bg-red-500[value="Delete"]')
    PERMISSION_ERROR = (By.CSS_SELECTOR,'div[role="alert"] > span.block.sm\\:inline')
    
    # My dashboard locators
    EDIT_ICON = (By.CSS_SELECTOR,'a.text-gray-400.hover\\:text-gray-600')
    DELETE_ICON = (By.CSS_SELECTOR,'form > button[type="submit"]')
    SEARCH_BAR = (By.CSS_SELECTOR,'input[placeholder="Search snippets..."]')
    SEARCH_FORM = (By.CSS_SELECTOR,'form[action="/dashboard"]')
    LANGUAGE_SELECT = (By.CSS_SELECTOR,'select[id=language]')
    SORT_SNIPPETS = (By.CSS_SELECTOR,'select[id="sort"]')
    APPLY_BTN = (By.CSS_SELECTOR,'input[type="submit"]')
    TITLES_IN_CODE_SNIPPET_MY_DASHBOARD = (By.CSS_SELECTOR,'h3 > a.hover\\:text-blue-600')
    
    # Tags Page
    TAG_PAGE_TITLE = (By.CSS_SELECTOR,'h1.font-bold')
    TAG_TD_BLOCK = (By.CSS_SELECTOR,'tr')
    NEW_TAG_BTN = (By.CSS_SELECTOR,'div > a.bg-blue-500.text-white.font-bold')
    VIEW_TAGS = (By.CSS_SELECTOR,'tr > td > a.text-blue-500')
    EDIT_TAGS = (By.CSS_SELECTOR,'tr > td > a.text-yellow-500')
    DELETE_TAGS = (By.CSS_SELECTOR,'input[value="Delete"].text-red-500')