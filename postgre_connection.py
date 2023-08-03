import psycopg2

def connect_to_postgres():
    try:
        # Parâmetros de conexão com o banco de dados PostgreSQL
        connection = psycopg2.connect(
            user="postgres",
            password="Softex2023",
            host="localhost",
            port="5432",
            database="livraria"
        )

        # Cria um cursor para executar operações SQL
        cursor = connection.cursor()

        # Exemplo de execução de uma consulta SQL
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        print("Conexão bem-sucedida.")
        print("Versão do PostgreSQL:", version)

        # Não esqueça de fechar o cursor e a conexão após o uso
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)

# Chamando a função de conexão
connect_to_postgres()
