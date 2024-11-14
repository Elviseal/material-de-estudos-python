import PySimpleGUI as sg

# Todas as coisas dentro da sua janela.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Crie a janela
window = sg.Window('Hello Example', layout)

# Event Loop para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()

    # se o usuário fechar a janela ou clicar em cancelar
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print('You entered ', values[0])


#janela.fechar()