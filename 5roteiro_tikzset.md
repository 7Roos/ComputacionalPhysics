# Introdução
Podemos melhorar o nosso script anterior ao redefinir valores padrão do Tikz, o que eu quero dizer com isso, é se você decidir que todas as linhas que serão desenhadas terão a cor azul, você não precisará escrever color=blue em todas as definições de linhas. Ao invés disso você pode redefinir o valor padrão uma única vez em seu script, e alterar diretamente no desenho caso queira outra cor. Vamos ver como isso é possível em LaTex-Tikz

# Redefinindo o estilo da linha
Podemos redefinir localmente no espoco o estilo padrão das linhas, usamos "help lines/.style={color=blue,very thin}", você poderá substituir a cor que desear e a espessura da linha. Ou então, redefinir globalmente, com tikzset, isso trará maior flexibilidade ao seu código. Dessa forma, podemos usar:
```
\tikzset{help lines/.style=very thin}
```
Também podemos parametrizar os estilos. Podemos definir a cor padrão azul, e se o usuário definir uma cor diferente, tome 50% dela. Assim, a sintaxe ficaria
```
\begin{tikzpicture}
[Karl's grid/.style ={help lines,color=#1!50},
Karl's grid/.default=blue]
\draw[Karl's grid] (0,0) grid (1.5,2);
\draw[Karl's grid=red] (2,0) grid (3.5,2);
\end{tikzpicture}
```

Além disso podemos definir um estilo próprio, personalizada, podemos chamar de mystyle
```
my style/.style={draw=red,fill=red!20}
```

Por exemplo, fazer definir a cor, e tamanho para todos os círculos através do ambiente 'tikzset'. Nessa sintaxe, definimos que todos os nós terão o seguinte estilo: circle, draw e com fill igual à 20% de azul.
```
\tikzset{
  every node/.style={circle,draw,fill=blue!20},
  every edge/.style={draw=black,->}
}
```

\begin{tikzpicture}[
  % Estilos globais
  every node/.style={circle,draw,fill=blue!20},
  every edge/.style={draw=black,->},
  
  % Estilo personalizado para linhas horizontais
  horizontal line/.style={help lines,color=red}
]

% Desenho
\draw[horizontal line] (0,0) -- (4,0);
\node[label=above:A] at (1,1) {};
\node[label=above:B] at (3,1) {};
\draw[->] (A) -- (B);
\end{tikzpicture}