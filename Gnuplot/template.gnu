#set terminal pngcairo dashed enhanced size 600,400 font 'arial,12' fontscale 1.0
#set output 'dash.png'

set terminal lua tikz linewidth 1 standalone
set output 'dash.tex' 

set encoding utf8

#set xlabel "{/Symbol G} / J_{1}"
#set ylabel "T / J_{1}"

set xlabel "$ \\Gamma / J_{1}$"
set ylabel "$T / J_{1}$"

plot [-pi/2:pi] cos(x)