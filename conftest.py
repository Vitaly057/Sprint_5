import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthLocators
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from urls import BASE_URL

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(*AuthLocators.LOGIN_REG_BUTTON).click()
    wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL)).send_keys(EXISTING_USER_EMAIL)
    driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys(EXISTING_USER_PASSWORD)
    driver.find_element(*AuthLocators.LOGIN_SUBMIT_BUTTON).click()
    wait.until(EC.visibility_of_element_located(AuthLocators.CREATE_AD_BUTTON))
    return driver