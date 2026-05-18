# tests/test_create_ad.py
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators

class TestCreateAd:
    def test_create_ad_unauthorized(self, driver):
        driver.find_element(*AuthLocators.CREATE_AD_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        modal = wait.until(EC.visibility_of_element_located(AuthLocators.MODAL_WINDOW_TITLE))
        assert "авторизуйтесь" in modal.text.lower()

    def test_create_ad_authorized_success(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 30)

        unique_title = f"Тест {random.randint(1000, 9999)}"
        unique_price = random.randint(1000, 100000)

        # Клик по кнопке "Разместить объявление" (без element_to_be_clickable, через JS)
        create_btn = wait.until(EC.presence_of_element_located(AuthLocators.CREATE_AD_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", create_btn)

        wait.until(EC.visibility_of_element_located(AuthLocators.NEW_AD_FORM_TITLE))

        title_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_TITLE))
        title_input.clear()
        title_input.send_keys(unique_title)

        desc_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();", desc_input)
        desc_input.clear()
        desc_input.send_keys("Отличное состояние")

        price_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_PRICE))
        price_input.send_keys(str(unique_price))

        publish_btn = wait.until(EC.presence_of_element_located(AuthLocators.AD_PUBLISH_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", publish_btn)

        # Ожидание редиректа или загрузки профиля
        wait.until(EC.url_contains("qa-desk.education-services.ru"))
        driver.get("https://qa-desk.education-services.ru/profile")
        wait.until(EC.visibility_of_element_located(AuthLocators.MY_ADS_TITLE))

        ad_card = wait.until(EC.visibility_of_element_located(
            (By.XPATH, AuthLocators.CREATED_AD_TITLE_TEMPLATE.format(unique_title))))
        assert ad_card is not None, f"Объявление '{unique_title}' не найдено"