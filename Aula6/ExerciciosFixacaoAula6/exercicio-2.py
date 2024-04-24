'''
Calculadora Simples com if-elif-else: Crie um programa que simule uma calculadora. Peça ao usuário que escolha uma operação (soma, subtração, multiplicação ou divisão) e, em seguida, solicite dois números. Realize a operação escolhida e mostre o resultado.

'''

operacao = int(input('Escolha uma operação entre: \n[1][soma]\n[2][subtração]\n[3][multiplicação]\n[4][divisão]\nOperação:'))

while operacao <= 0 or operacao > 4:
    print('Opção Inválida!')
    operacao = input('Escolha uma operação entre: \n[soma]\n[subtração]\n[multiplicação]\n[divisão]')
    
else:
    print('Escolha validada...')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))    

if operacao == 1:
    soma = num1 + num2
    print(f'A soma dos números é: {soma}')
elif operacao == 2:
    subtracao = num1 - num2
    print(f'A subtração dos números é: {subtracao}')
elif operacao == 3:
    multiplicacao = num1 * num2
    print(f'A ultiplicação dos números é: {multiplicacao}')
elif operacao == 4:
    divisao = num1 / num2
    print(f'A divisão dos números é: {divisao}')
else:
    print('Finalizado!')