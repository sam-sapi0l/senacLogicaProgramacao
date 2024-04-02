'''
7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento

'''

nome = input('Digite o seu nome: ')
salario = float(input('Digite seu salário: '))
salario_reajustado = salario

if salario < 280:
    aumento_20_porcento = (salario_reajustado * 0.2) + salario
    valor_aumento = salario * 0.2
    print(f'{nome}, seu salário antes do reajuste era: {salario}')
    print('Pelo valor do seu salário, reajuste será de 20%')
    print(f'Valor do aumento: {valor_aumento}')
    print(f'Seu salário após reajuste é: {aumento_20_porcento}')
elif salario >= 280 and salario < 700:
    aumento_15_porcento = (salario_reajustado * 0.15) + salario
    valor_aumento = salario * 0.15
    print(f'{nome}, seu salário antesdo reajuste era: {salario}')
    print(f'Valor do aumento: {valor_aumento}')
    print('Pelo valor do seu salário, reajuste será de 15%')
    print(f'Seu salário após reajuste é: {aumento_15_porcento}')
elif salario >= 700 and salario < 1500:
    aumento_10_porcento = (salario_reajustado * 0.1) + salario
    valor_aumento = salario * 0.1
    print(f'{nome}, seu salário antes do reajuste era: {salario}')
    print(f'Valor do aumento é: {valor_aumento}')
    print('Pelo valor do seu salário o reajuste será de 10%')
    print(f'Seu salário após reajuste é: {aumento_10_porcento}')
elif salario >= 1500:
    aumento_5_porcento = (salario * 0.05) + salario
    valor_aumento = salario * 0.05
    print(f'{nome}, seu salário antes do reajuste era: {salario}')
    print(f'Valor do aumento: {valor_aumento}')
    print('Pelo valor do seu salário,o reajuste será de 5%')
    print(f'Seu salário após reajuste é: {aumento_5_porcento}')
else:
    print('Valor inválido!')
