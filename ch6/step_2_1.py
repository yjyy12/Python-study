from playwright.async_api import Page, async_playwright  # 비동기 API 사용
from step_1_2 import run_playwright  # 이전에 작성한 모듈을 비동기 버전으로 사용
from step_1_3 import goto_best_goods  # 비동기 버전

# 카테고리 선택 함수
async def select_category(page: Page, category: str = None):
    selector = "li[class*='imageCategoryResponsive_list'] > button"
    await page.locator(selector, has_text=category).click()  # 카테고리 버튼 클릭

# 옵션 선택 함수
async def select_options(page: Page, option: str = None):
    await page.get_by_role("button", name="모두가 좋아하는 레이어 열기").click()
    await page.get_by_text(option).click()  # 세부 옵션 버튼 클릭

# 메인 실행 함수
if __name__ == "__main__":
    import asyncio

    async def main():
        # 비동기 방식으로 playwright 실행
        play, browser, page = await run_playwright(slow_mo=1000)
        
        # 베스트상품 페이지로 이동
        await goto_best_goods(page)
        await select_category(page, "패션의류")  # 카테고리 클릭
        await select_options(page, "10대 여성")  # 세부 옵션 클릭
        await page.pause()
        await browser.close()
        await play.stop()

