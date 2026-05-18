import random
import time
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

        # Клик с повторной попыткой
        for _ in range(3):
            try:
                create_btn = wait.until(EC.presence_of_element_located(AuthLocators.CREATE_AD_BUTTON))
                driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
                wait.until(EC.element_to_be_clickable(AuthLocators.CREATE_AD_BUTTON)).click()
                break
            except:
                continue

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Новое объявление')]")))

        # Заполнение
        title_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_TITLE))
        title_input.clear()
        title_input.send_keys(unique_title)

        # Описание товара
        desc_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_DESCRIPTION))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", desc_input)
        desc_input.click()  # фокусируем поле
        desc_input.clear()  # очищаем (на всякий случай)
        desc_input.send_keys("Отличное состояние")

        price_input = wait.until(EC.presence_of_element_located(AuthLocators.AD_PRICE))
        price_input.send_keys(str(unique_price))

        # Публикация
        publish_btn = wait.until(EC.element_to_be_clickable(AuthLocators.AD_PUBLISH_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView(true);", publish_btn)
        publish_btn.click()

        # Проверка успешности публикации
        wait.until(EC.url_contains("qa-desk.education-services.ru"))

        # Переход в профиль
        driver.get("https://qa-desk.education-services.ru/profile")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Мои объявления')]")))

        # Ожидание появления хотя бы одной карточки (чтобы убедиться, что страница загружена)
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ad-card')] | //h3[@class='h3']")))

        # Поиск объявления на всех страницах
        ad_card = None
        for page in range(1, 6):
            try:
                ad_card = driver.find_element(By.XPATH, f"//h2[@class='h2' and contains(text(),'{unique_title}')]")
                if ad_card.is_displayed():
                    break
            except:
                try:
                    next_btn = driver.find_element(By.XPATH, "//button[contains(@class,'arrowButton--right')]")
                    driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
                    next_btn.click()
                    time.sleep(1)
                except:
                    break

        assert ad_card is not None and ad_card.is_displayed(), f"Объявление '{unique_title}' не найдено"