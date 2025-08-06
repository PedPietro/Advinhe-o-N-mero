import random

def gerador():
    reposta =  input("Olá, Gostaria de Jogar um jogo de advinha?(s/n)").lower()
    if reposta == "s":
        intervalo_inicial = int(input("Digite o primeiro número do intervalo: "))
        intervalo_final = int(input("Digite o último número do intervalo: "))
        numero = (random.randint(intervalo_inicial, intervalo_final))
        palpite = 0
        tentativas = 0
        print("\nNúmero Gerado com sucesso, dúvido que você acertar HAHAHAHA!")
        print("Você tem 10 Tentativas!\n")
        paises = [
        "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina",
        "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize",
        "Benin", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burquina Faso", "Burundi",
        "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China",
        "Chipre", "Colômbia", "Comores", "Congo", "Coreia do Norte", "Coreia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
        "Dinamarca", "Djibuti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia",
        "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão",
        "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial",
        "Haiti", "Holanda", "Honduras", "Hungria", "Iémen", "Ilhas Marshall", "Ilhas Salomão", "Índia", "Indonésia", "Irã",
        "Iraque", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kuwait",
        "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte",
        "Madagáscar", "Malásia", "Malávi", "Maldivas", "Mali", "Malta", "Marrocos", "Maurícia", "Mauritânia", "México",
        "Mianmar", "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal",
        "Nicarágua", "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "País de Gales", "Países Baixos", "Palau", "Panamá",
        "Papua-Nova Guiné", "Paquistão", "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana",
        "República Checa", "República Democrática do Congo", "República Dominicana", "Romênia", "Ruanda", "Rússia", "São Cristóvão e Nevis", "São Marino", "São Tomé e Príncipe", "São Vicente e Granadinas",
        "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", "Somália", "Sri Lanka", "Sudão", "Sudão do Sul",
        "Suécia", "Suíça", "Suriname", "Tailândia", "Taiwan", "Tajiquistão", "Tanzânia", "Timor-Leste", "Togo", "Tonga",
        "Trindade e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", "Uruguai", "Uzbequistão", "Vanuatu",
        "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
        ]
        while palpite != numero or tentativas < 10:
            palpite = int(input("Digite seu palpite: "))
            if palpite < intervalo_inicial or palpite > intervalo_final:
                print("Número fora do intervalo digitado!")
                return
            if palpite > numero:
                print("Um pouco mais pra cima!")
            if palpite < numero:
                print("Um pouco mais pra baixo!")
            tentativas += 1
        if tentativas == 10:
            print("Você excedeu o número de tentativas AHAHAHAHAH")
            a = input("Deseja jogar Jogar denovo?(s/n)").lower()
            if a == "s":
                gerador()
            else: ("Vai Catar Coquinho!")
        if palpite == numero:
                print(f"Você Acertou em {tentativas}!!!")
                a = input("Deseja jogar Jogar denovo?(s/n)").lower()
                if a == "s":
                    gerador()
                else: ("Vai Catar Coquinho!")
    else:
        print("Vai te Lascar Então")
                        
if __name__ == "__main__":
    gerador()         
            