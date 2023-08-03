import psycopg2

def encontrar_emprestimo_por_nome_livro():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="livraria",
            user="postgres",
            password="Softex2023"
        )

        while True:
            cursor = connection.cursor()

            # Perguntar o nome do livro
            titulo_livro = input("Digite o nome do livro (ou [n] para sair): ")

            if titulo_livro.lower() == "n":
                break

            # Consulta SQL para encontrar o endereço da pessoa e a data do empréstimo
            query = """
                SELECT p.Nome, p.Rua, p.Numero, p.Apartamento, e.Data_emprestimo
                FROM Pessoa p
                JOIN Emprestimo e ON p.CPF = e.ID_Pessoa
                JOIN Livro l ON e.ID_Livro = l.ID
                WHERE l.Titulo = %s;
            """
            cursor.execute(query, (titulo_livro,))

            # Recuperar o resultado
            resultado = cursor.fetchone()

            if resultado:
                nome_pessoa, rua, numero, apartamento, data_emprestimo = resultado
                endereco_pessoa = f"{rua}, {numero}, {apartamento}"
                print(f"O livro '{titulo_livro}' foi pego por {nome_pessoa}. Endereço: {endereco_pessoa}. Data do empréstimo: {data_emprestimo}")
            else:
                print(f"O livro '{titulo_livro}' não foi encontrado na estante ou ainda não foi emprestado.")

            cursor.close()

    except (Exception, psycopg2.Error) as error:
        print("Erro ao realizar a consulta:", error)

    finally:
        if connection:
            connection.close()
            print("Conexão com o banco de dados fechada.")

# Chamada da função para encontrar o endereço e a data do empréstimo do livro informado pelo usuário
encontrar_emprestimo_por_nome_livro()


