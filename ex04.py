"""
from math import sqrt
num = int(input('Informe um número: '))
print('A raiz quadrada do número {} é: {}'.format(num, sqrt(num)))

from math import trunc
num1 = float(input('Informe outro número: '))
print('A porção inteira de {} é {}'.format(num1, trunc(num1)))
"""
#Programa que lê o comprimento do cateto oposto e adjacente, para calcular o valor da hipotenusa.
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente:'))
print('O comprimento da hipotenusa é: {:.2f}'.format(hypot(co,ca)))