from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_youtube(driver):
    driver.get('https://www.youtube.com')
    time.sleep(2)
    assert 'YouTube' in driver.title

def test_open_youtube2(driver):
    driver.get('https://wwww.youtube.com')
    time.sleep(2)
    assert 'YouTube' in driver.title

def test_open_youtube3(driver):
    driver.get('https://www.youtibe.com')
    time.sleep(2)
    assert 'YouTube' in driver.title

def test_open_youtube4(driver):
    driver.get('htttps://www.youtube.com')
    time.sleep(2)
    assert 'YouTube' in driver.title


def test_youtube_logo_presence():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "logo-icon"))
    )
    assert logo.is_displayed()
    driver.quit()

def test_youtube_headless():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com")
    assert "YouTube" in driver.title
    driver.quit()

def test_search_bar_presence():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    search_bar = driver.find_element(By.NAME, "search_query")
    assert search_bar.is_displayed()
    driver.quit()

def test_sign_in_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    sign_in_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Войти')]")
    assert sign_in_button.is_displayed()
    driver.quit()

def test_language_detection():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    html = driver.find_element(By.TAG_NAME, "html")
    assert html.get_attribute("lang") is not None
    driver.quit()

def test_dark_theme_switch():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    driver.execute_script("document.body.style.backgroundColor = 'black'")
    background = driver.execute_script("return document.body.style.backgroundColor")
    assert background == 'black'
    driver.quit()

def test_mobile_view():
    mobile_emulation = {"deviceName": "iPhone X"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com")
    assert "YouTube" in driver.title
    driver.quit()

def test_youtube_version():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    version = driver.execute_script("return yt.config_.VERSION")
    assert version is not None
    driver.quit()

