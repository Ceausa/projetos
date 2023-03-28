import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #AQUI É SÓ A CRIAÇÃO DA JANELA SEM ATRIBUIR FUNÇOES, O QUE TA DENTRO DE "KEY" É COMO VAMOS CHAMAR OS ITENS PRA ATRIBUIR ALGUM VALOR OU INPUTS ETC
       
        layout  = [
            [sg.Text("Site/Software",size = (10,1)),
             sg.Input(key = "site",size = (20,1))],
            [sg.Text("E-mail/Usuario", size=(20, 1)),
             sg.Input(key = 'usuario', size = (20,1))],
            [sg.Text("Quantidade de caracteres"), sg.Combo(values = list(range(30)),key = 'total_chars',default_value = 1, size=(3,1))],
            [sg.Output(size = (32,5))],
            [sg.Button('Gerar Senha')],
            
        ]      
        # DECLARAR JANELA
        self.janela = sg.Window('Password Generator', layout)      
    
    def Iniciar(self):
       ## AQUI É ONDE ATRIBUIREMOS OS VALORES E AS FUNÇOES DA JANELA JUNTO COM O CODIGO 
        
        while True:
            events, values = self.janela.read()
            if events == sg.WIN_CLOSED:
                break   
            if events == 'Gerar Senha':
                nova_senha = self.gerar_senha = self.gerar_senha(values)
                print(nova_senha)
                self.salvar_senha(nova_senha, values)
                                  
         #AQUI É ONDE O RANDOM FUNCIONA PRA GERAR A SENHA ALEATORIA   
    def gerar_senha(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%¨&*1234567890'
        chars = random.choices(char_list,k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

        #AQUI É ONDE O ARQUIVO VAI SER SALVO NO .TXT
    def salvar_senha(self, nova_senha, values):
        with open('senhas.txt','a',newline = '') as arquivo:
            arquivo.write(
                f"site: {values['site']}, usuario:{values['usuario']}, nova senha:{nova_senha}")
            print("ARQUIVO SALVO")

gen = PassGen()
gen.Iniciar()