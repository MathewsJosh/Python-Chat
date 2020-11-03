from tkinter import *
from bd import *
from CadastrarTela import *
from LogarTela import *

# Tela de Login e/ou cadastro
# largura,altura, +deslocamento margem esquerda, +deslocamento do topo
tam = "400x200"


# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class telaInicialWindow():
    def __init__(self):
        self.tela_inicial = 0
        self.x = 1

    def telaInicial(self):
        # Cria uma janela e define suas principais configurações
        self.tela_inicial = Tk()
        self.tela_inicial.title("Logue ou cadastre-se para usar o chat!")
        self.tela_inicial.wm_iconbitmap('chat.ico')
        self.tela_inicial.focus_force()
        self.tela_inicial.geometry(tam)

        # Cria instancias e botões para Logar e Cadastrar
        ltela = loginWindow()
        ctela = cadastrarWindow()
        botaoLogar = Button(text="Entrar", height=4, width=20, command=ltela.entrarTela)
        botaoCadastrar = Button(text="Cadastrar", height=4, width=20, command=ctela.cadastrarTela)
        
        # Posicionamento dos botões
        botaoLogar.place(relx=0.3, rely=0.5, anchor=CENTER)
        botaoCadastrar.place(relx=0.7, rely=0.5, anchor=CENTER)

        self.tela_inicial.mainloop()


x1 = telaInicialWindow()
x1.telaInicial()
