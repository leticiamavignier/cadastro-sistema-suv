import PySimpleGUI as sg

sg.theme('Darkbrown2')

# Iniciando Abertura de Protocolo - Pessoa desaparecida

layout = [[sg.Text('Gerar Protocolo para desaparecimento de uma pessoa.')],
          [sg.Text('Informe com cautela as seguintes informações:')],
          [sg.Text('Qual a idade?'), sg.InputText()],
          [sg.Text('Qual a altura aproximada?'), sg.InputText()],
          [sg.Text('Qual o peso aproximado?'), sg.InputText()],
          [sg.Text('Cor da pele?'), sg.InputText()],
          [sg.Text('Cor dos olhos?'), sg.InputText()],
          [sg.Text('Cor dos cabelos?'), sg.InputText()],
          [sg.Text('Cor dos olhos?'), sg.InputText()],
          [sg.Text('Último lugar que a pessoa foi vista?'), sg.InputText()],
          [sg.Text('Contexto do desaparecimento'), sg.InputText()],
          [sg.Text('Carregue a foto da pessoa caso tenha')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Button('Cadastrar')],
          ]
# Nome da Tela de Protocolo
window = sg.Window('Sistema SUV - Informar desaparecimento', layout)

# Interação da tela de Protocolo
event, values = window.read()

# Aviso de protocolo gerado
text_input = values[0]
sg.popup('Seu protocolo foi gerado com sucesso.', text_input)

# Aviso de notificação à Cruz Vermelha
text_input = values[0]
sg.popup('Será enviado a notificação para a Cruz Vermelha.', text_input)

# Fechar tela de Protocolo
window.close()
