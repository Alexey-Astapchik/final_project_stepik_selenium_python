from .basket_page_locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_no_products_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_OF_ITEMS), \
            "Products are in cart, but should not be."


    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_CART_EMPTY), \
            "Cart message is not presented, but should not."