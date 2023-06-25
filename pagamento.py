class Pagamento:
    def __init__(self):
        print('\n===Dados do Check-out===')
        self.valor_exames = leia_float('Digite o valor do(s) Exame(s): ')
        self.valor_consulta = leia_float('Digite o valor da consulta: ')
        self.valor_medicamento = leia_float('Digite o valor do(s) medicamento(s): ')
        self.forma_pagamento = ["Cartão de Crébito", "Cartão de Drebito", "Transferência bancária", "Prix", "Aproximação"]

        print("Escolha uma opção de pagamento:")
        for i, opcao in enumerate(self.forma_pagamento):
            print(f"{i + 1}. {opcao}")

        try:
            escolha = int(input("Opção escolhida: "))
            self.forma_pagamento = self.forma_pagamento[escolha - 1]
            print(f'A forma de pagamento escolhida foi {self.forma_pagamento}')
        except ValueError:
            print("Opção inválida. Por favor, tente novamente.")
        self.retorno = input('Digite a data do retorno: ')


    def ImpriDados(self):
        print('\n===Imprimindo Dados do Check-out===')
        print(f'O valor do(s) exame(s): R${self.valor_exames:.2f}')
        print(f'O valor da consulta: R${self.valor_consulta:.2f}')
        print(f'O valor do(s) medicamento(s): R${self.valor_medicamento:.2f}')
        print(f'O pagamento séra feito por: {self.forma_pagamento}')
        print(f'O valor total do pagamento é: R${self.valor_exames + self.valor_consulta + self.valor_medicamento:.2f}')
        print(f'A data do retorno é: {self.retorno}\n')


#Essa função trata o erro se o usuário digitar algo alem de números
def leia_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (TypeError, ValueError):
            print('O programa só aceita números e do tipo inteiro. ')
            continue
        else:
            return n


#Essa função trata o erro se o usuário escreva algo alem de letras e espaços
def leia_string(mensagem):
    while True:
        try:
            palavra = input(mensagem)
            if not all(c.isalpha() or c.isspace() for c in palavra):
                raise ValueError('Entrada inválida: utilize apenas letras e espaços.')
            return palavra
        except ValueError as ex:
            print(ex)