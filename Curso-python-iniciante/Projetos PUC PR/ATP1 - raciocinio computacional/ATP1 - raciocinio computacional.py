# Esta é a atividade prática da máteria de Raciocínio Computacional da PUC PR
# Conforme pedido vamos iniciar mostrando meu nome completo e o nome da minha loja

print('-=-'*20)
print("\33[1:35:40mOlá! Bem-vindo à loja da Ana Julia Nunes de Araujo\033[m")
print('-=-'*20)

# Em seguida pedirei os dados do cliente para iniciar a análise de crédito

print("Vamos iniciar sua análise de crédito... ")

#Suspense de 3 segundos

from time import sleep
sleep(3)

cargo = str(input('Digite o seu cargo: '))
salario = float(input('Digite o seu salário separando as casas decimais por ponto: '))
ano = int(input('Digite o ano do seu nascimento: '))
print('Você é {}, seu salário é de {} e você nasceu no ano {}'.format(cargo, salario, ano))

#Em seguida mostrarei na tela a idade aproximada do usuário utilizando o módulo datetime pra usar o ano atual de forma automática

from datetime import date
idade = date.today().year-ano
print('Sua idade é de aproximadamente {} anos'.format(idade))

#Cálculo para mostrar quanto o cliente poderá gastar na loja

limite = (salario * (idade / 1000)) + 100
print('Você poderá gastar na loja um total de R$ {}'.format(limite))










