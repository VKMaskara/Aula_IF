# ESSE CÓDIGO VERIFICA SE UM ANO É BISSEXTO OU NÃO
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

# Solicita ao usuário que digite um ano e converte para inteiro
ano = int(input("Digite o ano desejado :"))

# Verifica se o ano é divisível por 4
if ano %4 == 0:
    print(f"O ano é bissexto")
else :
    print("O ano nao é bissexto")
