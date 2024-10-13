def is_primo(num):
    if num <= 1:
        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
    return True  

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        if is_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
