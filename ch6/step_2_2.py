import asyncio
import json
from pathlib import Path

from playwright.async_api import Page, async_playwright  # async_playwright 클래스 불러오기

from step_1_1 import OUT_DIR
from step_1_2 import run_playwright
from step_1_3 import goto_best_goods

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.json"

async def take_screenshots(page: Page, count: int = 15):
    locs = await page.locator("li[class*='productCardResponsive_product_card']").all()
    imgs_path = []
    for idx, loc in enumerate(locs[:count]):
        path = OUT_DIR / f"{Path(__file__).stem}_{idx+1:03}.png"
        await loc.screenshot(path=path)
        imgs_path.append(path.as_posix())

    with open(OUT_2_2, "w", encoding="utf-8") as fp:
        json.dump(imgs_path, fp, indent=2, ensure_ascii=False)

async def main():
    async with async_playwright() as play:  # Playwright 객체 생성
        browser = await play.chromium.launch(headless=False)  # Browser 객체 생성
        page = await browser.new_page()  # Page 객체 생성

        # run_playwright 호출을 async로 변경하고, await을 사용하여 비동기적으로 처리
        play, browser, page = await run_playwright(slow_mo=1000)

        await goto_best_goods(page)
        await page.pause()

        await take_screenshots(page)

        await browser.close()
        await play.stop()


















