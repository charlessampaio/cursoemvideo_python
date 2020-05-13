l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a

print('A sua parede tem dimenção de {:.1f}x{:.1f} e sua área é de {:.3f}m²'.format(l, a, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(area * 0.5))