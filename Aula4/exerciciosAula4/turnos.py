'''

6. Faça um Programa que pergunte em que estuda você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noestuda.
 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''

nome = input('Digite seu nome: ')
estuda = input('Digite o estuda em que você estuda [M-matutino][V-Vespertino][N-Noturno]: ')
turnos = ['M','m', 'V', 'v', 'N', 'n']

if estuda == 'M' or estuda == 'm':
    print(f'Bom dia, {nome}!')
elif estuda == 'V' or estuda == 'v':
    print(f'Boa tarde, {nome}!')
elif estuda == 'N' or estuda == 'n':
    print(f'Boa noite, {nome}!')
else:
    print('Valor Inválido!')