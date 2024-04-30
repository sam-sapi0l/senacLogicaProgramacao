"""
Exercício 2

Faça um programa que recebe o raio de uma circunferência, calcular a área e o
perímetro da mesma.

caso saiba a circunferencia:

r = c / 2

caso saiba o raio:

c = r * 2

"""


sabe_circunferencia = input("Voce sabe a circunferência do círculo? [s/N]:")

if sabe_circunferencia == 's' or sabe_circunferencia == 'sim':
    raio = float(input("Digite o valor do raio do círculo:"))
    c = raio * 2
    print(f"O valor do perímetro/circunferência do círculo com os valores informados é: {c}")
elif sabe_circunferencia == 'n' or sabe_circunferencia == 'nao':
    circunferencia = float(input("Digite o valor da circunfêrencia do círculo:"))
    r = circunferencia / 2
    print(f"O valor do raio do círculo é: {r}")
else:
    print("Digite uma resposta válida!")
