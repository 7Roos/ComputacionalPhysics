# Tutorial for the use of the style in lines
# M. Roos, 19/03/2025
# Last updated 27/03/2025

#PNG
#set terminal pngcairo #enhanced size 600,400 font 'arial,12' fontscale 1.0
#set output 'dash.png'

#LATEX
set terminal lua tikz linewidth 1 standalone 
set output 'dash.tex'

set encoding utf8

# Label axis
set xlabel "$x$"
set ylabel "$f(x) = cos x$"

# Datafile
data = "cos.dat"

# Legend
set key at graph 0.25,0.51
set key font ',12'

#plot data u ($1 <= 1?$1:1/0):2 w l lt 10 title "FO", \
#'' u ($1 >= 1?$1:1/0):2 w l lt 2 title "SO"

# Definir cores para uso em fundo escuro
set border linecolor rgb "white"
set key textcolor rgb "white"
set xlabel textcolor rgb "white"
set ylabel textcolor rgb "white"
set xtics textcolor rgb "white"
set ytics textcolor rgb "white"

set label 1 at graph 0.5,0.9
set label 1 "Lyne type" font ',16' textcolor rgb "white"
# Line types
unset monochrome
## Specific by integer
plot data w l lt 1 lw 3 title "lt 1", '' u 1:(1.2*$2) w l lt 2 lw 3 title "lt 2",  \
'' u 1:(1.3*$2) w l lt 3 lw 3 title "lt 3", '' u 1:(1.4*$2) w l lt 4 lw 3 title "lt 4", \
'' u 1:(1.5*$2) w l lt 5 lw 3 title "lt 5", '' u 1:(1.6*$2) w l lt 6 lw 3 title "lt 6", \
'' u 1:(1.7*$2) w l lt 7 lw 3 title "lt 7", '' u 1:(1.8*$2) w l lt 8 lw 3 title "lt 8"

# Line width
## Specific by integer or real number
#plot data w l lt 1 lw 1  title "lw 1", '' u 1:(1.2*$2) w l lt 1 lw 2 title "lw 2",  \
#'' u 1:(1.3*$2) w l lt 1 lw 3 title "lw 3", '' u 1:(1.4*$2) w l lt 1 lw 4 title "lw 4", \
#'' u 1:(1.5*$2) w l lt 1 lw 5 title "lw 5", '' u 1:(1.6*$2) w l lt 1 lw 6 title "lw 6", \
#'' u 1:(1.7*$2) w l lt 1 lw 7 title "lw 7", '' u 1:(1.8*$2) w l lt 1 lw 8 title "lw 8"

# Dash type
## Specific by integer number
#plot data w l lt 3 lw 3 dt 1 title "dt 1", '' u 1:(1.2*$2) w l lt 3 lw 3 dt 2 title "dt 2",  \
#'' u 1:(1.3*$2) w l lt 3 lw 3  dt 3 title "dt 3", '' u 1:(1.4*$2) w l lt 3 lw 3 dt 4 title "dt 4", \
#'' u 1:(1.5*$2) w l lt 3 lw 3  dt 5 title "dt 5", '' u 1:(1.6*$2) w l lt 3 lw 3 dt 6 title "dt 6", \
#'' u 1:(1.7*$2) w l lt 3 lw 3  dt 7 title "dt 7", '' u 1:(1.8*$2) w l lt 3 lw 3 dt 8 title "dt 8"
## Specific by characters pattern
#set key at graph 0.57,0.45
#set key reverse Left
#set key sample 3
#plot data w l lt 1 lw 3 dt solid title "solid", '' u 1:(1.2*$2) w l lt 2 lw 3 dt "." title "dotted",  \
#'' u 1:(1.3*$2) w l lt 3 lw 3 dt "-" title "dashed", '' u 1:(1.4*$2) w l lt 4 lw 3 dt "-" title "dashed 2", \
#'' u 1:(1.5*$2) w l lt 5 lw 3 dt " " title "solid 2", '' u 1:(1.6*$2) w l lt 6 lw 3 dt ".-." title "dotted-dotted-dashed", \
#'' u 1:(1.7*$2) w l lt 7 dt 7 lw 3 title "double dashed", '' u 1:(1.8*$2) w l lt 8 dt 8 lw 3 title "dashed-dotted-dotted"
## Numerical representation
### (<solid length>,<emptyspace length>)
#plot data w l lw 6 dt (1,1) title '(1,1)', '' u 1:(1.2*$2) w l lw 6 dt (5,5) title '(5,5)', \
#'' u 1:(1.3*$2) w l lw 6 dt (4,2,4,4) title '(4,2,4,4)'

# Line color
#plot data w l lc 'red' title 'lc', '' u 1:(1.2*$2) w l lt 1 lc 'green' title 'lt+lc', \
#'' u 1:(1.3*$2) w l lw 4 lc 'blue' title 'lw+lc', '' u 1:(1.4*$2) w l lw 4 dt 2 lc 'orange' title 'lw+dt+lc'