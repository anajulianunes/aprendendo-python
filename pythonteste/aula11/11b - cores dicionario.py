nome = 'mel bonitinha'
cores = {'limpa':'\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco': '\033[7:30m'}
print('{}Essa {}{}{}{}{} é mto linda{}'.format(cores['pretoebranco'], cores['limpa'], cores['amarelo'], nome,
                                               cores['limpa'], cores['azul'], cores['limpa'] ))

