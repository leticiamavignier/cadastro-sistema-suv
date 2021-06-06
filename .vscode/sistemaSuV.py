import PySimpleGUI as sg

# Itens da tela de cadastro com o tema definido
sg.theme('Darkbrown2')
layout = [[sg.Text("Bem Vindo ao sistema SUV – Salve Uma Vida")],
          [sg.Text("Para fazer sua solicitação é preciso se cadastrar")],
          [sg.Text("IMPORTANTE: ")],
          [sg.Text("I - Cadastre um telefone e e-mails válidos. ")],
          [sg.Text("II – Os dados estão protegidos conforme a LGPD.")],
          [sg.Text("III –Não use o sistema para aplicar trotes")],
          [sg.Text("Nome:")],
          [sg.Input()],
          [sg.Text("Telefone:")],
          [sg.Input()],
          [sg.Text("E-mail:")],
          [sg.Input()],
          [sg.Button('Cadastrar')]]

# Nome da Tela de Cadastro
window = sg.Window('Sistema SUV - Salve Uma Vida', layout)

# Interação da tela de cadastro
event, values = window.read()


text_input = values[0]
sg.popup('Seu cadastro foi realizado com sucesso', text_input)

# Fechar tela de cadastro
window.close()
