'''
Faça um programa querecebe um nome de candidato a motorista e seu ano de nascimento,
informar se pode tirar a CNH ou não

'''

from datetime import date

dataAtual = date.today()
print(dataAtual)
dia=dataAtual.day
mes= dataAtual.month
ano = dataAtual.year
print('{}/{}/{}'.format(dia, mes, ano))

nome = input("Digite o nome do candidato: ")
anoNascimento = int(input("Digite seu ano de nascimento: "))
calcula_idade = dataAtual.year - anoNascimento

if calcula_idade >= 18:
    print(f"Seu ano de nascimento é : {anoNascimento}")
    print(f"Sua idade é {calcula_idade}")
    print("Cadidato aprovado por atender requisitos de idade.")
else:
    print("Não atende os requisitos de idade")
   