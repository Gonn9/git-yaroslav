from playwright.sync_api import sync_playwright
import time
import  os
import json

def test_basic_navigation():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://app.atom.dev.sigmation.ai/login")
        print(page.title(), "Блок Авторизация")
        page.wait_for_load_state("networkidle")

        page.locator('[name="email"]').click()
        page.locator('[name="email"]').fill('r.azizov@mixit.ru')
        page.locator('[name="password"]').click()
        page.locator('[name="password"]').fill('q1w2e3r4T~!')
        page.locator('[type="submit"]').click()
        page.wait_for_load_state("networkidle")
        time.sleep(3)
        page.locator('.css-1boe3v5').nth(3).click()
        time.sleep(3)
        page.wait_for_load_state("networkidle")
        page.locator('.css-1eoko2m').nth(5).click()
        time.sleep(3)
        page.wait_for_load_state("networkidle")
        context.storage_state(path="auth_azizov.json")
        print("Состояние сохранено - пользователь в ЛК")

        browser.close()
if __name__ == "__main__":
    test_basic_navigation()