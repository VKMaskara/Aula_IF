# PROGRAMA PARA CALCULAR MULTA POR EXCESSO DE VELOCIDADE
#AUTOR: VITOR KAUÊ
#DATA: 04/09/2025

# Solicitar entradas do usuário
km_saida = float(input("Digite o km de saída do veículo: "))
km_chegada = float(input("Digite o km de chegada do veículo: "))
hora_saida = float(input("Digite a hora de saída (em horas, ex: 10.5 para 10:30): "))
hora_chegada = float(input("Digite a hora de chegada (em horas, ex: 12.0 para 12:00): "))

# Calcular distância e tempo
distancia = km_chegada - km_saida
tempo = hora_chegada - hora_saida

# Verificar se tempo é positivo
if tempo <= 0:
    print("Erro: Hora de chegada deve ser maior que hora de saída.")
else:
    # Calcular velocidade média
    velocidade_media = distancia / tempo
    print(f"Velocidade média: {velocidade_media:.2f} km/h")

    # Verificar se excedeu 80 km/h
    if velocidade_media > 80:
        excesso = velocidade_media - 80
        multa = distancia * 5
        print(f"Você excedeu a velocidade em {excesso:.2f} km/h.")
        print(f"Multa: R$ {multa:.2f}")
    else:
        print("Velocidade dentro do limite. Nenhuma multa.")
