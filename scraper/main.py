"""Entrypoint do scraper de preços — agendado pelo APScheduler."""
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper.workers import run_scraping_cycle

scheduler = AsyncIOScheduler()
scheduler.add_job(run_scraping_cycle, "interval", minutes=120, id="price_scraper")
scheduler.start()

if __name__ == "__main__":
    print("⚡ Price tracker iniciado — verificação a cada 2h")
    asyncio.get_event_loop().run_forever()
