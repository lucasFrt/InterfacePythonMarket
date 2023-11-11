import tkinter as tk
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

    def inserirDados(self, codigo, nome, preco):
        try:

            new_preco = float(preco) * 1.1
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."produtos"
            ("codigo", "nome", "preco") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, new_preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def atualizarDados(self, codigo, nome, preco):
        try:
            novo_preco = float(preco) * 1.1
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_update_query = """Update public."produtos" set "nome" = %s,
            "preco" = %s where "codigo" = %s"""
            cursor.execute(sql_update_query, (nome, novo_preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = """select * from public."produtos"
            where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public."produtos"
            where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")


class PrincipalBD:
    def __init__(self, win):
        self.objBD = AppBD()

        # elementos visuais
        self.lbTitulo = tk.Label(win, text='PyMarket Register ')
        self.lbCodigo = tk.Label(win, text='Codigo de produto: ')
        self.lblNome = tk.Label(win, text='Nome do produto: ')
        self.lblPreco = tk.Label(win, text='Preço do produto: ')

        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProdutos)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text="Exluir", command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.fLimparTela)

        self.lblNovoPreco = tk.Label(win, text='Preco com adicao dos 10% : ')
        self.lblNovoPreco.place(x=100, y=300)

        self.lbTitulo.place(x=250, y=25)

        # Posição dos botoes
        self.lbCodigo.place(x=100, y=100)

        self.txtCodigo.place(x=250, y=100)

        self.lblNome.place(x=100, y=150)
        self.txtNome.place(x=250, y=150)

        self.lblPreco.place(x=100, y=200)
        self.txtPreco.place(x=250, y=200)

        self.btnCadastrar.place(x=100, y=250)
        self.btnAtualizar.place(x=200, y=250)
        self.btnExcluir.place(x=300, y=250)
        self.btnLimpar.place(x=400, y=250)

    def fCadastrarProdutos(self):
        try:
            codigo, nome, preco = self.fLerCampos
            novo_preco = float(preco) * 1.1
            self.objBD.inserirDados(codigo, nome, preco)
            self.lblNovoPreco.config(text=f'Preco com adicao dos 10% : {novo_preco}')
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')

        except:
            print('Não foi possível fazer o cadastro.')
        return codigo, nome, preco


    @property
    def fLerCampos(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        return codigo, nome, preco

    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')


    def fExcluirProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')


    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """INSERT INTO public."PRODUTO"
            ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")


janela = tk.Tk()
janela.configure(background='#EBEFBF')
principal = PrincipalBD(janela)
janela.title('Registro de produtos')
janela.geometry("600x400")
janela.mainloop()