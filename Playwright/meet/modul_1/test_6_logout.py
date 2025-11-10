from playwright.sync_api import sync_playwright
import time
import os
import json

def test_basic_navigation():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)  # headless=True для фонового режима

        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto("https://app.atom.dev.sigmation.ai/meet")
        print(page.title(), "Пользователь уже авторизован")
        # Выйти из аккаунта
        page.locator('.css-a36glh').click()
        print(page.title(), "Блок Авторизация")

        if os.path.exists("auth.json"):
            os.remove("auth.json")

        # Закрытие браузера
        browser.close()

if __name__ == "__main__":
    test_basic_navigation()