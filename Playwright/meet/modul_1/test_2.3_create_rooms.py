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

# Крестик + отмена
        page.locator('[data-testid="meet-page-create-room-card"]').click()
        page.locator('[data-testid="close-modal-button"]').click()
        page.locator('[data-testid="meet-page-create-room-card"]').click()
        page.locator('[data-testid="room-modal-cancel-button"]').click()
        print(page.title(), "тест выхода из модального окна")

# Создать комнату публ
        page.locator('[data-testid="meet-page-create-room-card"]').click()
        page.locator(".css-13mnqbs").click()
        page.locator('[data-testid="room-modal-name-input"]').click()
        page.locator('[data-testid="room-modal-name-input"]').fill('ТестОбщийДоступ')
        page.locator(".css-13mnqbs").click()
        page.locator(".css-15lidk2").nth(1).click() #ограниченный
        page.locator(".css-15lidk2").nth(0).click() #общий
        page.locator('[data-testid="room-modal-save-button"]').click() #сохранить
        print(page.title(), "комната 'Общий доступ' создана")

#Создать комнату огр дост
        page.locator('[data-testid="meet-page-create-room-card"]').click()
        page.locator('[data-testid="room-modal-name-input"]').click()
        page.locator('[data-testid="room-modal-name-input"]').fill('ТестОграниченныйДоступ')
        page.locator(".css-15lidk2").nth(1).click()  # ограниченный
        page.locator('[data-testid="room-modal-participants-input"]').click()
        page.locator('[data-testid="room-modal-participants-input"]').fill('m.suprun@mixit.ru')
        page.locator('[data-testid="room-modal-participants-add-button"]').click()
        page.locator('[data-testid="room-modal-save-button"]').click() #сохранить
        print(page.title(), "комната 'Ограниченный доступ' создана")

        browser.close()

if __name__ == "__main__":
    test_basic_navigation()


