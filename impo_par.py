# UM PROGRAMA DE IMPAR OU PAR
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

import os 
os.system("cls")  # Limpa a tela do terminal

num = int(input("Digite um numero: "))  # Solicita ao usuário um número inteiro
if num % 2 == 0 :  # Verifica se o número é divisível por 2 (par)
    print("o numero e par")  # Se for par, exibe esta mensagem
else:
    print("o numero e impar")  # Se não for par, exibe esta mensagem (ímpar)