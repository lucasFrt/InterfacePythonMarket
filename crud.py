import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="260103",
                                               host="127.0.0.1", port="5432",
                                               database="postgres")
        except(Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Falha ao se conectar ao BD", error)
