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


# общий доступ изменен на ограниченный
        page.locator('[data-room-slug="testobshijdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator(".css-15lidk2").nth(1).click()  # ограниченный
        page.locator('[data-testid="room-modal-participants-input"]').click()
        page.locator('[data-testid="room-modal-participants-input"]').fill('m.suprun@mixit.ru')
        page.locator('[data-testid="room-modal-participants-add-button"]').click()
        page.locator('[data-testid="room-modal-save-button"]').click()  # сохранить
        print(page.title(), 'общий доступ изменен на ограниченный')

# ограниченный доступ изменен на общий
        page.locator('[data-room-slug="testogranichennyjdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator(".css-15lidk2").nth(0).click()  # общий
        page.locator('[data-testid="room-modal-save-button"]').click()  # сохранить
        print(page.title(), 'ограниченный доступ изменен на общий')

# изменение названия
        page.locator('[data-room-slug="testogranichennyjdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator('[data-testid="room-modal-name-input"]').click()
        page.locator('[data-testid="room-modal-name-input"]').fill('Изменено')
        page.locator('[data-testid="room-modal-save-button"]').click()  # сохранить
        print(page.title(), 'название изменено')


        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


