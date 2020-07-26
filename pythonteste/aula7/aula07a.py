a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
s = a + b
d = a - b
m = a * b
div = a / b
p = pow(a , b)
di = a // b
r = a % b
print('A soma é {},\na diminuiçao é {},\na multiplicaçao é {}.'.format(s, d, m, div), end=' ')
print('A divisao inteira é {}, o resto é {}'.format(di, r))
