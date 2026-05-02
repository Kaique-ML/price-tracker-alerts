"""Parser para Amazon Brasil."""
from playwright.async_api import Page


async def parse_amazon(page: Page) -> dict | None:
    try:
        title = (await page.inner_text("#productTitle")).strip()
        price_text = await page.inner_text(".a-price-whole")
        price = float(price_text.replace(".", "").replace(",", "."))
        return {"title": title, "price": price, "source": "amazon"}
    except Exception:
        return None
