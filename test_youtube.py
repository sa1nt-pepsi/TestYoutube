from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()

def test_open_youtube(driver):
    driver.get('https://www.youtube.com')
    time.sleep(2)
    assert 'YouTube' in driver.title
    print("Тест 1-Главная страница YouTube открыта.")

def test_search_video(driver):
    driver.get('https://www.youtube.com')
    search_box = driver.find_element(By.XPATH, "//*[@id='center']/yt-searchbox/div[1]/form/input")
    search_box.send_keys("Kuplinov play")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert 'Kuplinov play' in driver.page_source
    print("Тест 2-Поиск видео выполнен.")

def test_search_and_play_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(10)
    print("Тест 3-Видео воспроизводится.")

def test_pause_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(5)
    video = driver.find_element(By.CSS_SELECTOR, "video")
    video.click()
    time.sleep(10)
    print("Тест 4-Видео на паузе.")

def test_like_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(5)
    like_button = driver.find_element(By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button')
    like_button.click()
    time.sleep(2)
    print("Тест 5-Видео лайкнуто.")

def test_dislike_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(5)
    dislike_button = driver.find_element(By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/dislike-button-view-model')
    dislike_button.click()
    time.sleep(2)
    print("Тест 6-Видео дизлайкнуто.")

def test_share_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(5)

    share_button = driver.find_element(By.XPATH, '//*[@id="top-level-buttons-computed"]/yt-button-view-model/button-view-model/button')
    share_button.click()
    time.sleep(2)
    print("Тест 7-Открыто меню 'Поделиться'.")

def test_report_video(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(5)
    report_button1 = driver.find_element(By.XPATH, '//*[@id="button-shape"]/button/yt-touch-feedback-shape/div/div[2]')
    report_button1.click()
    time.sleep(2)
    report_button2 = driver.find_element(By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
    report_button2.click()
    time.sleep(2)
    print("Тест 8-Окно репорта открыто.")

def test_subscribe_channel(driver):
    driver.get('https://www.youtube.com')
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search_query = "Kuplinov play"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)
    first_video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    first_video.click()
    time.sleep(10)
    subscribe_button = driver.find_element(By.XPATH,'//*[@id="subscribe-button"]')
    subscribe_button.click()
    time.sleep(2)
    print("Тест 9-Кнопка 'Подписаться' нажата")

def test_comment_video(driver):
    driver.get('https://www.youtube.com')
    comment_box = driver.find_element(By.XPATH, '//*[@id="placeholder-area"]')
    comment_box.click()
    time.sleep(2)
    print("Тест 10: Открыто поле для комментария.")

def test_login_button(driver):
    driver.get('https://www.youtube.com')
    login_button = driver.find_element(By.XPATH, '//*[contains(text(), "Войти")]')
    login_button.click()
    time.sleep(2)
    assert "accounts.google.com" in driver.current_url
    print("Тест 11: Открыта страница входа.")

def test_trending_page(driver):
    driver.get('https://www.youtube.com')
    trending_button = driver.find_element(By.XPATH, '//a[@title="Тренды"]')
    trending_button.click()
    time.sleep(2)
    assert "Тренды" in driver.page_source
    print("Тест 12: Открыта страница 'Тренды'.")

def test_subscriptions_page(driver):
    driver.get('https://www.youtube.com')
    subscriptions_button = driver.find_element(By.XPATH, '//a[@title="Подписки"]')
    subscriptions_button.click()
    time.sleep(2)
    assert "Подписки" in driver.page_source
    print("Тест 13: Открыта страница 'Подписки'.")

def test_library_page(driver):
    driver.get('https://www.youtube.com')
    library_button = driver.find_element(By.XPATH, '//a[@title="Библиотека"]')
    library_button.click()
    time.sleep(2)
    assert "Библиотека" in driver.page_source
    print("Тест 14: Открыта страница 'Библиотека'.")

def test_history_page(driver):
    driver.get('https://www.youtube.com')
    history_button = driver.find_element(By.XPATH, '//a[@title="История"]')
    history_button.click()
    time.sleep(2)
    assert "История" in driver.page_source
    print("Тест 15: Открыта страница 'История'.")

def test_my_videos_page(driver):
    driver.get('https://www.youtube.com')
    my_videos_button = driver.find_element(By.XPATH, '//a[@title="Мои видео"]')
    my_videos_button.click()
    time.sleep(2)
    assert "Мои видео" in driver.page_source
    print("Тест 16: Открыта страница 'Мои видео'.")

def test_liked_videos_page(driver):
    driver.get('https://www.youtube.com')
    liked_videos_button = driver.find_element(By.XPATH, '//a[@title="Понравившиеся"]')
    liked_videos_button.click()
    time.sleep(2)
    assert "Понравившиеся" in driver.page_source
    print("Тест 17: Открыта страница 'Понравившиеся'.")

def test_playlists_page(driver):
    driver.get('https://www.youtube.com')
    playlists_button = driver.find_element(By.XPATH, '//a[@title="Плейлисты"]')
    playlists_button.click()
    time.sleep(2)
    assert "Плейлисты" in driver.page_source
    print("Тест 18: Открыта страница 'Плейлисты'.")

def test_settings_page(driver):
    driver.get('https://www.youtube.com')
    settings_button = driver.find_element(By.XPATH, '//button[@aria-label="Настройки"]')
    settings_button.click()
    time.sleep(2)
    assert "Настройки" in driver.page_source
    print("Тест 19: Открыто меню 'Настройки'.")

def test_switch_account(driver):
    driver.get('https://www.youtube.com')
    switch_account_button = driver.find_element(By.XPATH, '//*[contains(text(), "Сменить аккаунт")]')
    switch_account_button.click()
    time.sleep(2)
    assert "accounts.google.com" in driver.current_url
    print("Тест 20: Открыта страница смены аккаунта.")

def test_create_playlist(driver):
    driver.get("https://www.youtube.com")
    library_button = driver.find_element(By.XPATH, '//a[@title="Библиотека"]')
    library_button.click()
    time.sleep(2)
    create_playlist_button = driver.find_element(By.XPATH, '//*[contains(text(), "Создать плейлист")]')
    create_playlist_button.click()
    time.sleep(2)
    assert "Создать плейлист" in driver.page_source
    print("Тест 21: Открыто окно создания плейлиста.")

def test_add_video_to_playlist(driver):
    driver.get("https://www.youtube.com/watch?v=a6aeDJvG26A&list=PLRVGb5te8vVH3DJKxtRQp3-68_gQ3CEqx&index=1&t=7568s")
    time.sleep(2)
    add_to_playlist_button = driver.find_element(By.XPATH, '//button[@aria-label="Сохранить"]')
    add_to_playlist_button.click()
    time.sleep(2)
    assert "Добавить в плейлист" in driver.page_source
    print("Тест 22: Открыто меню добавления видео в плейлист.")

def test_notifications(driver):
    driver.get("https://www.youtube.com")
    notifications_button = driver.find_element(By.XPATH, '//button[@aria-label="Уведомления"]')
    notifications_button.click()
    time.sleep(2)
    assert "Уведомления" in driver.page_source
    print("Тест 23: Открыты уведомления.")

def test_show_more(driver):
    driver.get("https://www.youtube.com")
    show_more_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать больше")]')
    show_more_button.click()
    time.sleep(2)
    print("Тест 24: Нажата кнопка 'Показать больше'.")

def test_hide(driver):
    driver.get("https://www.youtube.com")
    hide_button = driver.find_element(By.XPATH, '//*[contains(text(), "Скрыть")]')
    hide_button.click()
    time.sleep(2)
    print("Тест 25: Нажата кнопка 'Скрыть'.")

def test_dark_theme(driver):
    driver.get("https://www.youtube.com")
    settings_button = driver.find_element(By.XPATH, '//button[@aria-label="Настройки"]')
    settings_button.click()
    time.sleep(1)
    dark_theme_button = driver.find_element(By.XPATH, '//*[contains(text(), "Темная тема")]')
    dark_theme_button.click()
    time.sleep(2)
    print("Тест 26: Включена темная тема.")

def test_language(driver):
    driver.get("https://www.youtube.com")
    settings_button = driver.find_element(By.XPATH, '//button[@aria-label="Настройки"]')
    settings_button.click()
    time.sleep(1)
    language_button = driver.find_element(By.XPATH, '//*[contains(text(), "Язык")]')
    language_button.click()
    time.sleep(2)
    assert "Язык" in driver.page_source
    print("Тест 27: Открыто меню выбора языка.")

def test_restricted_mode(driver):
    driver.get("https://www.youtube.com")
    settings_button = driver.find_element(By.XPATH, '//button[@aria-label="Настройки"]')
    settings_button.click()
    time.sleep(1)
    restricted_mode_button = driver.find_element(By.XPATH, '//*[contains(text(), "Ограниченный режим")]')
    restricted_mode_button.click()
    time.sleep(2)
    print("Тест 28: Открыто меню ограниченного режима.")

def test_search_history(driver):
    driver.get("https://www.youtube.com")
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Python tutorial")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    search_history_button = driver.find_element(By.XPATH, '//*[contains(text(), "История поиска")]')
    search_history_button.click()
    time.sleep(2)
    assert "История поиска" in driver.page_source
    print("Тест 29: Открыта история поиска.")

def test_clear_watch_history(driver):
    driver.get("https://www.youtube.com/feed/history")
    time.sleep(2)
    clear_history_button = driver.find_element(By.XPATH, '//*[contains(text(), "Очистить историю просмотров")]')
    clear_history_button.click()
    time.sleep(2)
    print("Тест 30: История просмотров очищена.")

def test_clear_search_history(driver):
    driver.get("https://www.youtube.com/feed/history")
    time.sleep(2)
    clear_search_history_button = driver.find_element(By.XPATH, '//*[contains(text(), "Очистить историю поиска")]')
    clear_search_history_button.click()
    time.sleep(2)
    print("Тест 31: История поиска очищена.")

def test_show_history(driver):
    driver.get("https://www.youtube.com/feed/history")
    time.sleep(2)
    show_history_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать историю")]')
    show_history_button.click()
    time.sleep(2)
    print("Тест 32: История показана.")

def test_hide_history(driver):
    driver.get("https://www.youtube.com/feed/history")
    time.sleep(2)
    hide_history_button = driver.find_element(By.XPATH, '//*[contains(text(), "Скрыть историю")]')
    hide_history_button.click()
    time.sleep(2)
    print("Тест 33: История скрыта.")

def test_show_recommendations(driver):
    driver.get("https://www.youtube.com")
    show_recommendations_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать рекомендации")]')
    show_recommendations_button.click()
    time.sleep(2)
    print("Тест 34: Рекомендации показаны.")

def test_hide_recommendations(driver):
    driver.get("https://www.youtube.com")
    hide_recommendations_button = driver.find_element(By.XPATH, '//*[contains(text(), "Скрыть рекомендации")]')
    hide_recommendations_button.click()
    time.sleep(2)
    print("Тест 35: Рекомендации скрыты.")

def test_show_more_videos(driver):
    driver.get("https://www.youtube.com")
    show_more_videos_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать больше видео")]')
    show_more_videos_button.click()
    time.sleep(2)
    print("Тест 36: Показано больше видео.")

def test_hide_videos(driver):
    driver.get("https://www.youtube.com")
    hide_videos_button = driver.find_element(By.XPATH, '//*[contains(text(), "Скрыть видео")]')
    hide_videos_button.click()
    time.sleep(2)
    print("Тест 37: Видео скрыты.")

def test_show_more_channels(driver):
    driver.get("https://www.youtube.com")
    show_more_channels_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать больше каналов")]')
    show_more_channels_button.click()
    time.sleep(2)
    print("Тест 38: Показано больше каналов.")

def test_hide_channels(driver):
    driver.get("https://www.youtube.com")
    hide_channels_button = driver.find_element(By.XPATH, '//*[contains(text(), "Скрыть каналы")]')
    hide_channels_button.click()
    time.sleep(2)
    print("Тест 39: Каналы скрыты.")

def test_show_more_playlists(driver):
    driver.get("https://www.youtube.com")
    show_more_playlists_button = driver.find_element(By.XPATH, '//*[contains(text(), "Показать больше плейлистов")]')
    show_more_playlists_button.click()
    time.sleep(2)
    print("Тест 40: Показано больше плейлистов.")

