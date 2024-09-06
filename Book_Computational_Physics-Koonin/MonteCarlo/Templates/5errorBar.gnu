#!/usr/local/bin/gnuplot -persist
set terminal pngcairo enhanced font "arial,10" fontscale 1.0 size 600, 400 
set output 'magSeep800.png'
unset parametric
set style data lines
set ytics  norangelimit logscale autofreq 
set title "800 seeps" 
set xlabel "T/J_{1}" 
set xrange [0:5]
set ylabel "mag" 
set yrange [0:1.5] 
n(x)=1.53**2*x/(5.67+x)**2

data = 'Plots/histerese_T-m-mSig.dat'
plot data u 1:2:3 w yerr#, n(x) t "Theory" w lines
