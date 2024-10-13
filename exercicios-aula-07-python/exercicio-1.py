def calcula_media_notas():
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para encerrar): "))
            if nota == -1: 
                break
            if nota < 0 or nota > 10:
                print("Por favor, insira uma nota válida entre 0 e 10.")
            else:
                notas.append(nota)  
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

    if notas:  
        media = sum(notas) / len(notas) 
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
    calcula_media_notas()
