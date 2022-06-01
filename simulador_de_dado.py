import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('nao')]
        ]      


    def Iniciar(self):
         #Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #Fazer alguma coisa        
        
        try:
            if self.eventos == 'sim':
                self.ValorDoDado()
            elif self.eventos == 'nao':
                print('Obrigado por participar!')
            else:
                print('Responda sim ou não!')
        except:
            print('Erro!')


    def ValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
