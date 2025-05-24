# Derivada numérica com python
-Terminar roteiro
-Revisar
-Gravar
-Editar
-Gerar Thumb

## Intro
-A primer on Scientific Programing, pág. 689

## Implementação
A biblioteca math é importada para utilizar a função math.cos(x) para calcular o cosseno de x.
A função f(x) é definida para representar a função da qual queremos calcular a derivada. Neste caso, é a função cosseno.
O programa solicita ao usuário que digite os valores de x e h.
A função input() em Python é uma forma conveniente de obter entrada do usuário, combinando a exibição de uma mensagem com a leitura da entrada. Essa linha exibe a mensagem "Digite o valor de x: " na tela. Em seguida, o programa aguarda que o usuário digite um valor e pressione Enter.
O valor digitado pelo usuário é retornado como uma string.
A função float() é usada para converter essa string por input() em um número de ponto flutuante (um número decimal). Isso é necessário porque, por padrão, input() sempre retorna uma string.
map(float, ...): Aplica a função float() a cada elemento da lista de substrings.

### Map
Recebe como argumentos a função que você deseja aplicar a cada elemento do iterável e o iterável: O iterável que você deseja processar.

map() aplica a função a cada elemento do iterável, um por um.
Pode parecer um pouco abstrata à primeira vista. Vamos desvendar essa ideia com uma analogia e alguns exemplos práticos. Imaginemos um iterador como uma fábrica de valores sob demanda. No qual, um iterador atua como uma fábrica que não produz todos os seus produtos de uma vez, mas sim sob demanda. Quando você pede um produto, a fábrica o produz e entrega. Quando você pede outro, ela produz e entrega o próximo, e assim por diante.

No caso do map(), o iterador é como uma fábrica que aplica uma função a cada elemento de um iterável. Em vez de calcular e armazenar todos os resultados de uma vez, ele os calcula e os entrega um por um, conforme você os solicita.

Mas por que utilizar iteradores?

A resposta é a eficiência no uso de memória: Se você tiver um iterável muito grande, calcular e armazenar todos os resultados de uma vez pode consumir muita memória. Iteradores evitam esse problema, pois calculam os resultados apenas quando necessário.
Os iteradores são ideais para processar dados que chegam em fluxo contínuo, como dados de um arquivo ou de uma conexão de rede.

Por fim, a função split(',') divide uma string em uma lista de substrings, usando a vírgula (,) como delimitador. Vamos ver um exemplo...
**Construir um exemplo**

## Investigando vários valores de h
Agora, para investigar os vários valores de H, substituímos a linha com a função 'Map' em detrimento de apenas perguntar para o usuário o valor X, pois os valores de H agora serão iterados no 'Loop' na linha 15. Definimos o 'Loop' através do comando 'For' e o contador por 'i'. A função range(1, 9) gera uma sequência de números de 1 a 8, que serão utilizados como expoentes no cálculo de h. 
**Calculamos o valor**

# Derivada numérica com Julia
A função f(x) é definida usando a palavra-chave function e retorna o cosseno de x usando a função cos(x) da biblioteca padrão de Julia. Na linha 9, 'Print' exibe uma mensagem na tela. Na linha 10, a função 'Readline' lê uma linha inteira digitada pelo usuário como uma string na entrada padrão (o teclado). Enquanto isso, a função 'Split' divide a 'String' em 'Substrings', usando a vírgula como delimitador e a função 'Parse' converte cada substring em um número de ponto flutuante de 64 bits. Dessa forma, atribui os valores informados pelo usuário e convertidos às variáveis X e H. Essa sintaxe em Julia é chamada de 'Broadcast' e aplica a função 'Parse' a cada elemento do 'Array' retornado por 'Split'. 

O broadcast é uma funcionalidade poderosa em Julia, que permite aplicar uma função a cada elemento de uma coleção (arrays) de forma elegante e com uma sintaxe enxuta. É um conceito semelhante ao de vetorização em outras linguagens, como o NumPy em Python. Neste trecho, o símbolo de ponto é o operador de broadcast. À esquerda do operador, teremos o a função que desejamos aplicar (parse), e à direita, os elementos que vão sofrer a ação da função. Dentre as vantagens, temos uma sintaxe mais concisa e a possibilidade de otimização pelo compilador Julia. Esse mecanismo possui um efeito semelhante ao 'map' em Python. Em Fortran não há a necessidade desse operador, pois o separador de entradas do usuário já é a vírgula, e o tipo que será lido já está definido, seja ele do tipo real ou lógico, por exemplo. 

Na linha 13, o cálculo da derivada é idêntico aos casos da linguagem Fortran e Python. Na linha 16, a função 'Print Ln'  imprime o resultado na tela, formatando a string de forma semelhante ao Python. A principal diferença para 'print' e 'println', como você pode notar, é que no segundo caso há uma quebra de linha, portanto, meramente estético.