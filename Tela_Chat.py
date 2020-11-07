# Tkinter imports
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as scrolledtext
import tkinter.font as tkFont

# Funçoes imports
import random
from datetime import datetime

# Imports do banco de Dados
from BD_chatMessages import *

# Variáveis globais
tam = "600x400"
camIco = "Icones\chat.ico"


# Classe da Janela de chat
class chatWindow():
    # Função construtora da classe
    def __init__(self, nome):
        self.chatJanela = 0
        self.textbox = 0
        self.msgbox = 0
        self.botaoenviar = 0
        self.botaoatt = 0
        self.filename = ""
        self.bFrame = 0
        self.data_e_hora_em_texto = 0
        self.nome = nome
        self.cor = "black"
        self.clipPng = "Icones\clippng.png"
        self.tamFrase = 0
        self.camAtualizarButton = 0
        self.camEnviarButton = 0


    #---------------------------MAIN------------------------------#

    # Função MAIN da tela de chat => Gerencia tudo o que pode acontecer 
    def chatTela(self):
        # Chamada de funções de formatação
        self.formata_janela()

        # Envia a entrada do usuário para o banco de dados
        self.botaoenviar = Button(self.bFrame, text="Enviar mensagem", command=self.envia_msgs, image=self.camEnviarButton, bd=0, relief=GROOVE)
        self.botaoenviar.grid(row=0, column=2, padx=10, pady=10)

        self.botaoatt = Button(self.bFrame, text="Atualizar\nmensagens", command=self.atualiza_textbox, image=self.camAtualizarButton, bd=0, relief=GROOVE)
        self.botaoatt.grid(row=0, column=0, padx=10, pady=10)

        # Indica que a tela atual sempre estará em loop (comando obrigatório do Tkinter para a tela funcionar)
        self.chatJanela.mainloop()


    
    #---------------------------GERENCIAMENTO DO CHAT------------------------------#


    # Método responsável por enviar a mensagem digitada diretamente para o BD
    def envia_msgs(self):
        msg = self.msgbox.get("1.0", "end")
        

        # Se houver algo escrito, manda pro BD
        if len(msg) > 1:
            # Calcula o timestamp e apaga a caixa de texto onde o user escreveu
            self.datamsg()
            #self.apaga_msgbox()
            self.apaga_chatbox()
            
            # Envia pro BD
            criar_tabela()
            inserir_msg(self.data_e_hora_em_texto, self.nome, msg)

            self.atualiza_textbox()
            



    # Função responsavel por atualizar o bate papo com as msgs do BD
    def atualiza_textbox(self):
        self.apaga_chatbox()
        aux = seleciona_imprime(0)
    
        # Formata e insere linha por linha do banco de dados no textbox
        for x in aux:
            self.textbox.insert(INSERT, x[0])
            self.textbox.insert(INSERT, " - ")
            self.textbox.insert(INSERT, x[1])
            self.textbox.insert(INSERT, ": ")
            self.textbox.insert(INSERT, x[2])
            

        self.textbox.yview_moveto(1)
        self.pesquisa_usuario()

        self.apaga_msgbox()

        # Função necessária para não permitir que o textbox seja editado
        self.textbox.bind("<Key>", lambda e: "break")
            

    # Busca o nome do usuário no textbox, marca-o com uma tag e colore seu nome
    def pesquisa_usuario(self):
        # Remove a tag 'found' do index 1 até o final (END)
        self.textbox.tag_remove('found', '1.0', END)
        
        # Se o usuário existir, vamos colorir seu nome
        if self.nome:
            # Index do começo da string no ScrooledText é sempre 1.0
            idx = '1.0'
            while 1:
                #Encontra a string desejada a partir do index 1
                idx = self.textbox.search(self.nome, idx, nocase=1, stopindex=END)

                # Se não encontra a String, sai do loop
                if not idx:
                    break

                # Ultima soma de posição da posição atual e do tamanho do texto
                lastidx = '%s+%dc' % (idx, len(self.nome))
                
                # Marca a palavra encontrada com uma tag 'found'
                self.textbox.tag_add('found', idx, lastidx)
                idx = lastidx

            # Marca a string encontrada com uma cor
            self.textbox.tag_config('found', foreground=self.cor)


    #---------------------------MÉTODOS AUXILIARES------------------------------#

    # Escolhe radomicamente uma cor da lista para ser a cor daquele user
    def random_colors(self, x):
        cores = ["yellow","blue", "navy blue", "gold", "orange", "brown", "pink", "purple", "green", "red", "violet"]
        if x==0:
            self.cor = random.choice(cores)
        else:
            return random.choice(cores)

    # Calcula o timestamp da msg e retorna já formatado
    def datamsg(self):
        data_e_hora_atuais = datetime.now()
        self.data_e_hora_em_texto = data_e_hora_atuais.strftime(
            "%d/%m/%Y %H:%M:%S")

    # Apaga a caixa de bate-papo (onde as mensagens são exibidas)
    def apaga_chatbox(self):
        #self.textbox.destroy()
        self.textbox.delete(1.0, END)
    
    # Apaga a caixa de mensagem
    def apaga_msgbox(self):
        self.msgbox.delete(1.0, END)



    #---------------------------DESIGN & FORMATAÇÃO DA JANELA------------------------------#

    # Função responsável por formatar a janela da aplicação
    def formata_janela(self):
        # Definiçoes iniciais
        self.chatJanela = Tk()
        self.chatJanela.title("Chattttô!")
        self.chatJanela.wm_iconbitmap(camIco)
        self.chatJanela.focus_force()
        
        #Codigo para centralizar a Janela na tela
        self.chatJanela.withdraw()
        self.chatJanela.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.chatJanela.winfo_screenwidth() - self.chatJanela.winfo_reqwidth()) / 3
        y = (self.chatJanela.winfo_screenheight() - self.chatJanela.winfo_reqheight()) / 3
        self.chatJanela.geometry("+%d+%d" % (x, y))
        self.chatJanela.deiconify()

        # Define a cor do usuário
        self.random_colors(0)

        fontfamilylist = list(tkFont.families())
        fontindex = 0
        fontStyle = tkFont.Font(family=fontfamilylist[fontindex])

        # Tela onde aparecem as mensagens enviadas => atualiza a medida que são enviadas novas mensagens
        self.textbox = scrolledtext.ScrolledText(self.chatJanela, height=15, width=80, font=fontStyle)
        self.textbox.pack(padx=20, pady=20)
        self.textbox.insert(1.0, "Bem Vindo ao Chattttô @" + self.nome + "!!!\n")

        # Esse frame é uma especie de "caixa" que posiciona elementos dentro dele com o .grid
        self.bFrame = Frame(self.chatJanela)
        self.bFrame.pack()

        # Entrada de texto do usuário
        self.msgbox = Text(self.bFrame, height=3, width=40, font=fontStyle)
        self.msgbox.grid(row=0, column=1, padx=20, pady=20)
        self.msgbox.focus_force()

        #Converte os pngs dos botões para imagem
        self.camAtualizarButton = PhotoImage(file="Icones\Botoes\Atualizar.png", master=self.chatJanela)
        self.camEnviarButton = PhotoImage(file="Icones\Botoes\Enviar.png", master=self.chatJanela)



