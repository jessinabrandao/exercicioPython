"""
from math import sqrt
num = int(input('Informe um número: '))
print('A raiz quadrada do número {} é: {}'.format(num, sqrt(num)))

from math import trunc
num1 = float(input('Informe outro número: ')
print('A porção inteira de {} é {}'.format(num1, trunc(num1)))
"""
'''#Programa que lê o comprimento do cateto oposto e adjacente, para calcular o valor da hipotenusa.
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente:'))
print('O comprimento da hipotenusa é: {:.2f}'.format(hypot(co,ca)))'''

#Programa que sorteia uma string
import random
p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))
lista = [p1, p2, p3, p4]
#escolha = random.choice(lista)
print('A pessoa escolhida foi: {}'.format(random.choice(lista)))

'''#Programa  que sorteia uma ordem na string
from random import shuffle
p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))'''