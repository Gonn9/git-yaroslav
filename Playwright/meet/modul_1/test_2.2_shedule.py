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

        #блок запланировать
        page.locator('[data-testid="meet-page-schedule-meeting-card"]').click()
        print(page.title(), "Запланировать")

        page.locator(".css-1mx6x7h").click()
        print(page.title(), "Данные сохранены в буфер обмена")
        page.locator(".css-1hm7oyh").click()
        page.locator(".css-zasnql").click()

        # Вход в лайвкит через ввод ссылки
        input_field = page.locator('.css-zasnql')
        input_field.click()
        page.keyboard.press('Meta+V')
        page.locator('.css-1gkx8v3').click()

        page.locator('[data-testid="meet-page-join-meeting-button"]').click()
        print(page.title(), "Вход в превью комнаты по ссылке успешен")

        # Вход в комнату + ввод имени
        page.locator("#username").fill("Ярослав")
        page.locator(".lk-join-button").click()
        page.wait_for_load_state("networkidle")
        print(page.title(), "Вход в комнату")

        # Выход из комнаты
        page.locator(".lk-disconnect-button").nth(0).click()
        print(page.title(), "Выход из комнаты")

        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


