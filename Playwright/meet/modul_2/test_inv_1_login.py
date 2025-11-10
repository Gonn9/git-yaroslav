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
        page.locator('[name="email"]').fill('m.suprun@mixit.ru')
        page.locator('[name="password"]').click()
        page.locator('[name="password"]').fill('q1w2e3r4T~!!')
        page.locator('[type="submit"]').click()
        page.wait_for_load_state("networkidle")

        page.locator('a[href="/meet"]').click()
        page.wait_for_load_state("networkidle")
        context.storage_state(path="auth1.json")
        print("Состояние сохранено - пользователь в ЛК")

        browser.close()
if __name__ == "__main__":
    test_basic_navigation()