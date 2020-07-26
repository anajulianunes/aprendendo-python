print('=-=' * 20)
print('Analizador de triangulos')
print('=-=' * 20)
r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
if abs( r2 - r3) < r1 < (r2 + r3) or abs(r1 - r3) < r2 < (r1 + r3) or abs(r1 - r2) < r3 < (r1 + r2):
    print('Os segmentos acima formam um triangulo!')
else:
    print('Os segmentos acima NAAAAOOO formam um triangulo')
