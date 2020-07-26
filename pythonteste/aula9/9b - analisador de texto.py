nome = input('Digite seu nome: ').strip()
print('Seu nome em maiúculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(div[0], len(div[0])))


