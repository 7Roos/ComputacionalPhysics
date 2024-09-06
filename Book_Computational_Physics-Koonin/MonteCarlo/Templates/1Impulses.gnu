# Para mostrar como fica a avalição de funções no método de Monte Carlo
#para uma função qualquer.
#by Matheus Roos
#25/12/2023

reset

#PNG
set terminal pngcairo dashed enhanced size 600,400 font 'arial,12' fontscale 1.0
set output 'Base.png'

#LaTex
#set terminal lua tikz linewidth 2 standalone
#set output 'Base.tex' 

set encoding utf8

set xlabel "$x$"
set ylabel "$f(x)$"

set title "$N = 10000$"


func = "data_x-y.dat"
points = "MC_10000.dat"

set yrange [0:1.1]
set xrange [0:1]


#set xtics (0.5, 0.66)

#Style(Pallet Collors)
set style line 1 lc rgb '#181818'
set style line 2 lc rgb '#F2D57E'
set style line 3 lc rgb '#D9B68B'
set style line 4 lc rgb '#F2935C'
set style line 5 lc rgb '#8C4A3B'
set style line 6 lc rgb '#BF4F45'

#Legenda
set key off

#Plot
plot points w impulses ls 1, \
    func w l ls 5 lw 2.5, \
    
    