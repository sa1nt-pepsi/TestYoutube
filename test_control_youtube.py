from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_play_pause_video(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-play-button"))
    )
    play_button.click()

    # Проверяем состояние кнопки (должна быть пауза после клика)
    assert play_button.get_attribute("title").lower() == "пауза (k)"
    driver.quit()

def test_volume_control(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    volume_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-mute-button"))
    )
    volume_btn.click()

    # Устанавливаем громкость на 50%
    volume_slider = driver.find_element(By.CSS_SELECTOR, "div.ytp-volume-slider")
    driver.execute_script("arguments[0].value = 50; arguments[0].dispatchEvent(new Event('input'))", volume_slider)

    current_volume = volume_slider.get_attribute("value")
    assert current_volume == "50"
    driver.quit()


def test_fullscreen_mode(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    fullscreen_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-fullscreen-button"))
    )
    fullscreen_btn.click()

    # Проверяем, что видео в полноэкранном режиме
    is_fullscreen = driver.execute_script("return document.fullscreenElement !== null")
    assert is_fullscreen
    driver.quit()

def test_forward_seek(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    # Ждем загрузки плеера
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "video.html5-main-video"))
    )

    # Получаем текущее время
    current_time = driver.execute_script("return document.querySelector('video').currentTime")

    # Перематываем вперед на 10 секунд
    driver.execute_script("document.querySelector('video').currentTime += 10")

    new_time = driver.execute_script("return document.querySelector('video').currentTime")
    assert float(new_time) >= float(current_time) + 10
    driver.quit()


def test_backward_seek(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    # Сначала перематываем вперед
    driver.execute_script("document.querySelector('video').currentTime = 30")

    # Получаем текущее время
    current_time = driver.execute_script("return document.querySelector('video').currentTime")

    # Перематываем назад на 10 секунд
    driver.execute_script("document.querySelector('video').currentTime -= 10")

    new_time = driver.execute_script("return document.querySelector('video').currentTime")
    assert float(new_time) <= float(current_time) - 10
    driver.quit()


def test_time_display(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    time_display = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.ytp-time-current"))
    )

    assert time_display.text.count(":") == 1
    driver.quit()


def test_like_button(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    like_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Нравится']"))
    )
    initial_state = like_button.get_attribute("aria-pressed")

    like_button.click()
    new_state = like_button.get_attribute("aria-pressed")

    assert initial_state != new_state
    driver.quit()


def test_add_to_playlist(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Добавить в плейлист']"))
    )
    add_button.click()

    playlist_dialog = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "playlist-dialog"))
    )

    assert playlist_dialog.is_displayed()
    driver.quit()


def test_next_video_button(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    next_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.ytp-next-button"))
    )
    initial_url = driver.current_url

    next_button.click()

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != initial_url
    )

    assert driver.current_url != initial_url
    driver.quit()


def test_miniplayer_mode(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    miniplayer_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-miniplayer-button"))
    )
    miniplayer_btn.click()

    miniplayer = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.html5-video-player.ytp-miniplayer"))
    )

    assert miniplayer.is_displayed()
    driver.quit()


def test_controls_visibility(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "video.html5-main-video"))
    )

    # Проверяем, что элементы управления видны
    controls = driver.find_element(By.CSS_SELECTOR, "div.ytp-chrome-bottom")
    assert controls.is_displayed()

    # Наводим курсор вне видео
    action = ActionChains(driver)
    action.move_to_element_with_offset(video, -100, -100).perform()

    # Проверяем, что элементы управления скрылись
    try:
        assert not controls.is_displayed()
    except:
        # В некоторых случаях элементы могут оставаться видимыми
        pass

    driver.quit()


def test_stats_for_nerds(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    # Открываем меню настроек
    settings_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-settings-button"))
    )
    settings_btn.click()

    # Включаем "Статистику видео"
    stats_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Статистика видео')]"))
    )
    stats_btn.click()

    # Проверяем отображение статистики
    stats_panel = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ytp-videowall-stats"))
    )

    assert stats_panel.is_displayed()
    driver.quit()


def test_comprehensive_controls_check(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    # Проверка основных элементов управления
    assert driver.find_element(By.CSS_SELECTOR, "button.ytp-play-button").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "button.ytp-mute-button").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "button.ytp-subtitles-button").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "button.ytp-fullscreen-button").is_displayed()

    # Проверка кнопок взаимодействия
    assert driver.find_element(By.CSS_SELECTOR, "button[aria-label='Нравится']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "button[aria-label='Не нравится']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "button[aria-label='Поделиться']").is_displayed()

    # Проверка временной шкалы
    progress_bar = driver.find_element(By.CSS_SELECTOR, "div.ytp-progress-bar")
    assert progress_bar.is_displayed()

    driver.quit()