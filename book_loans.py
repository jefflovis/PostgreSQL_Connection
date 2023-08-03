import psycopg2

def listar_emprestimos():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="livraria",
            user="postgres",
            password="Softex2023"
        )

        cursor = connection.cursor()

        # Consulta SQL para obter informações de empréstimos
        query = """
            SELECT p.Nome AS Nome_Pessoa, l.Titulo AS Titulo_Livro
            FROM Pessoa p
            JOIN Emprestimo e ON p.CPF = e.ID_Pessoa
            JOIN Livro l ON e.ID_Livro = l.ID;
        """
        cursor.execute(query)

        # Recuperar todos os resultados
        resultados = cursor.fetchall()

        # Exibir os resultados
        for resultado in resultados:
            print(f"{resultado[0]} pegou o livro '{resultado[1]}'")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao listar os empréstimos:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o banco de dados fechada.")

# Chamada da função para listar os empréstimos
listar_emprestimos()