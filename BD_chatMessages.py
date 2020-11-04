import sqlite3
import os.path

caminho = "Bancos de dados/chatMessages.db"

# Verifica se o arquivo usuariosCadastrados existe
existe = os.path.exists(caminho)

# Cria o arquivo
connection = sqlite3.connect(caminho)

# navega pelo arquivo
c = connection.cursor()

def criar_tabela():
    c.execute(
        """CREATE TABLE IF NOT EXISTS messages (
            times text,
            nome text,
            message text,
            data BLOB
            )""")


def inserir_img(times, nome, filename):
    if existe == False:
        criar_tabela()
    else:
        with open(filename, 'rb') as f:
            data=f.read()
        c.execute("""INSERT INTO messages (
            times, 
            nome,  
            data) 
            VALUES (? ? ?)""",(times, nome, data))
    connection.commit()

def inserir_msg(times, nome, msg):
    if existe == False:
        print("Não existia")
        criar_tabela()
    else:
        #c.execute("""INSERT INTO messages (times,nome,message) VALUES (? ? ?)""",(times, nome, msg))
        c.execute("INSERT INTO messages (times,nome,message) VALUES ('"+times+"','"+nome+"','"+msg+"')")
    connection.commit()

#VALUES (? ? ?)""",(times, nome, message))

def exibir_tabela():
    m = c.execute("""SELECT * FROM messages""")
    #for x in range(len(m)):
    for x in m:
        print(x)

def impressora():
    #print("impressora")
    sql = "SELECT times,nome,message FROM messages"
    r = c.execute(sql)
    s = r.fetchall()
    
    #for x in s:
     #   print(x)
    return s



def fechaConexao():
    c.close()
    connection.close()