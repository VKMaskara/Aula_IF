# ADIVINHE O NUMERO
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

import os 
os.system("cls")  # Limpa a tela do terminal (no Windows)
import random 
print("Adivinhe o numero  ")  # Exibe mensagem inicial

gerar = random.randint(1,10)  # Gera um número aleatório entre 1 e 10

numero = int(input("Digite um numero de 1 a 10 "))  # Solicita ao usuário um número

if numero == gerar :  # Verifica se o número digitado é igual ao gerado
    print("Voce acertou ")  # Mensagem de acerto
else :
    print("cabaço voce errou ")  # Mensagem de erro
