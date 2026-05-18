from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from helpers import generate_random_email

class TestRegistration:

    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL))

        email = generate_random_email()
        password = "ValidPass123"
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()

        create_ad_btn = wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))
        assert create_ad_btn is not None, "Кнопка 'Разместить объявление' не отображается после регистрации"

    def test_registration_invalid_email(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL))

        driver.find_element(*AuthLocators.REG_EMAIL).send_keys("invalid-email")
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        error_msg = wait.until(EC.visibility_of_element_located(AuthLocators.REG_ERROR_MESSAGE))
        assert error_msg is not None, "Сообщение об ошибке не появилось"

    def test_registration_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL))

        email = generate_random_email()
        password = "ValidPass123"
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))

        # Выход
        wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))

        # Попытка повторной регистрации
        driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.REG_EMAIL))
        driver.find_element(*AuthLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*AuthLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_REPEAT_PASSWORD).send_keys(password)
        driver.find_element(*AuthLocators.REG_CREATE_BUTTON).click()
        error_msg = wait.until(EC.visibility_of_element_located(AuthLocators.REG_ERROR_MESSAGE))
        assert error_msg is not None, "Сообщение об ошибке не появилось"