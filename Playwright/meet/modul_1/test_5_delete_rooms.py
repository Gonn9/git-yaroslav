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
#удаление комнат
        page.locator('[data-room-slug="testogranichennyjdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator('[data-testid="room-modal-delete-button"]').click()
        page.locator(".css-bth2k2").click()
        page.locator('[data-testid="room-modal-cancel-button"]').click()
        page.locator('[data-room-slug="testogranichennyjdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator('[data-testid="room-modal-delete-button"]').click()
        page.locator(".css-1j5x1pw").click()
        print(page.title(), "вторая 'Ограниченный доступ' удалена")

        page.locator('[data-room-slug="testobshijdostup"] [data-testid="corporate-room-card-settings-button"]').click()
        page.locator('[data-testid="room-modal-delete-button"]').click()
        page.locator(".css-1j5x1pw").click()
        time.sleep(2)
        print(page.title(), "комната 'Общий доступ' удалена")



        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


