set terminal pngcairo #dashed enhanced size 600,400 font 'arial,12' fontscale 1.0
set output 'dash.png'
set encoding utf8

set xlabel "x"
set ylabel "f(x) = x"

data = "linear.dat"

plot data w l