from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.common.exceptions import TimeoutException



class Kanji_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        
    def click_Search_Btn(self):
        search_btn = self.wait.until(EC.presence_of_element_located(Locators.SEARCH_KANJI_BTN))
        self.driver.execute_script('arguments[0].click();', search_btn)
        
    def enter_kanji_character(self,kanjiChar):
        kanji_char = self.wait.until(EC.presence_of_element_located(Locators.SEARCH_BAR_KANJI))
        self.driver.execute_script("arguments[0].value = arguments[1];", kanji_char, kanjiChar)
        
    def get_word_from_kanji_card(self):
        kanji_card_word = self.wait.until(EC.presence_of_all_elements_located(Locators.KANJI_CARD))
        return kanji_card_word
    
    def get_kanji_fetch_success_msg(self):
        success_msg = self.wait.until(EC.presence_of_element_located(Locators.SUCCESS_MSG))
        text = self.driver.execute_script("return arguments[0].textContent",success_msg)
        return text

    def click_kanji_card(self,cardNumber):
        # Get all kanji cards and their child word elements
        kanji_cards = self.wait.until(EC.presence_of_all_elements_located(Locators.KANJI_CARD))
        self.driver.execute_script('arguments[0].click();', kanji_cards[cardNumber])

    
    def stroke_order_exists(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.STROKE_ORDER))
            return True
        except TimeoutException:
            return False


