27/06/2024

#Funções com Parâmetros e retorno

def calculadora(n1,op,n2):
    if op == '+':
        resultado = n1 + n2
    elif op=='-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2

    return resultado
# início do programa

while True:
    try:
        n1 = float(input('n1='))
        oper = 'x'
        while oper != '+' and oper != '-' and oper != '*' and oper != '/':
            oper = input('[ +  -  *  /  ] =')
        n2=float(input('n2='))
    except:
        print('Somente numeros Reais')
    r=calculadora(n1,oper,n2)
    print(f'{n1}  {oper} {n2} = {r}')
    print(f'{n1}  {oper} {n2} = {calculadora(n1,oper,n2)}')
    cont='x'
    while (cont !='S' and cont !='N'):
        cont=input('Continua (S/N)').upper()

    if cont=='N':
        break






''' Existe uma fórmula que determina uma relação entre as temperaturas. Veja abaixo:

 C = (F - 32) * 5 /9
 
 F = (C * 1.8 ) + 32

Onde C é a temperatura em graus Celsius e F, a temperatura em Fahrenheit. Ao simplificarmos a fórmula, temos:


Ou seja, para que você consiga converter de grau Celsius para Fahrenheit, basta multiplicar a temperatura em graus Celsius por 1,8 e somar 32. Veja o exemplo:

37º C para Fahrenheit:
F = 37 x 1,8 + 32;

F = 98,6;

Faça um programa que tem duas funções. 
Uma chamada Celcius que recebe um valor em Fahrenheit e mostra o valor em Celcius
Uma chamada Fahrenheit que recebe uma valor em Celcius e mostra o valor em Fahrenheit

Demonstre as funções com exemplos'''

def celcius(F):
    C = (F - 32) * 5 /9
    print( f' A temperatura {F}  ºF  = {round(C,2)} ºC')

def fahrenheit(C):
    F = (C * 1.8 ) + 32
    print(f' A temperatura {C} ºC =  {round(F,2)}  ºF')

while True:
    F = float(input("Digite Temperatura em ºF= "))
    celcius(F)
    C=float(input('Digite Temperatura em ºC= '))
    fahrenheit(C)
    cont='x'
    while (cont !='S' and cont !='N'):
        cont=input('Continua (S/N)').upper()

    if cont=='N':
        break
    print ('Continua....')
print('FIM')





#funcão sem parâmetro e sem Retorno
def apresentacao():
    print('Dentro da funcao')
    nome=input("Quem é você?")
    print(f'{nome}, hello world!')

 ## inicio do programa
print('Início do Programa')
print('Fora da função')
for i in range (3):
    apresentacao() # chama a funcão
    print ('voltou da funçao')
print('Continua o programa....')

def soma(a,b):
    print('\n\nDentro')
    print (f'soma de {a} + {b} = {a + b}\n\n')
def sub(a,b):
    print('\n\nDentro')
    print(f'subtração de {a} - {b} = {a - b}\n\n')
def mult(j,k):
    print(f'Multiplicação de {j} * {k} = {j * k }\n\n')

def div(a,b):
  
    print(f'Divisão de {a} / {b} = {round(a/b,2)}\n\n')


#inicio do programa
print('Fora')
x=float(input('x='))
y=float(input('y='))

soma(x,y)

a=float(input('a='))
b=float(input('b='))
sub(b,a)
sub(a,b)
sub(x,a)
sub(y,a)
soma(6.5,y)
print(a)

mult(a,y)
div(b,x)
print('fora e continua....')
