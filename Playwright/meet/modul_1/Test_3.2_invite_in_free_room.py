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

        # Вход в лайвкит через ввод ссылки
        page.locator('[data-room-slug="testobshijdostup"] [data-testid="corporate-room-card-enter-button"]').click()
        print(page.title(), "Вход в превью комнаты успешен")

        # Вход в комнату + ввод имени
        page.locator("#username").fill("Ярослав")
        page.locator(".lk-join-button").click()
        page.wait_for_load_state("networkidle")
        print(page.title(), "inside livekit")
        time.sleep(10)

        # Выход из комнаты
        page.wait_for_load_state("networkidle")
        page.locator(".lk-disconnect-button").nth(0).click()
        print(page.title(), "Выход из комнаты")

        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


