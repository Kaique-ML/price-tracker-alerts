"""Dashboard Streamlit para o Price Tracker."""
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Price Tracker", layout="wide")
st.title("🕷️ Price Tracker — Monitor de Preços")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Produtos Monitorados", "42", "+3")
col2.metric("Verificações Hoje", "21", "")
col3.metric("Alertas Disparados", "7", "🔔")
col4.metric("Taxa de Sucesso", "97.3%", "+0.5%")

st.subheader("📈 Histórico de Preço — Notebook Dell XPS")
dates = [datetime.now() - timedelta(days=i) for i in range(30, 0, -1)]
prices = [3200 + random.randint(-200, 200) for _ in dates]
df = pd.DataFrame({"Data": dates, "Preço": prices})
df["Limite"] = 2500
fig = px.line(df, x="Data", y=["Preço", "Limite"], title="Evolução do Preço")
st.plotly_chart(fig, use_container_width=True)
