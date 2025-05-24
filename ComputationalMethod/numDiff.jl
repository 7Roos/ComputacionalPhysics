# Formula 2 pts derivative
# M. Roos, 26/03/2025

function f(x)
    return cos(x)
end
  
  # Input
  print("Entre com x, h: ")
  x, h = parse.(Float64, split(readline(), ","))
  
  # Cálculo da derivada
  f_prime = (f(x + h) - f(x)) / h
  
  # Impressão do resultado
  println("f'(x0): ", f_prime)