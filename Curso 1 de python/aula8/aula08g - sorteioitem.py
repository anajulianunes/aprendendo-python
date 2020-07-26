from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo alunno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
# pra fazer lista coloca entre chaves
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}!'.format(escolhido))



