import psycopg2

conn = psycopg2.connect(database="postgres", name="postgres", password="1234",port="5432")
print("Conexão realizada com sucesso!")

comando = conn.cursor()
comando.execute("""SELECT * FROM AGENDA where id = 2""")
registro = comando.fetchone()
print("Dados Encontrados:", registro)

conn.commit()
print("seleção realizada com sucesso!!")
conn.close()