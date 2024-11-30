Vou trabalhar com diferentes séries e ir alternando para ver o que é mais 'lucrativo'.

**1. ShortTips: OneAPI**
   -UpperCase()
   -Snipets
2. Gnuplot: Op. Lógico
   -Estilizando linha: lc, paleta de cores, lw, dt, ls
   -Estilizando eixos: xy label, font, tics, offset, title fig
   -Estilizando legenda: key off, pos, altura entre linhas, font, title, label
   -filledCurve: preenchimento abaixo da curva, add transparência, hachura.
   -gradient legend: multilines legenda em gradiente.
   -multiplot: definições explícitas
   -multiplot: generalizando
   -marcações: arrow e linha horizontal e vertical fora a fora no gráfico
   -MapHeat
   -3D
   -3d: poligon
   -Refinando dados: smooth (sbezier, csplines, slinear) suaviza a curva, unique (remove pontos duplicados)
   -Diagrama de fases
   -Animações
   -Integração com python:
      import Gnuplot
      g = Gnuplot.Gnuplot()
      g('set title "Exemplo de plot com Python"')
      g.plot('sin(x)')
   -Estudar Plotly, Geogebra ou Bokeh (gráficos interativos)
3. Física 3: Coord. Cartesianas
   -Força elétrica entre duas partículas 1D
   -Força elétrica entre duas partículas 2D
   -Força elétrica entre duas partículas 3D
   -"..." três partículas 1D: AF
   -Força elétrica entre três partículas 2D: triângulo equilátero
   -Força elétrica entre 4 partículas 2D: quadrado
4. Física computacional:
   -Implementação derivada em Fortran plot error com gnuplot
   -Implementação Python e plot com matplotilib
   -Implementação Julia e plot
5. Tikz-Latex:
   -Tikzset: redefinir o estilo padrão
   -Alternância de cores AF: if
   -Legenda: positioning
   -Plano com transparência
   -3D rede quadrada
   -3D e 2D com scope
   -Conversão de pdf para outros formatos
   -O que é Tikz
   -3D hexagonal
   -Plots: pgfplots
   -shapes.geometric (myCircle)
   -Fluxograma
   -Diagramas de Circuitos
   -tikz-cd: diagrama de cargas elétricas
   -mapa mental
   -clone Halliday
6. Manim: cores
   -numeração de eq
   -numeração de fig
   -referência
   -fluxograma simples
7. build:
   -Lapack
   -makefile: começar do trivial, obj, S=, flags, clean
   -meson: alternativa
   -doxygen