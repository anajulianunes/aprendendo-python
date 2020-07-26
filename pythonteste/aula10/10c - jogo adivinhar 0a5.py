from random import randint
from time import sleep
nc = randint(0, 5) #faz o pc pensar
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5, tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número pensei? ')) #usuário tenta adivinhar
print('Processando...')
sleep(3) #pensa por 3segundos
if n == nc:
    print('Valeu! Vc conseguiu vencer')
else:
    print('Eu ganhei otário, pensei em {} e nao {}'.format(nc, n))


