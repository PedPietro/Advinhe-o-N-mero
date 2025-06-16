import random

def gerador():
    reposta =  input("Olá, Gostaria de Jogar um jogo de advinha?(s/n)").lower()
    if reposta == "s":
        intervalo_inicial = int(input("Digite o primeiro número do intervalo: "))
        intervalo_final = int(input("Digite o último número do intervalo: "))
        numero = (random.randint(intervalo_inicial, intervalo_final))
        palpite = 0
        tentativas = 0
        print("\nNúmero Gerado com sucesso, dúvido que você acertar HAHAHAHA!\n")

        
        while palpite != numero:
            palpite = int(input("Digite seu palpite: "))
            if palpite > numero:
                print("Um pouco mais pra cima!")
            if palpite < numero:
                print("Um pouco mais pra baixo!")
            tentativas += 1
        if palpite == numero:
                print(f"Você Acertou em {tentativas}!!!")

if __name__ == "__main__":
    gerador()         
            