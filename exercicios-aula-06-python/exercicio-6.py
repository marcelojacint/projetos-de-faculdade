if __name__ == '__main__':

  funk_artistas = ["Anitta", "MC Kevinho", "MC Livinho", "Ludmilla", 
                  "MC Mirella", "MC Don Juan", "MC Pedrinho", "Tati Zaqui"]
  
  for artista in funk_artistas:
    print(f'Olá {artista}, você foi convidado para uma festa de opera!')
    if artista.lower() == 'anitta':
      funk_artistas.remove(artista)
      print(f'{artista}, não irá à ópera')

  funk_artistas.append('jojo todinho')
  funk_artistas.append('mc tigrão')

  print('adicionado mais 2 participantes!')

  print(f'nova lista:\n')

  for artista in funk_artistas:
     print(f'Olá {artista}, você foi convidado para uma festa de opera!')


      