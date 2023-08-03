import psycopg2

def contar_livros_estante():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="livraria",
            user="postgres",
            password="Softex2023"
        )

        cursor = connection.cursor()

        # Consulta SQL para contar os livros na estante
        query = "SELECT COUNT(*) FROM Livro;"
        cursor.execute(query)

        # Recuperar o resultado
        quantidade_livros = cursor.fetchone()[0]

        print(f"Quantidade de livros na estante: {quantidade_livros}")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao contar os livros:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o banco de dados fechada.")


# Chamada da função para contar os livros
contar_livros_estante()


