velo = float(input('Digite a velocidade do carro: '))
if velo <= 80:
    print('Beleza, boa viagem aperto o cinto')
else:
    print('MULTADO! vc passou de 80km/h!!')
    print('Sua multa é de R$ {:.2f}'. format((velo - 80) * 7))
    print('tenha um dia legal')

