'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

distancia = float(input("Diga a distancia em km da sua viagem: "))

consumo = float(input("Diga também a distância média em km que seu carro percorre por litro: "))

gastolitro = distancia / consumo

print("Seu carro irá gastar", gastolitro, "litro(s) nessa viagem.")
