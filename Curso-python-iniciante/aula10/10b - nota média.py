n1 = float(input('Qual sua nota: '))
n2 = float(input('Qual sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m>=7:
    print('vc passou cabaço')
else:
    print('burro, tente de novo ano que vem')
