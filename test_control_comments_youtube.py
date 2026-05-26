from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_comment_section_visibility():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    comments_section = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//ytd-comments"))
    )
    assert comments_section.is_displayed()
    driver.quit()

def test_expand_comments_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    expand_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Развернуть')]"))
    )
    expand_btn.click()

    comments = driver.find_element(By.XPATH, "//ytd-comment-thread-renderer")
    assert comments.is_displayed()
    driver.quit()


def test_comment_post_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    driver.add_cookie({"name": "LOGIN_INFO", "value": "YOUR_AUTH_COOKIE"})  # тут нужна авторизация

    comment_box = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='placeholder-area']"))
    )
    comment_box.click()

    input_field = driver.find_element(By.XPATH, "//div[@id='contenteditable-root']")
    input_field.send_keys("Тестовый комментарий")

    post_button = driver.find_element(By.XPATH, "//ytd-button-renderer[@id='submit-button']")
    assert post_button.is_enabled()
    driver.quit()


def test_comment_like_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    like_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//yt-icon[@id='like-button'])[1]"))
    )
    like_btn.click()

    # Проверяем, что кнопка изменила состояние
    liked = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "(//yt-icon[@id='like-button']/button[@aria-pressed='true'])[1]"))
    )
    assert liked
    driver.quit()


def test_comment_dislike_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    dislike_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//yt-icon[@id='dislike-button'])[1]"))
    )
    dislike_btn.click()

    disliked = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "(//yt-icon[@id='dislike-button']/button[@aria-pressed='true'])[1]"))
    )
    assert disliked
    driver.quit()

def test_comment_reply_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    reply_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//yt-formatted-string[contains(text(), 'Ответить')])[1]"))
    )
    reply_btn.click()

    reply_box = driver.find_element(By.XPATH, "(//div[@id='reply-text-field'])[1]")
    assert reply_box.is_displayed()
    driver.quit()


def test_expand_replies_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    expand_replies_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//yt-formatted-string[contains(text(), 'Развернуть')])[2]"))
    )
    expand_replies_btn.click()

    replies = driver.find_element(By.XPATH, "(//ytd-comment-replies-renderer)[1]")
    assert replies.is_displayed()
    driver.quit()


def test_pinned_comment():
    driver = webdriver.Chrome()
    driver.get(
        "https://www.youtube.com/watch?v=0_IWHx20yqc")

    pinned = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//ytd-comment-thread-renderer[contains(@class, 'pinned-comment')]"))
    )
    assert pinned.is_displayed()
    driver.quit()

def test_show_more_comments():
    driver = webdriver.Chrome()
    driver.get(
        "https://www.youtube.com/watch?v=0_IWHx20yqc")

    show_more_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Показать')]"))
    )
    initial_count = len(driver.find_elements(By.XPATH, "//ytd-comment-thread-renderer"))

    show_more_btn.click()
    time.sleep(2)  # Ждем загрузки

    new_count = len(driver.find_elements(By.XPATH, "//ytd-comment-thread-renderer"))
    assert new_count > initial_count
    driver.quit()


def test_share_comment_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    menu_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-menu-renderer//button)[1]"))
    )
    menu_btn.click()

    share_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Поделиться')]"))
    )
    assert share_btn.is_displayed()
    driver.quit()

def test_report_comment_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    menu_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-menu-renderer//button)[1]"))
    )
    menu_btn.click()

    report_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Пожаловаться')]"))
    )
    assert report_btn.is_displayed()
    driver.quit()


def test_edit_comment_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")
    driver.add_cookie({"name": "LOGIN_INFO", "value": "YOUR_AUTH_COOKIE"})

    menu_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-menu-renderer//button)[1]"))
    )
    menu_btn.click()

    edit_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Редактировать')]"))
    )
    assert edit_btn.is_displayed()
    driver.quit()

def test_delete_comment_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")  # видео с моим комментарием
    driver.add_cookie({"name": "LOGIN_INFO", "value": "YOUR_AUTH_COOKIE"})

    menu_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-menu-renderer//button)[1]"))
    )
    menu_btn.click()

    delete_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Удалить')]"))
    )
    assert delete_btn.is_displayed()
    driver.quit()

def test_comment_author_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    author = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-comment-thread-renderer//a[@id='author-text'])[1]"))
    )
    author.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/user/") | EC.url_contains("/channel/")
    )
    assert "youtube.com" in driver.current_url
    driver.quit()

def test_comment_time_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    time_btn = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, "(//ytd-comment-thread-renderer//yt-formatted-string[@id='published-time-text'])[1]"))
    )
    assert "назад" in time_btn.text or "ago" in time_btn.text
    driver.quit()

def test_comment_permalink():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    menu_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-menu-renderer//button)[1]"))
    )
    menu_btn.click()

    permalink = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Ссылка')]"))
    )
    permalink.click()

    WebDriverWait(driver, 5).until(
        EC.url_contains("lc=")  # Параметр ссылки на комментарий
    )
    assert "lc=" in driver.current_url
    driver.quit()


def test_comment_emoji_button():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")
    driver.add_cookie({"name": "LOGIN_INFO", "value": "YOUR_AUTH_COOKIE"})

    comment_box = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='placeholder-area']"))
    )
    comment_box.click()

    emoji_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Смайлики']"))
    )
    emoji_btn.click()

    emoji_panel = driver.find_element(By.XPATH, "//yt-emoji-picker")
    assert emoji_panel.is_displayed()
    driver.quit()

def test_comprehensive_comments_functionality():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=0_IWHx20yqc")

    # Проверка основных элементов
    assert driver.find_element(By.XPATH, "//ytd-comments").is_displayed()
    assert driver.find_element(By.XPATH, "//div[@id='placeholder-area']").is_displayed()

    # Проверка кнопок взаимодействия
    comments = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//ytd-comment-thread-renderer"))
    )
    assert len(comments) > 0

    first_comment = comments[0]
    assert first_comment.find_element(By.XPATH, ".//yt-icon[@id='like-button']").is_displayed()
    assert first_comment.find_element(By.XPATH, ".//yt-formatted-string[contains(text(), 'Ответить')]").is_displayed()

    driver.quit()