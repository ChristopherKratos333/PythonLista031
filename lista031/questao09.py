'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''

import math

numero = float(input("Digite um número: "))

quadrado = math.pow(numero,2)

raizquadrada = math.sqrt(numero)

print("Seu número é:", numero)
print("O quadrado desse número é:", quadrado)
print("A raiz quadrada desse número é:", raizquadrada)

