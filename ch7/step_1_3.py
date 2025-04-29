import json
from pathlib import Path
from playwright.async_api import async_playwright, Page
from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright

OUT_DIR.mkdir(exist_ok=True)
OUT_1_3 = OUT_DIR / f"{Path(__file__).stem}.json"

async def goto_market_cap(page: Page):
    await page.goto("https://finance.naver.com")
    await page.get_by_role("link", name="국내증시").click()
    await page.get_by_role("link", name="시가총액").first.click() #이부분 문법이 잘못되어 있었어요 수정했어요

async def parse_table_kospi(page: Page) -> tuple[list, list]:
    tag_table = page.locator("table", has_text="코스피")
    tag_thead = tag_table.locator("thead > tr > th")
    header = await tag_thead.all_inner_texts()
    tag_tbody = tag_table.locator("tbody > tr")
    body = [await tr.locator("td").all_inner_texts() for tr in await tag_tbody.all()]
    return header, body

async def main():
    async with async_playwright() as play:
        browser = await play.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        
        await goto_market_cap(page)
        header, body = await parse_table_kospi(page)
        
        dumped = json.dumps(dict(header=header, body=body), ensure_ascii=False, indent=2)
        ######해당 부분 추가해주세요######
        print("저장할 경로:", OUT_1_3.resolve())
        print("헤더 길이:", len(header))
        print("바디 길이:", len(body))
        ######해당 부분 추가해주세요######
        OUT_1_3.write_text(dumped, encoding="utf-8")
        
        await browser.close()

# 이벤트 루프 실행
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())