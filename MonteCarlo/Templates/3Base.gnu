#Base(tabela) de spin, um "tabuleiro de spin"
#by Matheus Roos
#25/12/2023

reset

#PNG
#set terminal pngcairo dashed enhanced size 600,600 font 'arial,12' fontscale 1.0
#set output 'Base.png'

#LaTex
set terminal lua tikz linewidth 2 size 6,6 standalone
set output 'MC.tex' 

set size ratio 1 #Garante porporção igual em x e y
set encoding utf8
#unset border              # Remove as bordas do gráfico
unset xtics               # Remove as marcações do eixo x
unset ytics               # Remove as marcações do eixo y

# Define a paleta de cores (branco para 0, preto para 1)
set palette defined (0 "#19135d", 1 "#fc2314")

# Desativando a colorbox
unset colorbox

set title "Metropolis: $L=20, T=1, i=1k$"

dataFile = "Plots/Metropolis_L(20)T(1).dat"

# Plota o "tabuleiro de spins"
plot dataFile matrix with image pixels

