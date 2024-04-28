'''
4.Leia 5 valores e imprima sua média e soma 

'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite terceiro valor: "))
valor4 = float(input("Digite o quarto valor: "))
valor5 =float(input("Digite o quinto e último valor: "))

soma = valor1 + valor2 + valor3 + valor4 + valor5
media = soma / 5

print(f"A soma dos valores informados é {soma} e sua média é: {media:.2f}")