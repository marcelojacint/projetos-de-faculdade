def gera_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11): 
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    try:
        num = int(input("Digite um número para gerar a tabuada: "))
        gera_tabuada(num)
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
