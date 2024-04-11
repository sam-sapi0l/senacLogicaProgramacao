numero1 =int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    numero1 += 2
    for i in range(numero1, numero2,-2):
        if i%2 != 0:
            i -= 2
            print(i)