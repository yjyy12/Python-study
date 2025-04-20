import asyncio
from playwright.async_api import async_playwright  # async_playwright 클래스 불러오기

async def run():
    async with async_playwright() as play:  # Playwright 객체 생성
        browser = await play.chromium.launch(headless=False)  # Browser 객체 생성
        page = await browser.new_page()  # Page 객체 생성
        await page.goto("https://shopping.naver.com/ns/home")  # 페이지 이동
        await page.pause()  # 인스펙터 실행
