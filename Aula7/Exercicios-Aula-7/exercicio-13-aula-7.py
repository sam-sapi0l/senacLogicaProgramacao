'''
13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

'''

# inicializando listas
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []
mesesMaiorTemperatura = []

# Determinando número de itens a serem inseridos
for i in range(1, 13, 1):
        try:
            campo_temperatura = float(input('Digite temperatura referente ao mes: '))
            temperatura.append(campo_temperatura)
            print(f'Meses: {mes}')
            print(f'Temperatura: {temperatura}')
        except:
            print('Entrada Inválida!')


contador = 0
for t in temperatura:
    contador += t
    
mediaTemperatura = contador / len(mes)


for t in temperatura:
    if t > mediaTemperatura:
        mesesMaiorTemperatura.append(t)
    elif t <= mediaTemperatura:
        pass
    else:
        print('Problema ao iterar!')
        
print(f'Maiores Médias de Temperatura: {mesesMaiorTemperatura}')
print(f'A média de temperatura é: {mediaTemperatura:.1f}')

