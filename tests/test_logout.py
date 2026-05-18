from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from locators import AuthLocators

class TestLogout:
    def test_logout(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)
        # Повторная попытка клика по кнопке "Выйти"
        for _ in range(3):
            try:
                wait.until(EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
                break
            except StaleElementReferenceException:
                continue
        login_btn = wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_REG_BUTTON))
        assert login_btn.is_displayed()