import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100) 
    tentativas = 0
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Faça seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break 

        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    jogo_adivinhacao()
