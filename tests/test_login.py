from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestLogin:
    def test_successful_login(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL)).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверка кнопки "Разместить объявление"
        create_ad_btn = wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))
        assert create_ad_btn is not None, "Кнопка 'Разместить объявление' не отображается"

        # Проверка аватара
        avatar = wait.until(EC.visibility_of_element_located(AuthLocators.AVATAR))
        assert avatar is not None, "Аватар не отображается"

        # Проверка имени User
        user_name = wait.until(EC.visibility_of_element_located(AuthLocators.USER_NAME))
        assert "User" in user_name.text, f"Имя пользователя: '{user_name.text}', ожидается 'User'"