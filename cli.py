import argparse
import psycopg2
from os import getenv
from dotenv import load_dotenv

# Carrega as variáveis do seu arquivo .env
load_dotenv()

DATABASE_URL = getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/pricetracker")

def add_product(url, name, max_price):
    try:
        # Conecta ao Postgres que você subiu no Docker
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        
        # Insere o produto na tabela (ajuste os nomes das colunas conforme seu schema)
        query = """
        INSERT INTO products (url, name, max_price, created_at)
        VALUES (%s, %s, %s, NOW())
        ON CONFLICT (url) DO UPDATE SET max_price = EXCLUDED.max_price;
        """
        cur.execute(query, (url, name, max_price))
        
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Produto '{name}' adicionado/atualizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao conectar no banco de dados: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Price Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Comando add-product
    add_parser = subparsers.add_parser("add-product")
    add_parser.add_argument("--url", required=True, help="URL do produto no Mercado Livre")
    add_parser.add_argument("--name", required=True, help="Nome amigável do produto")
    add_parser.add_argument("--max-price", type=float, required=True, help="Preço alvo para alerta")

    args = parser.parse_args()

    if args.command == "add-product":
        add_product(args.url, args.name, args.max_price)
    else:
        parser.print_help()