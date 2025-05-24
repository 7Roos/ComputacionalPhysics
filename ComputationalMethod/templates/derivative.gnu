# Plot accuracy between differents formulas for derivative
# M. Roos, 19/03/2025
# Last updated 19/03/2025

#PNG
set terminal pngcairo dashed enhanced size 600,400 font 'arial,12' fontscale 1.0
set output 'dash.png'

#LATEX
set terminal lua tikz linewidth 2 standalone 
set output 'dash.tex'

set encoding utf8

# Label axis
set xlabel "h"
set ylabel "error"

set logscale x
set logscale y

set xtics ('$10^{-1}$' 1E-1, '$10^{-2}$' 1E-2, '$10^{-3}$' 1E-3, '$10^{-4}$' 1E-4, '$10^{-5}$' 1E-5, '$10^{-6}$' 1E-6, '$10^{-7}$' 1E-7, '$10^{-8}$' 1E-8)
set ytics ('$10^{-1}$' 1E-1, '$10^{-2}$' 1E-2, '$10^{-3}$' 1E-3, '$10^{-4}$' 1E-4, '$10^{-5}$' 1E-5, '$10^{-6}$' 1E-6, '$10^{-7}$' 1E-7, '$10^{-8}$' 1E-8)

# Datafile
d2pts = "plots/der2pts.dat"

# Legend
#Position
set key left 

plot d2pts w lp title "2 pts"