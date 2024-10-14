def desenha_triangulo(altura):
    for i in range(1, altura + 1):
        print('#' * i)

def desenha_quadrado(tamanho):
    for i in range(tamanho):
        print('*' * tamanho)

def desenha_losango(tamanho):
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '%' * (2 * i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(' ' * (tamanho - i - 1) + '%' * (2 * i + 1))

if __name__ == "__main__":
    print("Escolha um padrão para desenhar:")
    print("1. Triângulo")
    print("2. Quadrado")
    print("3. Losango")
    
    escolha = int(input("Digite o número do padrão desejado (1, 2 ou 3): "))

    if escolha == 1:
        altura = int(input("Digite a altura do triângulo: "))
        desenha_triangulo(altura)
    elif escolha == 2:
        tamanho = int(input("Digite o tamanho do quadrado: "))
        desenha_quadrado(tamanho)
    elif escolha == 3:
        tamanho = int(input("Digite o tamanho do losango: "))
        desenha_losango(tamanho)
    else:
        print("Escolha inválida! Por favor, escolha 1, 2 ou 3.")
