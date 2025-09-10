# PEGUE O SALARIO DE UM FUNCIONARIO, SE GANHAR MENOS DE 1.200,00 DE AUMENTO DE 15%, SE TIVER FILHOS GANHA 200,00 POR FILHO
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

import os
os.system("cls")  # Limpa a tela do terminal (no Windows)

salario = float(input("Digite o salario do funcionario: "))  # Solicita ao usuário o salário do funcionário
filhos = int(input("Digite a quantidade de filhos: "))  # Solicita ao usuário a quantidade de filhos
aumento = 0  # Inicializa a variável aumento

if salario < 1200:  # Verifica se o salário é menor que 1200
    aumento += salario * 0.15  # Adiciona 15% ao aumento se o salário for menor que 1200

if filhos > 0:  # Verifica se o funcionário tem filhos
    aumento += filhos * 200  # Adiciona 200 por cada filho ao aumento

novo_salario = salario + aumento  # Calcula o novo salário somando o salário original e o aumento

print(f" O seu salario é de R$ {salario:.2f}, voce tem {filhos} filhos, e o seu aumento foi de R$ {aumento:.2f}, entao o seu novo salario é de R$ {novo_salario:.2f} ")  # Exibe o salário original, a quantidade de filhos, o aumento e o novo salário