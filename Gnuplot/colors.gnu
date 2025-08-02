# Exemplo de código para gerar um gráfico de referência de cores
set terminal pngcairo enhanced font "Arial,10" size 1000,600
set output "gnuplot_color_chart.png"
set xrange [0:10]
set yrange [0:8]
unset border
unset key
unset tics

# Definir cores em grupos (apenas cores válidas do Gnuplot)
basic_colors = "red green blue yellow cyan magenta black white"
warm_colors = "red orange coral salmon pink gold"
cool_colors = "blue cyan turquoise navy purple violet"
earth_colors = "brown orange yellow green gray black"

# Plotar cores básicas
set label "Cores Básicas" at 5,7.5 center font "Arial,14,bold"
do for [i=1:words(basic_colors)] {
  x = (i-1) % 8 + 1
  y = 6.5 - int((i-1)/8) * 0.8
  set object i rectangle from x,y to x+0.8,y+0.6 fc rgb word(basic_colors,i) fs solid
  set label word(basic_colors,i) at x+0.4,y-0.3 center font "Arial,8"
}

# Plotar cores quentes
set label "Cores Quentes" at 5,5.5 center font "Arial,14,bold"
do for [i=1:words(warm_colors)] {
  x = (i-1) % 6 + 2
  y = 4.5 - int((i-1)/6) * 0.8
  set object (100+i) rectangle from x,y to x+0.8,y+0.6 fc rgb word(warm_colors,i) fs solid
  set label word(warm_colors,i) at x+0.4,y-0.3 center font "Arial,8"
}

# Plotar cores frias
set label "Cores Frias" at 5,3.5 center font "Arial,14,bold"
do for [i=1:words(cool_colors)] {
  x = (i-1) % 6 + 2
  y = 2.5 - int((i-1)/6) * 0.8
  set object (200+i) rectangle from x,y to x+0.8,y+0.6 fc rgb word(cool_colors,i) fs solid
  set label word(cool_colors,i) at x+0.4,y-0.3 center font "Arial,8"
}

# Plotar cores terrosas
set label "Cores Terrosas" at 5,1.5 center font "Arial,14,bold"
do for [i=1:words(earth_colors)] {
  x = (i-1) % 6 + 2
  y = 0.5 - int((i-1)/6) * 0.8
  set object (300+i) rectangle from x,y to x+0.8,y+0.6 fc rgb word(earth_colors,i) fs solid
  set label word(earth_colors,i) at x+0.4,y-0.3 center font "Arial,8"
}

# Título principal
set label "Paleta de Cores do Gnuplot" at 5,7.8 center font "Arial,16,bold"

# Comando plot necessário para renderizar o gráfico
plot NaN notitle