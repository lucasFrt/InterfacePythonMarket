###import os
###os.system("pip install psycopg2")

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="260103", port="5432")
print("Conexão com o Banco de dados realizada com sucesso!")

comando = conn.cursor()
comando.execute(""" CREATE TABLE Produtos
(nome TEXT NOT NULL,
codigo int NOT NULL,
preco VARCHAR(12));
""")

conn.commit()

print("Tabela criada com sucesso!")
conn.close()