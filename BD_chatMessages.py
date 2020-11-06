import sqlite3
import os.path

# Variavel Global
caminho = "Bancos de dados/chatMessages.db"

# Cria o arquivo e conecta o cursor para navegar pelo arquivo
connection = sqlite3.connect(caminho)
c = connection.cursor()

def criar_tabela():
    sql = """CREATE TABLE IF NOT EXISTS messages (times text, nome text, message text)"""
    c.execute(sql)


def inserir_msg(times, nome, msg):
    # Verifica se o arquivo usuariosCadastrados existe
    if not(os.path.exists(caminho)):
        print("Não existia")
        criar_tabela()
    else:
        #c.execute("""INSERT INTO messages (times,nome,message) VALUES (? ? ?)""",(times, nome, msg))
        c.execute("INSERT INTO messages (times,nome,message) VALUES ('"+times+"','"+nome+"','"+msg+"')")
    connection.commit()


# Retorna os campos selecionados => Retorna uma lista de tuplas
def seleciona_imprime(campos):
    # Retorna todos os campos do BD
    if campos==0:
        sql = "SELECT times,nome,message FROM messages"
        r = c.execute(sql)
        s = r.fetchall()
        return s
    # Retorna apenas os nomes de usuário sem repetir
    elif campos==1:
        sql = "SELECT DISTINCT nome FROM messages"
        r = c.execute(sql)
        s = r.fetchall()
        return s
    else:
        sql = "SELECT * FROM messages"
        r = c.execute(sql)
        s = r.fetchall()
        return s


def fechaConexao():
    c.close()
    connection.close()