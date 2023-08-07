'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

valor1 = int(input("Digite 4 valores inteiros em sequência. Primeiro: "))

valor2 = int(input("Segundo: "))

valor3 = int(input("Terceiro: "))

valor4 = int(input("Quarto: "))

resultado1 = valor1 + valor2 + valor3 + valor4

resultado2 = valor1 * valor2 * valor3 * valor4

print("A adição de todos eles:", resultado1)
print("A multiplicação de todos eles:", resultado2)