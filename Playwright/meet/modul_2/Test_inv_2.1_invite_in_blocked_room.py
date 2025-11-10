from playwright.sync_api import sync_playwright
import time
import os
import json

def test_basic_navigation():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)  # headless=True для фонового режима

        context = browser.new_context(storage_state="auth1.json")
        page = context.new_page()
        page.goto("https://app.atom.dev.sigmation.ai/meet")

        page.locator('[data-room-slug="testogranichennyjdostup"] [data-testid="corporate-room-card-copy-link-button"]').click()
        input_field = page.locator('[data-testid="meet-page-join-meeting-input"]')
        input_field.click()
        page.keyboard.press('Meta+V')
        print(page.title(), "Вход в превью комнаты по ссылке успешен")
        page.locator('[data-testid="meet-page-join-meeting-button"]').click()
        # Вход в комнату + ввод имени
        page.locator("#username").fill("Ярослав2")
        page.locator(".lk-join-button").click()
        time.sleep(10)
        print(page.title(), "Вход в комнату")

        # Выход из комнаты
        page.wait_for_load_state("networkidle")
        page.locator(".lk-disconnect-button").nth(0).click()
        print(page.title(), "Выход из комнаты")

        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


