from kivy.app import App
from kivy.app import Widget

class Tela(Widget):
    pass
class teste():
    def chama(self):
        print("chama")
        pass
    def save_d(self):
        pass

class teste1():
    def peido(self):
        print("pufff")
        pass

class Prg(App):
    def build(self):
        self.teste = teste()
        self.teste1 = teste1()
        return Tela()

Prg().run()