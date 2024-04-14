'''

**Tabuada de Multiplicar:**
Faça um programa que calcule um número não determinado de tabuadas. O programa deve pedir para o usuário 
digitar um número inteiro e, em seguida, imprima a tabela de multiplicação para esse número de 1 a 10.
Por exemplo, se o usuário digitar 3, o programa deve imprimir a tabuada de multiplicar de 3.
Encerrar o programa quando o usuário digitar um numero <=0 

'''
numero_digitado = int(input('Digite um númeoro inteiro: '))
print('Para finalizar o programa digite [0]')

while numero_digitado != 0:
    for i in range(1, 11):
        tabuada = i * numero_digitado
        print(tabuada)
    numero_digitado = int(input('Digite um númeoro inteiro: '))
    print('Para finalizar o programa digite [0]')
else:
    print('Programa encerrado.')
