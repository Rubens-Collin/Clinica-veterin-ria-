class Animal:
    def __init__(self):
        print('===Dados do Check-in===\n')
        print('=Dados do Animal=')
        self.especie = leia_string('Digite a espécie do animal: ')
        self.nome = leia_string('Digite o nome do animal: ')
        self.raca = leia_string('Digite a raça do animal: ')
        self.peso = leia_float('Digite o peso do animal: ')
        self.idade = leia_int('Digite a idade do animal: ')
        self.sexo = leia_string('Digite o sexo animal: ')
        self.comorbidade = leia_string('Digite a comorbidade do animal:')
        self.cor = leia_string('Digite a cor do animal: ')

    def ImpriDados(self):
        print('\n===Imprimindo Dados do Check-in===')
        print(f'Especie do Animal: {self.especie}')
        print(f'Nome do Animal: {self.nome}')
        print(f'Raça do Animal: {self.raca}')
        print(f'Peso do Animal: KG:{self.peso}')
        print(f'Idade do Animal: {self.idade} anos')
        print(f'Sexo do Animal: {self.sexo}')
        print(f'Comorbidade(s) do Animal: {self.comorbidade}')
        print(f'Cor do Animal: {self.cor}')



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

#Essa função trata o erro se o usuário digitar algo alem de números
def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (TypeError, ValueError):
            print('O programa só aceita números e do tipo inteiro. ')
            continue
        else:
            return n
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