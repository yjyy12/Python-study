from playwright.async_api import Page, async_playwright  # 비동기 API 사용
from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.

# 페이지 이동 함수
async def goto_best_goods(page: Page):
    await page.goto("https://shopping.naver.com/ns/home")  # 페이지 이동
    await page.get_by_role("link", name="베스트상품").click()  # 클릭

# 메인 실행 함수
if __name__ == "__main__":
    import asyncio

    async def main():
        play, browser, page = await run_playwright(slow_mo=1000)
        await goto_best_goods(page)  # 베스트상품 페이지로 이동
        await page.pause()  # 인스펙터 실행
        await browser.close()
        await play.stop()

