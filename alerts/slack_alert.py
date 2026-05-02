"""Envia alertas de preço via Slack Webhook."""
import os
import requests
from datetime import datetime


def send_slack_alert(product: dict, current_price: float):
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook:
        print("⚠️ SLACK_WEBHOOK_URL não configurada")
        return

    message = {
        "text": f"🔔 *Alerta de Preço!*",
        "blocks": [
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*{product['name']}*"}},
            {"type": "section", "fields": [
                {"type": "mrkdwn", "text": f"*Preço atual:*
R$ {current_price:,.2f}"},
                {"type": "mrkdwn", "text": f"*Seu limite:*
R$ {product['max_price']:,.2f}"},
            ]},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"<{product['url']}|🛒 Comprar agora>"}},
        ],
    }
    requests.post(webhook, json=message)
