from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main>h1')
    TITLE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    ITEM_PRICE_ON_CART = (By.CSS_SELECTOR, '.hidden-xs')
    QUANTITY_OF_ITEMS = (By.CSS_SELECTOR, '#id_form-0-quantity')
    MESSAGE_CART_EMPTY = (By.CSS_SELECTOR,'#content_inner')