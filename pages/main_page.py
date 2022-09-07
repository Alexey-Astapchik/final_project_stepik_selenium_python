from .base_page import BasePage
from .main_page_locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def guest_open_cart_from_main_page(self):
        go_to_cart_button = self.wait_button_to_be_clickable(*MainPageLocators.GO_TO_CART_BUTTON)
        go_to_cart_button.click()
