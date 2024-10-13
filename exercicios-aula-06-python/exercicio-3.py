
numero = int(input("Digite um número para calcular a tabuada: "))

with open('tabuadasExercicio3.txt', 'w') as file:
    file.write(f'Tabuada do {numero}:\n')
    for i in range(1, 11): 
        resultado = numero * i
        file.write(f'{numero} x {i} = {resultado}\n')

print(f"Tabuada do {numero} armazenada no arquivo 'tabuadadasExercicio3.txt'.")
