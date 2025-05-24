# Formula 2 pts derivative
# M. Roos, 26/03/2025

import math

def f(x):
  return math.cos(x)

# Input
x = float(input("Digite o valor de x: "))
#h = float(input("Digite o valor de h: "))
#x, h = map(float, input("Entre com x, h: ").split(','))

# Cálculo da derivada
for i in range (1,9):
  h = 10.0 ** (-i)

  f_prime = (f(x + h) - f(x)) / h

  # Impressão do resultado
  #print(f"f'(x0): {f_prime}")
  print(f"{h:13.4e} {f_prime:13.4e}")