from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")  # thay URL thật vào đây
    driver.maximize_window()
    yield driver
    driver.quit()

# TC01 - Login thành công
def test_login_success(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(2)
    assert "Dashboard" in driver.page_source or "Login success" in driver.page_source

# TC02 - Sai password
def test_login_wrong_password(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("wrong")
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(2)
    assert "Invalid" in driver.page_source

# TC03 - Bỏ trống Username
def test_blank_username(driver):
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(2)
    assert "Please enter username" in driver.page_source

# TC04 - Bỏ trống Password
def test_blank_password(driver):
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(2)
    assert "Please enter password" in driver.page_source

# TC05 - Forgot Password link
def test_forgot_password_link(driver):
    forgot_link = driver.find_element(By.LINK_TEXT, "Forgot password?")
    assert forgot_link.is_displayed()
    forgot_link.click()
    time.sleep(2)
    assert "Reset Password" in driver.page_source

# TC06 - Social Login buttons
def test_social_login_buttons(driver):
    fb = driver.find_element(By.CSS_SELECTOR, "a[href*='facebook']")
    tw = driver.find_element(By.CSS_SELECTOR, "a[href*='twitter']")
    gg = driver.find_element(By.CSS_SELECTOR, "a[href*='google']")
    assert fb.is_displayed() and tw.is_displayed() and gg.is_displayed()
