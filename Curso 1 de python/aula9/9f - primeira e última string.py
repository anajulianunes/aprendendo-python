frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posiçao {}'.format(frase.lower().find('a')+1))
print('A última letra A apareceu na posiçao {}'.format(frase.lower().rfind('a')+1))








