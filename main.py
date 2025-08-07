import random

def gerador():
    reposta =  input("Olá, Gostaria de Jogar um jogo de advinha?(s/n)").lower()
    if reposta == "s":
        intervalo_inicial = int(input("Digite o primeiro número do intervalo: "))
        intervalo_final = int(input("Digite o último número do intervalo: "))
        numero = int(random.randint(intervalo_inicial, intervalo_final))
        palpite = 0
        tentativas = 1
        a = " "
        print("\nNúmero Gerado com sucesso, dúvido que você acertar HAHAHAHA!")
        print("Você tem 10 Tentativas!\n")
        
        while palpite != numero or tentativas < 10:
            print(f"Esta é sua {tentativas}° tentativa ")
            palpite = int(input("Digite seu palpite: "))
            if palpite < intervalo_inicial or palpite > intervalo_final:
                print("Número fora do intervalo digitado!")
                return
            if palpite > numero:
                print("Um pouco mais pra baixo!")
            if palpite < numero:
                print("Um pouco mais pra cima!")
            tentativas += 1
            if tentativas == 10:
                print("Você excedeu o número de tentativas AHAHAHAHAH")
                while a != "s" and a != "n":
                    print("Digite uma resposta válida s ou n!")
                    a = input("Deseja jogar Jogar denovo?(s/n)").lower()
                    if a == "s":
                        gerador()
                    if a == "n":
                        print("Obrigado por usar meu programa!")
            if palpite == numero:           
                print(f"Você Acertou em {tentativas} tentativas!!!")
                while a != "s" and a != "n":
                    print("Digite uma resposta válida s ou n!")
                    a = input("Deseja jogar Jogar denovo?(s/n)").lower()
                    if a == "s":
                        gerador()
                    if a == "n":
                        print("Obrigado por usar meu programa!")
    else:
        print("Vai te Lascar Então")
                        
if __name__ == "__main__":
    gerador()         
                            #vai jantar? oq qui é? acho q frango fimose vou :D, ta vc vai cmg as 17:30, pdc 👍