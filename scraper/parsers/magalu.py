"""Parser para Magazine Luiza."""
from playwright.async_api import Page


async def parse_magalu(page: Page) -> dict | None:
    try:
        title = (await page.inner_text("h1[data-testid=heading-product-title]")).strip()
        price_text = await page.inner_text("[data-testid=price-value]")
        price = float(price_text.replace("R$", "").replace(".", "").replace(",", ".").strip())
        return {"title": title, "price": price, "source": "magalu"}
    except Exception:
        return None
