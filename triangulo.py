# programa que determina se tres lados formam um triangulo
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

import os
os.system("cls")  # Limpa a tela do terminal (no Windows)

print("Digite os tres lados do triangulo: ")  # Solicita ao usuário os três lados do triângulo
a = float(input("Lado A: "))  # Solicita o lado A
b = float(input("Lado B: "))  # Solicita o lado B
c = float(input("Lado C: "))  # Solicita o lado C

if a < b + c and b < a + c and c < a + b :  # Verifica a condição para formar um triângulo
    print("Os lados formam um triangulo")  # Se a condição for verdadeira, exibe esta mensagem
else:
    print("Os lados nao formam um triangulo") #se a condição for falsa, exibe esta mensagem