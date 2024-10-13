def decimal_para_binario(n):
    if n < 0:
        return None  
    if n == 0:
        return "0"  
    
    binario = ""
    while n > 0:
        resto = n % 2  
        binario = str(resto) + binario  
        n //= 2  
    
    return binario

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro não negativo: "))
        resultado = decimal_para_binario(numero)
        if resultado is None:
            print("Binário não é definido para números negativos.")
        else:
            print(f"A representação binária de {numero} é: {resultado}")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro não negativo.")
