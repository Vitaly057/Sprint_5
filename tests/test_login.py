from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from helpers import generate_random_email


class TestLogin:

    def test_successful_login(self, driver):
        wait = WebDriverWait(driver, 10)
        email = generate_random_email()
        password = "ValidPass123"

        # Регистрация
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))

        # Выход (кнопка видна сразу)
        wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))

        # Логин с теми же данными
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL)).send_keys(email)
        driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.LOGIN_SUBMIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))