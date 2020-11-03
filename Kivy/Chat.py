#Importar o campo info do chat.kv
from logging import info

#Framework kivy para GUIs https://kivy.org/#download
#O arquivo .kv deve ter o mesmo nome que o arquivo .py 
# ao qual ele faz referencia
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

#Permite importar outros arquivos .kv
from kivy.lang import Builder
menuPath = Builder.load_file('menu.kv')
Builder.load_file('Chat.kv')



#Telas da aplicação e gerenciamento das mesmas
class MenuJanela(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def trocar_para_login(self):
        self.current = 'LoginJanela'
        print("Trocou a janela?")

    def trocar_para_cadastrar(self):
        self.current = 'cadastrojanela'

    def trocar_para_chat(self):
        self.current = 'chatjanela'

class Login(Screen):
    pass



#Funções dentro de cada tela
class LoginJanela(Screen):
    print("ENTROU Login Janela")
    def validar_usuario(self):
        print("Validou o user")
        usuario = self.ids.username_field
        senha = self.ids.pwd_field
        info = self.ids.info

        unome = usuario.text
        senha = senha.text

        if unome == '' or senha == "":
            info.text = '[color=#FF0000]Nome de usuário e/ou senha necessário[/color]'
        else:
            if unome=='admin' or unome=='adm' and senha == 'admin' or senha=='adm':
                info.text = ("[color=#00FF00]Logado com sucesso!!![/color]")
            else:
                info.text = '[color=#FF0000]Nome de usuário e/ou senha inválido![/color]'

class CadastroJanela(Screen):
    print("ENTROU Cadastro Janela")
    pass

class ChatJanela(Screen):
    print("ENTROU ChatJanela")
    pass



#Execução
class ChatApp(App):
    def build(self):
        self.MenuJanela = MenuJanela()
        self.LoginJanela = LoginJanela()
        self.ChatJanela = ChatJanela()
        return MenuJanela()

if __name__ == "__main__":
    ChatApp().run()
