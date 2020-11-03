from PySimpleGUI import PySimpleGUI as sg
# Comandos cmd:
# pip install PySimpleGUI

# Layout
sg.theme('Reddit')
buttons = [
    [sg.Button('Entrar', size=(10,1))],
    [sg.Button('Cadastrar!', size=(10,1))]
]
layout = [
    [sg.Text('Usuário', size=(7, 1)), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha', size=(7, 1)), sg.Input(key='senha',
                                             password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o Login?'), sg.Text('Não possui cadastro?')],
    [sg.Column(buttons,element_justification='left')]
    # ,[sg.Button('Entrar'), sg.Button('Cadastrar!')]
]


# Cria a janela
window = sg.Window('My window', layout, element_justification='c')
#window = sg.Window('Bem vindo ao chat!', layout)

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Josh' and valores['senha'] == '123456':
            print('Bem vindo ao chat!')
