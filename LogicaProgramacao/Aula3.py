"""
1. Ler dois números e imprimir as variáveis na mesma ordem que foram digitadas.
2. Ler dois valores numéricos e escrever a soma destes.
 
3. Ler três valores numéricos e escrever a média aritmética.
        
4. Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.
5. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa.
Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.    
    
"""

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))
nota5 = float(input("Digite sua quinta nota: "))

calculaMedia = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print(f'Sua média: {calculaMedia}')