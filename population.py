import psycopg2

# Função para criar as tabelas
def criar_tabelas():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="livraria",
            user="postgres",
            password="Softex2023"
        )

        cursor = connection.cursor()

        # Criação da tabela Livro
        cursor.execute("""
            CREATE TABLE Livro (
                ID SERIAL PRIMARY KEY,
                Titulo VARCHAR(100) NOT NULL,
                Altura NUMERIC NOT NULL,
                Largura NUMERIC NOT NULL
            )
        """)

        # Criação da tabela Pessoa
        cursor.execute("""
            CREATE TABLE Pessoa (
                CPF VARCHAR(14) PRIMARY KEY,
                Nome VARCHAR(100) NOT NULL,
                Rua VARCHAR(100) NOT NULL,
                Numero VARCHAR(10) NOT NULL,
                Apartamento VARCHAR(10) NOT NULL
            )
        """)

        # Criação da tabela Emprestimo
        cursor.execute("""
            CREATE TABLE Emprestimo (
                ID SERIAL PRIMARY KEY,
                ID_Pessoa VARCHAR(14) REFERENCES Pessoa(CPF),
                ID_Livro INTEGER REFERENCES Livro(ID),
                Data_emprestimo DATE NOT NULL
            )
        """)

        connection.commit()
        print("Tabelas criadas com sucesso!")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao criar as tabelas:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o banco de dados fechada.")

# Função para popular as tabelas
def popular_tabelas():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="livraria",
            user="postgres",
            password="Softex2023"
        )

        cursor = connection.cursor()

        # Inserção de dados na tabela Livro
        cursor.execute("""
            INSERT INTO Livro (Titulo, Altura, Largura)
            VALUES ('Livro A', 25, 15),
                   ('Livro B', 20, 12),
                   ('Livro C', 30, 18)
        """)

        # Inserção de dados na tabela Pessoa
        cursor.execute("""
            INSERT INTO Pessoa (CPF, Nome, Rua, Numero, Apartamento)
            VALUES ('111.111.111-11', 'João', 'Rua A', '123', 'Ap 4'),
                   ('222.222.222-22', 'Maria', 'Rua B', '456', 'Ap 7'),
                   ('333.333.333-33', 'Pedro', 'Rua C', '789', 'Ap 12')
        """)

        # Inserção de dados na tabela Emprestimo
        cursor.execute("""
            INSERT INTO Emprestimo (ID_Pessoa, ID_Livro, Data_emprestimo)
            VALUES ('111.111.111-11', 1, '2023-07-10'),
                   ('222.222.222-22', 2, '2023-07-15'),
                   ('111.111.111-11', 3, '2023-07-20'),
                   ('333.333.333-33', 1, '2023-07-25')
        """)

        connection.commit()
        print("Dados inseridos com sucesso!")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao popular as tabelas:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o banco de dados fechada.")

# Chamada das funções
criar_tabelas()
popular_tabelas()
