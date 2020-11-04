#from sqlite3.dbapi2 import Timestamp
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.scrolledtext as scrolledtext
import random
import sys
#from termcolor import colored
#conda install -c conda-forge colored
from colored import fg, bg, attr

#conda install -c omnia termcolor

from BD_chatMessages import *
from datetime import datetime

tam = "600x400"
camIco="Icones\chat.ico"
clipPng="Icones\clippng.png"

class chatWindow():
    def __init__(self, nome):
        self.chatJanela = 0
        self.textbox = 0
        self.msgbox = 0
        self.botaoenviar = 0
        self.botaoanexar= 0
        self.filename = ""
        self.data_e_hora_em_texto = 0
        self.nome = nome
        self.cor = "black"

    def chatTela(self):
        self.chatJanela = Tk()
        self.chatJanela.title("Chattttô!")
        self.chatJanela.wm_iconbitmap(camIco)
        self.chatJanela.focus_force()
        self.chatJanela.geometry(tam)

        #Define a cor do usuário
        self.random_colors()

        #, state=DISABLED
        self.textbox = scrolledtext.ScrolledText(self.chatJanela, height=15, width=80)
        self.textbox.pack(padx=20, pady=20)
        
        self.textbox.insert(1.0,"Bem Vindo ao Chattttô!!!\n")
        #self.textbox.config(state="disabled")
        

        self.botaoFrame = Frame(self.chatJanela)
        self.botaoFrame.pack()
        #,foreground=set.color
        self.msgbox = Text(self.botaoFrame, height=3, width=40)
        self.msgbox.grid(row=0, column=0, padx=20, pady=20)
        self.msgbox.focus_force()

        self.botaoanexar = Button(self.botaoFrame, text="Anexar\narquivo", command=self.abrir_imagem)
        self.botaoanexar.grid(row=0, column=1, padx=10, pady=10)
        clip2= PhotoImage(file=clipPng)
        clip3= clip2.subsample(20,20)
        self.botaoanexar.config(image=clip3,compound=RIGHT)
        
        self.botaoenviar = Button(self.botaoFrame, text="Enviar mensagem", command=self.envia_msgs)
        self.botaoenviar.grid(row=0, column=2, padx=10, pady=10)

        
        self.chatJanela.mainloop()

    def abrir_imagem(self):
        try:
            self.filename = askopenfilename()
            #inserir_tabela(self.data_e_hora_em_texto, "Pedro", self.filename)
            print(self.filename)
        except:
            print("Erro ao abrir o arquivo!")

    def envia_msgs(self):
        msg = self.msgbox.get("1.0","end")

        #Se houver algo escrito, manda pro BD
        if len(msg) != 1:
            #Chamada de funções => sem retorno
            self.datamsg()
            self.apaga_msgbox()
            criar_tabela()
            inserir_msg(self.data_e_hora_em_texto, "Pedro", msg)
            #self.textbox.insert(INSERT,msg)
            self.textbox.focus_force()
            aux = impressora()
            
            # Formata e insere linha por linha do banco de dados no textbox
            for x in aux:
                self.textbox.insert(INSERT, x[0])
                self.textbox.insert(INSERT, " - ")
                self.textbox.insert(INSERT, x[1])
                self.textbox.insert(INSERT, " : ")
                self.textbox.insert(INSERT, x[2])
                #self.textbox.insert(INSERT, "\n")

            print(self.cor)
            self.textbox.yview_moveto(1)
            self.find(self.textbox)
            
    #Busca o nome do usuário no textbox e o marca com a tag e colore seu nome
    #https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
    def find(self,msg): 
        #remove tag 'found' from index 1 to END 
        self.textbox.tag_remove('found', '1.0', END)  
        
        #returns to widget currently in focus 
        s = "Pedro" 
        if s: 
            idx = '1.0'
            while 1: 
                #searches for desried string from index 1 
                idx = self.textbox.search(s, idx, nocase=1,  
                                stopindex=END)  
                if not idx: break
                
                #last index sum of current index and 
                #length of text 
                lastidx = '%s+%dc' % (idx, len(s))  
                
                #overwrite 'Found' at idx 
                self.textbox.tag_add('found', idx, lastidx)  
                idx = lastidx 
            
            #mark located string as red 
            self.textbox.tag_config('found', foreground=self.cor)  
        msg.focus_set() 
        #self.textbox.config(command=find)         

    def random_colors(self):
        COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'antique white', 'papaya whip', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 
        'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 
        'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise']
        self.cor=random.choice(COLORS)

    # Calcula o timestamp da msg e retorna já formatado
    def datamsg(self):
        data_e_hora_atuais = datetime.now()
        self.data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
    
    def apaga_chatbox(self):
        self.textbox.destroy()
    # Apaga a caixa de mensagem
    def apaga_msgbox(self):
        self.msgbox.delete(1.0, END)


#c = chatWindow("pedro")
#c.chatTela()




#"Passar o usuario como parametro de s para mudar de cor"
#"Cores Foreground aleatorias entre usuarios"
#"Toda vez que o programa inicia, deletar o chat antes de cria-lo"
#"bem vindo @pedro!"