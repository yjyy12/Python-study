from playwright.sync_api import sync_playwright

def run_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=100,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://shopping.naver.com/ns/home")

        try:
            page.get_by_role("button", name="하루 동안 보지 않기").click(timeout=3000)
        except:
            pass

        page.pause()  # 직접 조작 가능
        browser.close()

if __name__ == "__main__":
    run_playwright()
