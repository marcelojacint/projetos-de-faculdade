def gera_fibonacci(n):
    fib_sequencia = []
    a, b = 0, 1  # Os dois primeiros números da sequência

    for _ in range(n):
        fib_sequencia.append(a)  
        a, b = b, a + b  

    return fib_sequencia

if __name__ == "__main__":
    try:
        n = int(input("Digite quantos números da sequência de Fibonacci você deseja: "))
        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            fibonacci = gera_fibonacci(n)
            print(f"Os primeiros {n} números da sequência de Fibonacci são:")
            print(fibonacci)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
