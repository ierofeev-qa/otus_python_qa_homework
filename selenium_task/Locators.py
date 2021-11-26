from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_ICONS = (By.CSS_SELECTOR, '[id="top-links"]')
    NAVBAR = (By.CSS_SELECTOR, '[class="navbar"]')
    SEARCH_ITEM = (By.CSS_SELECTOR, '[id="search"]')
    CART_BUTTON = (By.CSS_SELECTOR, '[id="cart"]')
    FOOTER = (By.CSS_SELECTOR, 'footer [class="container"]')


class CatalogPageLocators:
    GROUP_LIST = (By.CSS_SELECTOR, '[class="list-group"]')
    SORT_INPUT = (By.CSS_SELECTOR, '[id="input-sort"]')
    LIMIT_INPUT = (By.CSS_SELECTOR, '[id="input-limit"]')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="list-view"]')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '[id="grid-view"]')


class ProductPageLocators:
    PRODUCT_IMAGES = (By.CSS_SELECTOR, '[class="thumbnails"]')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id="button-cart"]')
    DESCRIPTION_TAB = (By.CSS_SELECTOR, '[id="tab-description"]')
    REVIEW_TAB = (By.CSS_SELECTOR, '[id="tab-review"]')
    RATING_BUTTONS = (By.CSS_SELECTOR, '[class="rating"]')


class AdminLoginPageLocators:
    HEADER = (By.CSS_SELECTOR, '[class="navbar-header"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id="input-username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    HELP_BLOCK = (By.CSS_SELECTOR, '[class="help-block"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-primary"]')


class RegistrationPageLocators:
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-firstname"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '[id="input-lastname"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[id="input-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="input-password"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
