# Esta é a atividade prática da máteria de Raciocínio Computacional da PUC PR

# ETAPA 1
# Conforme pedido vamos iniciar mostrando meu nome completo e o nome da minha loja
print('-=-'*20)
print("\33[1:35:40mOlá! Bem-vindo à loja da Ana Julia Nunes de Araujo\033[m")
print('-=-'*20)
print("Vamos iniciar sua análise de crédito... ")
#Suspense de 3 segundos
from time import sleep
sleep(2)
cargo = str(input('Digite o seu cargo: '))
salario = float(input('Digite o seu salário separando as casas decimais por ponto: '))
ano = int(input('Digite o ano do seu nascimento: '))
print('Você é {}, seu salário é de {} e você nasceu no ano {}'.format(cargo, salario, ano))

# ETAPA 2
# Em seguida mostrarei na tela a idade aproximada do usuário utilizando o módulo datetime pra usar o ano atual de forma automática
from datetime import date
idade = date.today().year-ano
print('Sua idade é de aproximadamente {} anos'.format(idade))
#Cálculo para mostrar quanto o cliente poderá gastar na loja
limite = (salario * (idade / 1000)) + 100
print('Você poderá gastar na loja um total de R$ {}'.format(limite))

# ETAPA 3
# Pedindo o nome e o preço do produto
prod = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: R$ '))
# Usando as condicionais solicitadas nesta etapa
if valor<=limite*(60/100):
    print('Liberado!')
elif limite*(60/100)<valor<limite*(90/100):
    print('Liberado ao parcelar em até 2 vezes')
elif limite*(90/100)<valor<limite:
    print('Liberado ao parcelar em 3 ou mais vezes')
else:
    print('Bloqueado')
# Em seguida a condicional com o número de caracteres do meu nome completo
meunome = 'Ana Julia Nunes de Araujo'
eucaractere = len(meunome)
if eucaractere<valor<idade:
    # O desconto é o número de caracteres do meu primeiro nome
    desconto = 3
    print('Vc terá um desconto de R${}'.format(desconto))
    print('O valor do produto com desconto é de {}'.format(valor-desconto))
















