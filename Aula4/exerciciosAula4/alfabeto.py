'''
1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''
import re
letra_digitada = input("Digite uma letra: ")
vogal = ['a','e','i','o','u']
alfabeto = re.findall("[a-zA-Z]", letra_digitada)

if letra_digitada in vogal:
    print(f"A letra '{letra_digitada}' é vogal!")
elif letra_digitada not in vogal and letra_digitada in alfabeto:
    print(f"A letra '{letra_digitada}' é consoante!")
elif letra_digitada not in vogal and letra_digitada not in alfabeto:
    print("Digite uma entrada válida!")