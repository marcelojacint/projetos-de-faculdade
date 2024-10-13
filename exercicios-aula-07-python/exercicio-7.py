def calcula_fatorial(n):
    if n < 0:
        return None  
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i 
    return fatorial

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro não negativo: "))
        resultado = calcula_fatorial(numero)
        if resultado is None:
            print("Fatorial não é definido para números negativos.")
        else:
            print(f"O fatorial de {numero} é: {resultado}")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro não negativo.")
