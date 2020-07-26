numero = int(input('Insert a number: '))
u = numero // 1 % 10 #pega um número divide por 1 e depois por 10 e pega o resto da divisao
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u,d, c, m))

