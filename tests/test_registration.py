import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from helpers import generate_random_email


class TestRegistration:

    @pytest.fixture(autouse=True)
    def open_registration_form(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL))

    def test_successful_registration(self, driver):
        email = generate_random_email()
        password = "ValidPass123"
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))

    def test_registration_invalid_email(self, driver):
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys("invalid-email")
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        error_msg = wait.until(EC.visibility_of_element_located(AuthLocators.REG_ERROR_MESSAGE))
        assert error_msg.is_displayed()

    def test_registration_existing_user(self, driver):
        # Регистрируем пользователя вручную, чтобы получить существующий email
        email = generate_random_email()
        password = "ValidPass123"

        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))

        # Выходим – ждём появления кнопки "Выйти"
        wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))

        # Снова открываем форму регистрации и пытаемся зарегистрировать того же пользователя
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        driver.find_element(*AuthLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        error_msg = wait.until(EC.visibility_of_element_located(AuthLocators.REG_ERROR_MESSAGE))
        assert error_msg.is_displayed()