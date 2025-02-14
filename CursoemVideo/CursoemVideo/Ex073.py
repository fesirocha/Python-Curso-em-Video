#Brasileirão
classificacao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
                 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
                 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
                 'São Paulo', 'Fluminsnse', 'Sport Recife', 'Vitória',
                 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Os cinco primeiros colocados são: {classificacao[0:5]}')
print(f'Os últimos quatro colocados são: {classificacao[-1:-5:-1]}')
print(sorted(classificacao))
print(f'A Chapecoense está na {classificacao.index('Chapecoense')+1}ª posição')
