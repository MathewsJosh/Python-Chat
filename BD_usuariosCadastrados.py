import sqlite3
import os.path

# Deleta o arquivo de dados de chat se o mesmo existir
os.remove("Bancos de dados/usuariosCadastrados.db")

# Variavel global
caminho = "Bancos de dados/usuariosCadastrados.db"

# Verifica se o arquivo usuariosCadastrados existe
existe = os.path.exists(caminho)

# Cria o arquivo
connection = sqlite3.connect(caminho)

# Navega pelo arquivo
c = connection.cursor()

# Método de criação da tabela do banco de dados
def criar_tabela():
    c.execute(
        """CREATE TABLE IF NOT EXISTS dados (
            nome text,
            senha text,
            UNIQUE(nome)
            )""")

# Método auxiliarde entrada de dados e criação de tabela
def entradaauxiliar():
    criar_tabela()
    c.execute("INSERT OR IGNORE INTO dados (nome, senha) VALUES ('admin', 'admin')")
    c.execute("INSERT OR IGNORE INTO dados (nome, senha) VALUES ('adm', 'adm')")
    connection.commit()

# Método de entrada dos dados do usuário para o cadastramento
def entradaDados(nome, senha):
    criar_tabela()
    c.execute("INSERT OR IGNORE INTO dados (nome, senha) VALUES ('admin', 'admin')")
    c.execute("INSERT OR IGNORE INTO dados (nome, senha) VALUES ('adm', 'adm')")
    c.execute("INSERT OR REPLACE INTO dados (nome, senha) VALUES ('"+nome+"','"+senha+"')")
    connection.commit()

# Método que retorna o nome e senha do usuário cadastrado
def leDados(nome,senha):
    entradaauxiliar()
    sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
    for linha in c.execute(sql, (nome,senha,)):
        if linha == "":
            return False
        else:
            return True

# Método que fecha a conexão com o banco de dados(nunca usado)
def fechaConexao():
    c.close()
    connection.close()
