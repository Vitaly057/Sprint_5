from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators

class TestLogout:

    def test_logout(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)
        # Кнопка "Выйти" видна сразу
        wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
        login_btn = wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))
        assert login_btn.is_displayed()