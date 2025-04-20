from playwright.async_api import Browser, Page, Playwright, async_playwright

async def run_playwright(slow_mo: float = None) -> tuple[Playwright, Browser, Page]:
    play: Playwright = await async_playwright().start()
    browser: Browser = await play.chromium.launch(
        args=["--start-maximized"],
        headless=False,
        slow_mo=slow_mo,
    )
    page: Page = await browser.new_page(no_viewport=True)
    await page.add_locator_handler(
        page.get_by_role("button", name="하루 동안 보지 않기"),
        handler=lambda loc: loc.click(),
        times=1,
    )
    return play, browser, page

if __name__ == "__main__":  
    import asyncio
    async def main():
        play, browser, page = await run_playwright()
        await page.goto("https://shopping.naver.com/ns/home")
        await page.pause()
        await browser.close()
        await play.stop()
  