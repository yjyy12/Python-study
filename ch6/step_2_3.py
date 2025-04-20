from step_1_2 import run_playwright
from step_1_3 import goto_best_goods
from step_2_1 import select_category, select_options
from step_2_2 import take_screenshots
import asyncio  

async def fetch_trends_by_filter(category: str = None, option: str = None):
    play, browser, page = await run_playwright(slow_mo=500)
    await goto_best_goods(page)
    if category:
        await select_category(page, category)
    if option:
        await select_options(page, option)
    await take_screenshots(page)
    await browser.close()
    await play.stop()

if __name__ == "__main__":
    category, option = "패션의류", "10대 여성"
    asyncio.run(fetch_trends_by_filter(category, option)) 

