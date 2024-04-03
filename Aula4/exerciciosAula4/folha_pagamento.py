'''
8. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                                : R$   55,00 
    (-) INSS ( 10%)                       : R$  110,00
    FGTS (11%)                            : R$  121,00
    Total de descontos                : R$  165,00
    Salário Liquido                       : R$  935,00

'''

nome = input('Digite seu nome: ')
valor_hora = float(input('Digite valor/h: '))
quantidade_hora = float(input('Digite seu número de horas trabalhadas: '))
calcula_salario_bruto = valor_hora * quantidade_hora

if calcula_salario_bruto <= 900:
    calcula_desconto_imposto_de_renda = calcula_salario_bruto * 0.05
    calcula_desconto_inss = calcula_salario_bruto * 0.1
    calcula_desconto_fgts = calcula_salario_bruto * 0.11
    total_descontos = calcula_desconto_fgts + calcula_desconto_inss + calcula_desconto_imposto_de_renda + calcula_desconto_inss
    calcula_salario_liquido =  calcula_salario_bruto - calcula_desconto_fgts - calcula_desconto_inss
    print(f'Colaborador: {nome}')
    print('Isento de descontos de Imposto de Renda')
    print(f'Salário Bruto: R${calcula_salario_bruto}')
    print(f'(-) IR (0%)                  :R$ 0,00')   
    print(f'(-) INSS (10%)               :R${calcula_desconto_inss}')
    print(f'FGTS (11%)                   :R${calcula_desconto_fgts} ')
    print(f'Totais de Descontos          :R${total_descontos}')
    print(f'Salário Liquido              :R${calcula_salario_liquido}')
elif calcula_salario_bruto > 900 and calcula_salario_bruto < 1500:
    calcula_desconto_imposto_de_renda = calcula_salario_bruto * 0.05
    calcula_desconto_inss = calcula_salario_bruto * 0.05
    calcula_desconto_fgts = calcula_salario_bruto * 0.11
    total_descontos = calcula_desconto_fgts + calcula_desconto_inss + calcula_desconto_imposto_de_renda + calcula_desconto_inss
    calcula_salario_liquido =  calcula_salario_bruto - calcula_desconto_fgts - calcula_desconto_inss
    print(f'Colaborador: {nome}')
    print(f'Salário Liquido: R${calcula_salario_bruto}')
    print(f'(-) IR (5%)                  :R${calcula_desconto_imposto_de_renda}')   
    print(f'(-) INSS (10%)               :R${calcula_desconto_inss}')
    print(f'FGTS (11%)                   :R${calcula_desconto_fgts} ')
    print(f'Totais de Descontos          :R${total_descontos}')
    print(f'Salário Liquido              :R${calcula_salario_liquido}')
elif calcula_salario_bruto >= 1500 and calcula_salario_bruto < 2500:
    calcula_desconto_imposto_de_renda = calcula_salario_bruto * 0.05
    calcula_desconto_inss = calcula_salario_bruto * 0.10
    calcula_desconto_fgts = calcula_salario_bruto * 0.11
    total_descontos = calcula_desconto_fgts + calcula_desconto_inss + calcula_desconto_imposto_de_renda
    calcula_salario_liquido =  calcula_salario_bruto - calcula_desconto_fgts - calcula_desconto_inss
    print(f'Colaborador: {nome}')
    print(f'Salário Liquido: R${calcula_salario_bruto}')
    print(f'(-) IR (5%)                  :R${calcula_desconto_imposto_de_renda}')   
    print(f'(-) INSS (10%)               :R${calcula_desconto_inss}')
    print(f'FGTS (11%)                   :R${calcula_desconto_fgts} ')
    print(f'Totais de Descontos          :R${total_descontos}')
    print(f'Salário Liquido              :R${calcula_salario_liquido}')
elif calcula_salario_bruto >= 2500:
    calcula_desconto_imposto_de_renda = calcula_salario_bruto * 0.20
    calcula_desconto_inss = calcula_salario_bruto * 0.10
    calcula_desconto_fgts = calcula_salario_bruto * 0.11
    total_descontos = calcula_desconto_fgts + calcula_desconto_inss + calcula_desconto_imposto_de_renda
    calcula_salario_liquido =  calcula_salario_bruto - calcula_desconto_fgts - calcula_desconto_inss - calcula_desconto_imposto_de_renda
    print(f'Colaborador: {nome}')
    print(f'Salário Liquido: R${calcula_salario_bruto}')
    print(f'(-) IR (20%)                  :R${calcula_desconto_imposto_de_renda}')   
    print(f'(-) INSS (10%)               :R${calcula_desconto_inss}')
    print(f'FGTS (11%)                   :R${calcula_desconto_fgts} ')
    print(f'Totais de Descontos          :R${total_descontos}')
    print(f'Salário Liquido              :R${calcula_salario_liquido}')
else:
    print('Valor inválido!')
