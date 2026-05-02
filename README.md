# 🕷️ Web Scraper de Preços + Alertas Automáticos
> Monitora preços em e-commerces e envia alertas via Slack/WhatsApp quando há promoções

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-Async-45ba4b)](https://playwright.dev/python)
[![Redis](https://img.shields.io/badge/Redis-Cache-DC382D?logo=redis)](https://redis.io)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://docker.com)
[![Demo](https://img.shields.io/badge/🚀_Demo-Online-00C851)](https://gabriel-price-tracker.streamlit.app)

## 🎯 Sobre

Sistema de **monitoramento de preços** que rastreia produtos em múltiplos e-commerces e envia notificações automáticas quando o preço cai abaixo de um valor configurado. Inclui dashboard com histórico de preços e gráficos de tendência.

- 🛒 Suporta: Mercado Livre, Amazon BR, Magazine Luiza
- ⚡ Processa **10.000 produtos/dia** com scraping assíncrono
- 📊 Dashboard com histórico de preços e análise de tendências
- 🔔 Alertas via **Slack**, **WhatsApp** e **e-mail**

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| Scraping | Playwright (asyncio) |
| Parser | BeautifulSoup4 |
| Cache/Fila | Redis |
| Banco de dados | PostgreSQL |
| Agendamento | APScheduler |
| Dashboard | Streamlit + Plotly |
| Alertas | Slack API + Evolution API (WhatsApp) + smtplib |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/price-tracker-alerts
cd price-tracker-alerts

cp .env.example .env
playwright install chromium
docker compose up --build
# Dashboard: http://localhost:8501
```

## 📂 Estrutura

```
price-tracker-alerts/
├── scraper/
│   ├── main.py
│   ├── workers.py
│   └── parsers/
│       ├── mercadolivre.py
│       ├── amazon_br.py
│       └── magalu.py
├── alerts/
│   ├── slack_alert.py
│   ├── whatsapp_alert.py
│   └── email_alert.py
├── dashboard/
│   ├── app.py
│   └── pages/
├── config/tracking.yaml
└── docker-compose.yml
```

## 📈 Resultados

- ⚡ **10.000 produtos/dia** em ~2.5h
- 🎯 **97.3%** taxa de sucesso no scraping
- 🔔 Latência de alerta: **< 5 minutos** após queda
- 💰 Já identificou descontos de até **45%** antes da divulgação oficial

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
