import os
import time
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

class Config:
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
# Conexão com o banco de dados
# OBJETIVO OBRIGATÓRIO: É necessário preencher os parâmetros dbname, user, password, host e port com os respectivos valores configurados na criação do banco de dados.
# OBJETIVOS OPTATIVOS: (i) há um problema relacionado à segurança das informações; (ii) há outro problema relacionado às boas práticas de programação: DICA: será que o objeto 'conn' não poderia ser criado em outro lugar e retornado para cá de uma forma mais elegante?
def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=Config.DB_NAME,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                host=Config.DB_HOST,
                port=Config.DB_PORT
            )
            return conn
        except psycopg2.OperationalError as e:
            print("Database connection failed. Retrying in 5 seconds...")
            time.sleep(5)

# Conexão com o banco de dados
conn = connect_to_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    consulta_resultado = None
    colunas = None
    erro = None

    if request.method == 'POST':
        comando_sql = request.form['comandoSQL']
        cursor = conn.cursor()

        try:
            cursor.execute(comando_sql)
            rows = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]  # Obtém os nomes das colunas
            conn.commit()
            
        except psycopg2.Error as e:
            # OBJETIVO OBRIGATÓRIO: é necessário preencher esse bloco de código caso a query digitada seja inválida.
            # DICA: É necessário criar uma mensagem de erro que mostre o erro ocorrido no BD e cancelar a consulta problemática no banco de dados a partir de um procedimento chamado 'rollback'. Pesquisar na documentação do psycopg2.
            
            conn.rollback()  # Rollback em caso de erro no SQL
            erro = f"Erro ao executar a query SQL: {e}"
            rows = []
        finally:
            cursor.close()

        consulta_resultado = rows

    return render_template('index.html', consulta_resultado=consulta_resultado, colunas=colunas, erro=erro)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

