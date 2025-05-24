# Exemplo de código para gerar um gráfico de referência de cores
set terminal pngcairo enhanced font "Arial,10" size 800,600
set output "gnuplot_color_chart.png"
set xrange [0:10]
set yrange [0:11]
unset border
unset key
unset tics

# Definir cores em grupos
basic_colors = "red green blue yellow cyan magenta"
red_tones = "red darkred indianred firebrick crimson tomato coral salmon"
# etc...

# Plotar cores em grupos
set label "Cores Básicas" at 0.5,10.5 font "Arial,12"
do for [i=1:words(basic_colors)] {
  x = (i-1) % 5
  y = 10 - int((i-1)/5)
  set object i rectangle from x,y to x+0.9,y+0.9 fc rgb word(basic_colors,i) fs solid
  set label word(basic_colors,i) at x+0.45,y+0.45 center
}