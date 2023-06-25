import datetime
from animal import *
from pessoa import *
from consulta import *
from pagamento import *

data_hora = datetime.datetime.now()
agora = data_hora.strftime('%d/%m/%Y %H:%M')

print(f"Data e hora do Check-in: {agora}")
animal = Animal()
print('\n=Dados do(a) Dono(a)=')
dono = Dono()
print('\n=Dados do Veterinário(a)=')
vet = Vet()
animal.ImpriDados()
dono.ImpriDados()
vet.ImpriDados()

con = Consulta()
con.ImpriDados()

pag = Pagamento()
pag.ImpriDados()

data_hora1 = datetime.datetime.now()
agora = data_hora1.strftime('%d/%m/%Y %H:%M')
print(f"Data e hora do Check-out: {agora}\n\n")

