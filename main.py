import random

reposta =  input("Olá, Gostaria de Jogar um jogo de advinha?(s/n)").lower()
if reposta == "s":
    intervalo_inicial = int(input("Digite o primeiro número do intervalo: "))
    intervalo_final = int(input("Digite o último número do intervalo: "))
    numero = random.randint(intervalo_inicial, intervalo_final)
    print("\nNúmero Gerado com sucesso, dúvido que você acertar HAHAHAHA!\n")

    palpite = input("Digite seu palpite: ")
    if palpite > numero:
        print