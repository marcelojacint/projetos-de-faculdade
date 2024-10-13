def conta_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"
    contador_vogais = 0
    contador_consoantes = 0

    for char in frase:
        if char.isalpha():
            if char in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1

    return contador_vogais, contador_consoantes

if __name__ == "__main__":
    frase_usuario = input("Digite uma frase: ")
    vogais, consoantes = conta_vogais_consoantes(frase_usuario)

    print(f"Número de vogais: {vogais}")
    print(f"Número de consoantes: {consoantes}")
