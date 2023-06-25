class Consulta:
    def __init__(self):
        print('\n=Dados da Consulta=')
        self.sintomas = leia_string('Sintomas: ')
        self.exames = leia_string('O(s) exame(s) a ser feito: ')
        self.diagnostico = leia_string('Diagnóstico: ')
        self.medicamentos = leia_string('Medicamentos: ')
        self.procedimentos = leia_string('Procedimentos a ser feito: ')
        self.situacao = leia_string('Situação do Animal: ')

    def ImpriDados(self):
        print('\n===Imprimindo dados sobre a consulta===')
        print(f'Sintomas: {self.sintomas}')
        print(f'Exames feitos: {self.exames}')
        print(f'Diagnóstico: {self.diagnostico}')
        print(f'Medicamentos: {self.medicamentos}')
        print(f'Procedimentos: {self.procedimentos}')
        print(f'Situação: {self.situacao}')



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