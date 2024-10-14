import random

def lancar_dados(num_lancamentos):
    resultados = []
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6) 
        resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    print("Simulador de Lançamento de Dados")
    try:
        num_lancamentos = int(input("Digite o número de lançamentos do dado: "))
        
        if num_lancamentos <= 0:
            print("Por favor, insira um número positivo.")
        else:
            resultados = lancar_dados(num_lancamentos)
            print(f"Resultados dos lançamentos: {resultados}")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
