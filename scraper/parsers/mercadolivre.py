"""Parser para o Mercado Livre."""
from playwright.async_api import Page


async def parse_mercadolivre(page: Page) -> dict | None:
    try:
        title = (await page.inner_text("h1.ui-pdp-title")).strip()
        price_el = page.locator(".andes-money-amount__fraction").first
        price_text = await price_el.inner_text()
        price = float(price_text.replace(".", "").replace(",", "."))
        return {"title": title, "price": price, "source": "mercadolivre"}
    except Exception:
        return None
