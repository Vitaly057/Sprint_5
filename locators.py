from selenium.webdriver.common.by import By

class AuthLocators:
    # Кнопки на главной
    LOGIN_REG_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    AVATAR = (By.CLASS_NAME, "circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")

    # Форма регистрации
    REG_EMAIL = (By.NAME, "email")
    REG_PASSWORD = (By.NAME, "password")
    REG_REPEAT_PASSWORD = (By.NAME, "submitPassword")
    REG_CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")

    # Ошибки регистрации
    REG_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(),'Ошибка') or contains(@class,'error')]")
    RED_BORDER_EMAIL = (By.CSS_SELECTOR, "input[name='email'].error")
    RED_BORDER_PASSWORD = (By.CSS_SELECTOR, "input[name='password'].error")
    RED_BORDER_REPEAT = (By.CSS_SELECTOR, "input[name='submitPassword'].error")

    # Форма логина
    LOGIN_EMAIL = (By.NAME, "email")
    LOGIN_PASSWORD = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    # Модальное окно для неавторизованного
    MODAL_WINDOW_TITLE = (By.XPATH, "//h1[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]")

    # Форма создания объявления
    AD_TITLE = (By.NAME, "name")
    AD_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    AD_PRICE = (By.NAME, "price")
    AD_CATEGORY = (By.NAME, "category")
    AD_CITY = (By.NAME, "city")
    AD_PUBLISH_BUTTON = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText[type='submit']")
    AD_CONDITION_NEW = (By.XPATH, "//label[text()='Новый']")
    AD_CONDITION_USED = (By.XPATH, "//label[text()='Б/У']")

    # Профиль
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Мои объявления')]")
    MY_ADS_BLOCK = (By.XPATH, "//h1[contains(text(),'Мои объявления')]")