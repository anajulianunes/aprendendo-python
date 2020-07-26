l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
print('Sua parede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2'.format(l, h, a))
print('Para pintar essa parede, vc precisará de {:.2f}l de tinta'.format(a/2))
