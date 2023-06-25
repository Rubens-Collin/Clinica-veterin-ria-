class Pessoa:
    def __init__(self):
        self.nome = leia_string('Digite o nome:')
        self.idade = leia_int('Digite a idade:')



class Dono(Pessoa):
    def __init__(self):
        super().__init__()
        self.cpf = leia_int('Digite o CPF:')
        self.cep = leia_int('Digite o cep:')
        self.email = input('Digite o e-mail:')
        self.telefone = leia_int('Digite o telefone:')

    def ImpriDados(self):
        print(f'Nome do Dono: {self.nome}')
        print(f'Idade do Dono: {self.idade} anos')
        print(f'CPF: {self.cpf}')
        print(f'CEP: {self.cep}')


class Vet(Pessoa):
    def __init__(self):
        super(Vet, self).__init__()
        self.crmv = leia_int('Digite o CRMV do Veterinário(a): ')


    def ImpriDados(self):
        print(f'Nome do Veterinário(a): {self.nome}')
        print(f'Idade do Veterinário(a): {self.idade} anos')
        print(f'CRMV: {self.crmv}')



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