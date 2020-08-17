valor1 = float(input('primeiro valor: '))
valor2 = float(input('segundo valor: '))
valor3 = float(input('terceiro valor: '))
#verificando menor valor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#verificando o maior número
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor2 and valor3 > valor1:
    maior = valor3
print('O menor valor é {}'. format(menor))
print('E o maior valor é {}'.format(maior))

