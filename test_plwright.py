import time

from playwright.sync_api import Playwright, Page, sync_playwright, expect

"Все поля пустые"
def test_all_fields_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(15)
    assert page.wait_for_selector("span:has-text('Поле не заполнено')")
    browser.close()

"Только имя юзера пустое"
def test_only_user_fields_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Электронная почта").click()
    page.get_by_label("Электронная почта").fill("test@mail.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qaz2wsx3edc434768ddgg")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.wait_for_selector("span:has-text('Поле не заполнено')")
    browser.close()

"Только емейл пустой"
def test_user_fields_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("Vasiliy324")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qaz2wsx3edc434768ddgg")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.wait_for_selector("span:has-text('Поле не заполнено')")
    browser.close()


"Неправильный емейл"
def test_wrong_email_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("Vasiliy324")
    page.get_by_label("Электронная почта").click()
    page.get_by_label("Электронная почта").fill("test.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qaz2wsx3edc434768ddgg")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.wait_for_selector("span:has-text('Формат e-mail: somebody@somewhere.ru')")
    browser.close()


"Короткое имя"
def test_short_username_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("Vas")
    page.get_by_label("Электронная почта").click()
    page.get_by_label("Электронная почта").fill("test@mail.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qaz2wsx3edc434768ddgg")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.wait_for_selector("span:has-text('Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы')")
    browser.close()

"Короткий пароль"
def test_short_password_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("Vasiliy324")
    page.get_by_label("Электронная почта").click()
    page.get_by_label("Электронная почта").fill("test@mail.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qaz")
    page.locator("#input-179").click()
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.wait_for_selector("span:has-text('Пароль должен содержать минимум 8 символов')")
    browser.close()

"Не активировано согласияе(пользовательское соглашение, политика конфиденциальности)"
def test_unable_checkbox_empty(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://exchange.konomik.com/authorization/signup")
    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("Vasiliy324")
    page.get_by_label("Электронная почта").click()
    page.get_by_label("Электронная почта").fill("test@mail.ru")
    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("1qazппFfjhghhHH78")
    page.get_by_role("button", name="Далее").click()
    time.sleep(2)
    assert page.locator("#input-179").is_enabled()
    browser.close()




