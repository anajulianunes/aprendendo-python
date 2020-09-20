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
from datetime import date
def obter_limite():
    cargo = str(input('Digite o seu cargo: '))
    salario = float(input('Digite o seu salário separando as casas decimais por ponto: '))
    ano = int(input('Digite o ano do seu nascimento: '))
    print('Você é {}, seu salário é de {} e você nasceu no ano {}'.format(cargo, salario, ano))
# ETAPA 2
    # Em seguida mostrarei na tela a idade aproximada do usuário utilizando o módulo datetime pra usar o ano atual de forma automática
    idade_cliente = date.today().year-ano
    print('Sua idade é de aproximadamente {} anos'.format(idade_cliente))
    #Cálculo para mostrar quanto o cliente poderá gastar na loja
    limite_total = (salario * (idade_cliente / 1000)) + 100
    print('\33[1:35:40mVocê poderá gastar na loja um total de R$ {}\033[m'.format(limite_total))
    return limite_total, idade_cliente

# ETAPA 3
# Pedindo o nome e o preço do produto
def verificar_produto(limite):
    prod = input('Digite o nome do produto: ')
    valor_prod = float(input('Digite o valor do produto: R$ '))
    # Usando as condicionais solicitadas nesta etapa
    desconto = 0
    bloq = 0
    if valor_prod<=limite*(60/100):
        print('Liberado!')
    elif limite*(60/100)<valor_prod<limite*(90/100):
        print('Liberado ao parcelar em até 2 vezes')
    elif limite*(90/100)<valor_prod<limite:
        print('Liberado ao parcelar em 3 ou mais vezes')
    else:
        print('Bloqueado')
        bloq = 1
    # Em seguida a condicional com o número de caracteres do meu nome completo
    meunome = 'Ana Julia Nunes de Araujo'
    nomecaractere = len(meunome)
    primeironome = (meunome.split() [0])
    primnomecaractere = len(primeironome)
    if (not bloq):
        if (nomecaractere<valor_prod<idade_cliente):
            # O desconto é o número de caracteres do meu primeiro nome
            desconto = primnomecaractere
            print('Vc terá um desconto de R${}'.format(desconto))
            valor_prodfinal = valor_prod-desconto
            print('O valor do produto com desconto é de {}'.format(valor_prodfinal))
            limite -= valor_prodfinal
        else:
            print('Sem desconto.')
            limite -= valor_prod
    return(limite)

#ETAPA 4
#Por fim, após criar as funções dentro das etapas 1,2 e 3, criamos a estrutura de repetição
limite, idade_cliente = obter_limite()
qtdd_prod = int(input('Digite a quantidade de produtos que será comprada: '))
for i in range(qtdd_prod):
    limite = verificar_produto(limite)
    print('\33[1:35:40mSeu novo limite é de {}\033[m'.format(limite))

input('Clique na tecla "enter" para finalizar')


















