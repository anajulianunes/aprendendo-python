salario = float(input('Digite o salário atual: R$ '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('O novo salário é {:.2f}'.format(novo))



