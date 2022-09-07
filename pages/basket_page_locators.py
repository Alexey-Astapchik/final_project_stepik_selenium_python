from selenium.webdriver.common.by import By

class BasketPageLocators():
    QUANTITY_OF_ITEMS = (By.CSS_SELECTOR, '#id_form-0-quantity')
    MESSAGE_CART_EMPTY = (By.CSS_SELECTOR, '#content_inner')