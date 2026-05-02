"""Pool assíncrono de workers Playwright para scraping de preços."""
import asyncio
from playwright.async_api import async_playwright
from scraper.parsers.mercadolivre import parse_mercadolivre
from scraper.parsers.amazon_br import parse_amazon
from scraper.parsers.magalu import parse_magalu
import redis
import json
import os

r = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

PARSERS = {
    "mercadolivre.com.br": parse_mercadolivre,
    "amazon.com.br": parse_amazon,
    "magazineluiza.com.br": parse_magalu,
}


async def run_scraping_cycle():
    products = _get_products_from_db()
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        tasks = [_scrape_product(browser, p) for p in products]
        await asyncio.gather(*tasks, return_exceptions=True)
        await browser.close()
    print(f"✅ Ciclo completo: {len(products)} produtos verificados")


async def _scrape_product(browser, product: dict):
    url = product["url"]
    domain = [d for d in PARSERS if d in url]
    if not domain:
        return
    parser = PARSERS[domain[0]]
    page = await browser.new_page()
    try:
        await page.goto(url, timeout=30000)
        data = await parser(page)
        if data:
            _check_alert(product, data["price"])
    except Exception as e:
        print(f"Erro em {url}: {e}")
    finally:
        await page.close()


def _get_products_from_db() -> list[dict]:
    # TODO: buscar do PostgreSQL
    return [{"id": "1", "url": "https://www.mercadolivre.com.br/...", "max_price": 2500.0, "name": "Notebook"}]


def _check_alert(product: dict, current_price: float):
    key = f"price:{product['id']}"
    last = r.get(key)
    last_price = float(last) if last else None
    r.set(key, current_price, ex=86400)
    if current_price <= product["max_price"]:
        print(f"🔔 ALERTA! {product['name']}: R$ {current_price} (max: R$ {product['max_price']})")
