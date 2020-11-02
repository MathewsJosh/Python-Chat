from logging import info
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#Framework kivy para GUIs https://kivy.org/#download
#O arquivo .kv deve ter o mesmo nome que o arquivo .py 
# ao qual ele faz referencia


#Janelas
class LoginJanela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validar_usuario(self):
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


class CadastroJanela(BoxLayout):
    pass



class ScreenManagement(ScreenManager):

class LoginApp(App):
    def build(self):
        return LoginJanela()


if __name__=="__main__":
    sa = LoginApp()
    sa.run()
