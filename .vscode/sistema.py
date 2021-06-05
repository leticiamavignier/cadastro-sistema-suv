import PySimpleGUI as sg
sg.theme = ('DarkAmber')
# Define the windows contents
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

# Create the windows
sg.theme = ('DarkAmber')
window = sg.Window('Sistema SUV - Salve Uma Vida', layout)

# Display and interact with the Window
event, values = window.read()


text_input = values[0]
sg.popup('Seu cadastro foi realizado com sucesso', text_input)

# Finish up by removing from the screen
window.close()
