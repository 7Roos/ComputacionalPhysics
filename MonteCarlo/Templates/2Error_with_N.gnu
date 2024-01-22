# Para mostrar a tendência do erro com 1/sqrt(N)
#by Matheus Roos
#06/01/2024

reset

#PNG
#set terminal pngcairo dashed enhanced size 600,400 font 'arial,12' fontscale 1.0
#set output 'Error_w_N.png'

#LaTex
set terminal lua tikz linewidth 2 standalone
set output 'Base.tex' 

set encoding utf8

set xlabel "$N$"
set ylabel "$error = \\langle f_{\\pi} \\rangle - \\pi$"

#set title "$N = 10000$"


#func = "data_x-y.dat"
points = "Plots/pi/pi_N-error.dat"

#set yrange [-0.1:0.1]
set xrange [1e4:1e9]

# Escala logarítmica no eixo x, base 10
set logscale x 10

# Definindo rótulos personalizados no eixo x
set xtics ("$10^{4}$" 10000, "$10^{5}$" 100000, "$10^{6}$" 1000000, "$10^{7}$" 10000000, "$10^{8}$" 100000000, "$10^{9}$" 1000000000)

#set xtics (0.5, 0.66)

#Style(Pallet Collors)
set style line 1 lc rgb '#181818'
set style line 2 lc rgb '#F2D57E'
set style line 3 lc rgb '#D9B68B'
set style line 4 lc rgb '#F2935C'
set style line 5 lc rgb '#8C4A3B'
set style line 6 lc rgb '#BF4F45'

#Legenda
#set key off

#Plot
plot points w lp notitle ls 1, \
    1/sqrt(x) with lines title '$\pm 1/\sqrt{N}$' ls 6, \
    -1/sqrt(x) with lines notitle ls 6