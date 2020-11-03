from tkinter import *
from bd import *
#from LogarTela import *

tam = "400x200"


class cadastrarWindow():
    # Construtor da Classe
    def __init__(self):
        self.cadastrarJanela = 0
        self.userEntry2 = 0
        self.passEntry2 = 0
        self.aviso = 0
        self.botaoCadastrar = 0

    # Criar uma janela sem valores
    def cadastrarTela(self):
        # Cria uma janela e define suas principais configurações
        self.cadastrarJanela = Tk()
        self.cadastrarJanela.geometry(tam)
        self.cadastrarJanela.title("Cadastre-se")
        self.cadastrarJanela.wm_iconbitmap('chat.ico')
        self.cadastrarJanela.focus_force()

        # Cria os campos necessários para o cadastro e os posiciona
        lb1 = Label(self.cadastrarJanela, text="Nome de usuário: ")
        lb2 = Label(self.cadastrarJanela, text="Senha: ")
        lb1.grid(row=0, column=0)
        lb2.grid(row=1, column=0)

        # Cria as respectivas entradas de dados e as posiciona
        self.userEntry2 = Entry(self.cadastrarJanela)
        self.passEntry2 = Entry(self.cadastrarJanela)
        self.userEntry2.grid(row=0, column=1)
        self.passEntry2.grid(row=1, column=1)
        self.aviso = Label(self.cadastrarJanela)

        # Cria um botão Cadastrar nessa tela e verifica se é possivel cadastrar o usuario
        self.botaoCadastrar = Button(self.cadastrarJanela, text="Cadastrar!", command=self.cadastrarMetodo)
        self.botaoCadastrar.grid(row=4, column=1)

    def cadastrarMetodo(self):
        if self.userEntry2.get() == "" or self.passEntry2.get() == "":
            # Avisa que deu erro ao cadastrar
            self.aviso = Label(self.cadastrarJanela, text="Digite um nome de usuário e/ou senha!", foreground='red')
            self.aviso.grid(row=2, column=1)
            return 0
        else:
            # Adiciona os dados inseridos no banco de dados
            entradaDados(self.userEntry2.get(), self.passEntry2.get())

            # Avisa que o cadastro deu certo
            self.aviso.destroy()
            self.aviso = Label(
                self.cadastrarJanela, text="Cadastro efetuado com sucesso!", foreground='green')
            self.aviso.grid(row=2, column=1)

            # Altera o botão cadastrar para "Voltar"
            self.botaoCadastrar.destroy()
            self.botaoCadastrar = Button(
                self.cadastrarJanela, text="Voltar", command=self.destroiTela)
            self.botaoCadastrar.grid(row=4, column=1)

    def destroiTela(self):
        self.cadastrarJanela.destroy()
