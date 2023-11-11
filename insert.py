import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="260103", port="5432")
print("Conexão realizada com sucesso")

comando = conn.cursor()
comando.execute("""INSERT INTO Produtos (codigo,nome, preco))
""")

conn.commit()
print("Inserção realizada com sucesso!")
conn.close()
