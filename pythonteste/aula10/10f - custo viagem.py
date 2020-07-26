from time import sleep
dist = float(input('Qual a distancia da viagem: '))
print('You are about to travel {}km'.format(dist))
sleep(1)
if dist <= 200:
    print('O preço da passagem será R%{:.2f}'.format(dist * 0.5))
else:
    print('O preço da viagem será R${:.2f}'.format(dist * 0.4))