# Testes apenas para essa tela
#c = chatWindow("Julho")
#c.chatTela()



#Codigos descartados:
"""
#Calcula o tamanho da ultima frase inserida (sem a mensagem)
self.tamFrase = (len(x[0]) + 3 + len(x[1]) + 2)

# Botão anexar => anexa uma imagem à mensagem e a envia para o chat imediatamente
self.botaoanexar = Button(self.botaoFrame, text="Anexar\narquivo", command=self.abrir_imagem)
self.botaoanexar.grid(row=0, column=1, padx=10, pady=10)

# Coloca um icone de clip no botão anexar
clip2 = PhotoImage(file=self.clipPng)
clip3 = clip2.subsample(20, 20)
self.botaoanexar.config(image=clip3, compound=RIGHT)

root["bg"] = "black"

# A ideia era ter um botão de anexar arquivo e enviar as imagens para o chat
# DEVE ENVIAR A IMAGEM PARA O TEXTBOX/BD IMEDIATAMENTE
    def abrir_imagem(self):
        try:
            self.filename = askopenfilename()
            #inserir_tabela(self.data_e_hora_em_texto, "Pedro", self.filename)
            print(self.filename)
        except:
            print("Erro ao abrir o arquivo!")
#https://www.youtube.com/watch?v=VvM-uAp9zW8&ab_channel=soumilshah1995
#https://www.youtube.com/watch?v=T4niJOZB4PI&ab_channel=Ssj6


# A ideia era deixar cada usuário com uma cor diferente
# Retorna todos os usuários do chat
aux2 = seleciona_imprime(1)
aux2.pop(aux2.index((self.nome,)))
for x in aux2:
    aux3 = str(x).strip('(,\')')
    self.pesquisa_usuario(aux3)



###############################################BANCO DE DADOS

def inserir_img(times, nome, filename):
    if existe == False:
        criar_tabela()
    else:
        with open(filename, 'rb') as f:
            data=f.read()
        sql = "INSERT INTO messages (times, nome,  data) VALUES (? ? ?)",(times, nome, data)
        c.execute(sql)
    connection.commit()

"Não tem mais data BLOB"
def criar_tabela():
    sql="CREATE TABLE IF NOT EXISTS messages (times text,nome text,message text,data BLOB)"
    c.execute(sql)   

"""



# Referências
"""
https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#lendo-as-informacoes-do-banco-de-dados
https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/
https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
http://buttonoptimizer.com/

"""