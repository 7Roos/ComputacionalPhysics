# Usando comandos condicionais do TeX

## Intro
Um conceito bastante importante em programação é a estrutura de ramificação, isto é, a construção 'if-else'. No primeiro vídeo desta série de estudo do LaTex-TIkz, eu mostrei como utilizar a estrutura de repetição, loops. No qual, nos beneficiamos para automatizar a construção de nossa ilustração. Agora é a vez de utilizarmos condições lógicas para construir figuras. Novamente, vou utilizar a rede quadrada de spins no estado ferromagnético como caso de estudo. Para explorar a aplicação de condicionais, vamos considerar a tarefa de construir uma rede de spins na fase antiferromagnética, isto é, com a alternância de sinal entre seus primeiros vizinhos. Em outras palavras, os círculos poderão assumir apenas duas cores (clara e escura), correspondendo aos estados up e down do spin.

## Ifnum

## ifdim
Compara dimensões (comprimentos)

## ifodd: 
Verifica se um número é ímpar.

## ifx ou \if: 
Compara a igualdade de tokens (útil para comparar strings ou comandos).
```latex
\def\condicao{sim}
  \foreach \i in {1,2} {
    \ifx\condicao\relax % \relax é um token especial que geralmente não é definido
      \node at (0,\i) {Condição não definida};
    \else
      \node at (0,\i) {Condição definida};
    \fi
  }
```

## ifdef: 
Verifica se um comando está definido

# Pacotes LaTeX para lógica condicional:
Existem pacotes LaTeX que fornecem comandos mais amigáveis para estruturas condicionais, que podem ser usados dentro de ambientes TikZ:

## ifthenelse: 
Este pacote oferece comandos como '\ifthenelse{<condição>}{<código se verdadeiro>}{<código se falso>}.':
```latex
\foreach \i in {1,...,5} {
    \ifthenelse{\i < 3}{
      \draw[thick, blue] (\i,0) -- (\i+1,1);
    }{
      \draw[dashed, red] (\i,0) -- (\i+1,1);
    }
  }
```

## ifthen
A biblioteca matemática do PGF (a base do TikZ) oferece a função 'ifthen(<condição>, <valor se verdadeiro>, <valor se falso>)' que pode ser usada dentro de \pgfmathsetmacro ou diretamente na chave evaluate.
```latex
\foreach \i in {1,...,5} {
    \pgfmathsetmacro{\raio}{ifthen(\i < 3, 1, 2)} % Usando ifthen (ver abaixo)
    \draw (2*\i,0) circle (\raio cm);
  }
  \foreach [evaluate=\j as \cor using \j<3 ? "blue" : "red"] \j in {1,...,5} {
    \fill[opacity=0.5, \cor] (2*\j,-2) circle (0.5cm);
  }
```
## Referência
- PGF/TikZ Manual