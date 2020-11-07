from tkinter import *
from Tela_Cadastrar import *
from Tela_Logar import *

#####################TELA PRINCIPAL DA APLICAÇÃO######################
#Execute esse arquivo


#Variaveis Globais
tam = "500x300"
camIco = "Icones\chat.ico"

# Tela que da a opção de Logar ou cadastrar antes de entrar no chat
class telaInicialWindow():
    # Função construtora da classe tela inicial
    def __init__(self):
        self.tela_inicial = 0
        self.camLoginButton = 0
        self.camCadastrarButton = 0
        self.chatto = 0
        self.bFrame = 0

    # Função que controla toda tela inicial
    def telaInicial(self):
        # Cria uma janela e define suas principais configurações
        self.tela_inicial = Tk()
        self.tela_inicial.title("Logue ou cadastre-se para usar o Chattttô!")
        self.tela_inicial.wm_iconbitmap(camIco)
        self.tela_inicial.focus_force()
        self.tela_inicial.geometry(tam)

        # Converte os pngs dos botões para imagem
        self.camLoginButton = PhotoImage(file="Icones\Botoes\Login.png", master=self.tela_inicial)
        self.camCadastrarButton = PhotoImage(file="Icones\Botoes\Cadastrar.png", master=self.tela_inicial)
        self.chatto = PhotoImage(file="Icones\Chatto.png", master=self.tela_inicial)

        # Coloca uma imagem em cima dos botões
        l1 = Label(image=self.chatto)
        l1.place(relx=0.5, rely=0.25, anchor="n")

        # Cria instancias e botões para Logar e Cadastrar
        ltela = loginWindow()
        ctela = cadastrarWindow()
        botaoLogar = Button(command=ltela.entrarTela, image=self.camLoginButton, bd=0, relief=GROOVE)
        botaoCadastrar = Button(command=ctela.cadastrarTela, image=self.camCadastrarButton, bd=0, relief=GROOVE)

        # Posicionamento dos botões
        botaoLogar.place(relx=0.3, rely=0.7, anchor="s")
        botaoCadastrar.place(relx=0.7, rely=0.7, anchor="s")

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.tela_inicial.mainloop()


x1 = telaInicialWindow()
x1.telaInicial()
