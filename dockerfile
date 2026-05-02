# Usamos a imagem oficial do Playwright. Ela é baseada em Ubuntu e já tem tudo pronto.
FROM mcr.microsoft.com/playwright:v1.44.0-jammy

# Configurações padrão de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala apenas dependências básicas de compilação para o psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as bibliotecas do projeto
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Expondo a porta do Streamlit
EXPOSE 8501

CMD ["streamlit", "run", "dashboard/app.py"]