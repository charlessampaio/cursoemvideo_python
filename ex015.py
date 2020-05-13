dias = int(input('Quantidade de dias: '))
km = int(input('Quantidade de Km: '))
total = (dias * 60) + (km * 0.15)

print('O total a pagar é R$ {:.2f}'.format(total))