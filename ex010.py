real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 4.80

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))