with open('tabuadas.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f'Tabuada do {i}:\n')
        for j in range(1, 11):
            resultado = i * j
            file.write(f'{i} x {j} = {resultado}\n')
        file.write('\n') 
print("Tabuadas armazenadas no arquivo 'tabuadas.txt'.")
