from tkinter import *
from bd import *
from CadastrarTela import *

tam = "400x200"

class loginWindow():
  def __init__(self):
    self.loginJanela = 0
    self.userEntry = 0
    self.passEntry = 0
    self.aviso = 0
    self.botaoEntrar = 0

  def entrarTela(self):
    # Cria uma janela e define suas principais configurações
    self.loginJanela = Tk()
    self.loginJanela.title("Entre para usar o chat!")
    self.loginJanela.wm_iconbitmap('chat.ico')
    self.loginJanela.focus_force()
    self.loginJanela.geometry(tam)

    # Labels, entradas de texto e botões
    lb1 = Label(self.loginJanela, text="Login: ")
    lb2 = Label(self.loginJanela, text="Senha: ")
    self.userEntry = Entry(self.loginJanela)
    self.passEntry = Entry(self.loginJanela)
    
    self.aviso = Label(self.loginJanela)

      
    self.botaoEntrar = Button(self.loginJanela, text="Entrar", command=self.logarMetodo)
    self.botaoEntrar.grid(row=4, column=1)

    #Posicionamento dos elementos
    lb1.grid(row=0, column=0)
    lb2.grid(row=1, column=0)
    self.userEntry.grid(row=0, column=1)
    self.passEntry.grid(row=1, column=1)
      
      ##############################self.loginJanela.mainloop()
  def logarMetodo(self):
    if self.userEntry.get() == '' or self.passEntry.get() == '':
      # Avisa que faltam dados para fazer o login
      self.aviso = Label(self.loginJanela, text="Digite um nome de usuário e/ou senha!", foreground='red')
      self.aviso.grid(row=2, column=1)
    elif leDados(self.userEntry.get(), self.passEntry.get()):
      # Avisa sobre o sucesso no login
      self.aviso.destroy()
      self.aviso = Label(self.loginJanela, text="Usuario Logado! Você já pode usar o chat!", foreground='green')
      self.aviso.grid(row=2, column=1)
      # Muda o botão entrar para "Abrir chat"
      self.botaoEntrar = Button(self.loginJanela, text="Abrir Chat!")
      self.botaoEntrar.grid(row=4, column=1)
      print("teste")
    else:
      # Avisa ao usuário que ele errou a senha ou nome
      self.aviso.destroy()
      self.aviso = Label(self.loginJanela, text="Usuário e/ou senha inválidos", foreground='red')
      self.aviso.grid(row=2, column=1)

  # Destroi a Tela de Login e CRIA a tela de chat
  def criaChat(self):
      self.loginJanela.destroy()


