from .base_page import BasePage
from .product_page_locators import ProductPageLocators
from .main_page_locators import MainPageLocators

class ProductPage(BasePage):

    def add_item_to_cart(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_cart_button.click()

    def verify_item_price_after_adding_to_cart(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_price_text = item_price.text
        item_price_presented_in_cart = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_CART)
        item_price_presented_in_cart_text = item_price_presented_in_cart.text
        assert item_price_text in item_price_presented_in_cart_text

    def should_be_success_message(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title_text = book_title.text
        success_message_title = self.browser.find_element(*ProductPageLocators.TITLE_IN_SUCCESS_MESSAGE)
        success_message_title_text = success_message_title.text
        assert book_title_text == success_message_title_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."

    def should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."

    def should_be_no_products_in_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.QUANTITY_OF_ITEMS), \
            "Products are in cart presented, but should not be."

    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CART_EMPTY), \
            "Cart message is not presented, but should not."

    def guest_open_cart_from_product_page(self):
        go_to_cart_button = self.wait_button_to_be_clickable(*MainPageLocators.GO_TO_CART_BUTTON)
        go_to_cart_button.click()