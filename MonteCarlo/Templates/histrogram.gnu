# Configurações gerais
reset
#set terminal pngcairo
#set output 'histogram_pi_error.png'

#LaTex
set terminal lua tikz linewidth 2 standalone
set output 'histogram.tex' 

# Configurações do histograma
set key off
binwidth = 0.0004  # Largura do bin
bin(x, width) = width*floor(x/width)
set boxwidth binwidth
set style fill solid border -1
set ylabel 'Frequência'
set xlabel 'Erro na estimativa de $\pi$'

#Style(Pallet Collors)
set style line 1 lc rgb '#181818'
set style line 2 lc rgb '#F2D57E'
set style line 3 lc rgb '#D9B68B'
set style line 4 lc rgb '#F2935C'
set style line 5 lc rgb '#8C4A3B'
set style line 6 lc rgb '#BF4F45'


# Configuração do xrange
set xrange [-0.005:0.005]

set title "$N = 500k$"
data = 'Plots/pi_x-y-Erro_N(500k).dat'

# Número total de pontos
total_points = 900

# Função Gaussiana
gaussian(x, mean, sigma) = 1./(sigma*sqrt(2*pi)) * exp(-(x - mean)**2 / (2 * sigma**2))

# Ajuste de curva Gaussiana aos dados
fit gaussian(x, mean, sigma) data using (bin($3, binwidth)):(1.0) via mean, sigma

# Plotagem do histograma
plot data using (bin($3, binwidth)):(1.0) smooth freq with boxes ls 6, \
     gaussian(x, mean, sigma/total_points) with lines linestyle 1 lw 2
