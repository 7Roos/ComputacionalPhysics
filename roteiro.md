**Série "Fortran In-Depth":**
1. **Estruturas de ramificação:**
   - **Episódio 1: Variáveis Lógicas:**
      -  Explicar o tipo de dados lógico em Fortran (logical).
      -  Mostrar como declarar variáveis lógicas e atribuir valores (True ou False).
      -  Variáveis lógicas como interruptores.

    - **Episódio 2: Operadores Lógicos:**
      -  Operadores relacionais e combinacinais.
      -  Demonstrar como usar esses operadores em expressões lógicas.

    - **Episódio 3: Construção IF-ELSE:**
      -  if-else de uma linha apenas
      -  Apresentar a estrutura básica de um bloco if-else em Fortran.
      -  Mostrar exemplos simples de declarações condicionais.
      -  declaração stop.

    - **Episódio 4: SWITCH ou SELECT CASE:**
      -  Introduzir a construção select case como uma alternativa ao encadeamento de if-else if.
      -  Demonstração de como usar select case para lidar com várias opções.

    - **Episódio 5: Rótulos de Blocos:**
      -  Explicar o uso de rótulos para identificar blocos de código.
      -  Demonstrar situações em que rótulos podem ser úteis, especialmente em loops aninhados.
      -  Quebra de linhs para muitas condições lógicas.

2. **Loops:**
   - **Episódio 1: Loops Condicionais (DO WHILE e DO Vazio):**
      -  Explicação do loop DO WHILE para execução de um bloco enquanto uma condição é verdadeira.
      -  Discussão sobre o uso de DO vazio para loops que executam um bloco um número específico de vezes sem uma condição explícita.
      -  Comentário sobre a instrução go to.

    - **Episódio 2: Loops Iterativos (DO Iterativo):**
      -  Demonstração de loops iterativos usando a construção DO.
      -  Explicação do controle de iteração usando índices e limites.
      -  Loop iterative como um loop condicional (mudança das variáveis a cada iteração).

    - **Episódio 3: Instruções EXIT e CYCLE em Loops:**
      -  Introdução ao uso de EXIT para sair prematuramente de um loop.
      -  Discussão sobre CYCLE para pular para a próxima iteração do loop.
      -  declaração stop.

    - **Episódio 4: Loops Implícitos:**
      -  Explicação de como os loops implícitos funcionam.
      -  Apresentação de loops implícitos para simplificar a impressão de matrizes.
      -  Rótulos de blocos.

3. **Arrays:**
   - **Episódio 1: Vetores Unidimensionais:**
      -  Declaração de vetores unidimensionais (inteiro, real, etc.).
      -  Uso de parâmetros para determinar o tamanho do vetor (vetor parametrizado).
      -  Operações básicas com vetores unidimensionais (soma, subtração, multiplicação por escalar).
      -  Seleção de um intervalo de valores em um vetor.
      -  Utilização de funções intrínsecas como minval, maxval, etc.

    - **Episódio 2: Vetores Multidimensionais (Matrizes):**
      -  Declaração de matrizes (vetores multidimensionais).
      -  Preenchimento de uma matriz usando a função reshape.
      -  Operações com matrizes (soma, subtração, multiplicação por escalar, produto escalar).
      -  Impressão de uma matriz de forma amigável.
      -  Alocação dinâmica de memória para matrizes.
      -  Utilização de funções intrínsecas avançadas como matmul, maxval, etc.

    - **Episódio 3: Abordagens Avançadas com Funções:**
      -  Uso de funções como pseudo-funções, tratando entradas de linha e coluna como inputs e um elemento como resultado da função.
      -  move_alloc

    - **Episódio 4: Loops Implícitos:**
      -  Explicação de como os loops implícitos funcionam.
      -  Apresentação de loops implícitos para simplificar a impressão de matrizes.
      -  Rótulos de blocos.

4. **Funções:**
   - **Episódio 1: Introdução às Funções em Fortran**
      - Funções matemáticas: entradas e saída.
      - Funções inline
      - Explicação sobre funções em Fortran:entradas mais complexas e saída.
      - Demonstração de como declarar, chamar e usar funções: função soma.
      - Exemplos práticos de funções numéricas (inteiro, real, logical, caracter).

   - **Episódio 2: Funções Internas e Externas em Fortran**
      - Diferença entre funções internas e externas.
      - Como criar e utilizar funções internas.
      - Discussão sobre a criação de funções externas e a importância delas.
      - Salvando e compilando um função em um arquivo separado.

   - **Episódio 3: Trabalhando com Variáveis em Fortran**
      - Tipos de variáveis (inteiro, real, logical) e suas características.
      - Escopo de variáveis (Global vs Local) e variáveis fictícias.
      - Boas práticas (atributo intent).
      - Exemplos práticos:
        -Inteiro: Fibonacci;
        -Real: Raiz cúbica;
        -Logical: while dinâmico;
        -Caracter: UpperCase.

   - **Episódio 4: Explorando funções vetorial em Fortran**
      - Funções matemáticas vetoriais.
      - Declaração e inicialização de vetores.
      - Abordagem de funções que retornam vetores em Fortran.
      - Operações com vetores: soma de dois vetores.
      - Exemplos práticos de funções que retornam vetores inteiros, reais, lógicos, etc.
      - Aplicações específicas para funções vetoriais em Fortran: produto matricial

   - **Episódio 5: Uso Avançado de Funções em Fortran**
      - Função recursiva (deve ser evitada, uso de pilha).
      - Atributos pure, elemental.
      - External

4. **Sub-Rotinas:**
   - **Episódio 1: Introdução às Sub-Rotinas em Fortran:**
      -  Explicação sobre o conceito de sub-rotinas.
      -  Diferenças entre funções e sub-rotinas.
      -  Declarando, chamando e utilizando sub-rotinas.
      -  Exemplos práticos de sub-rotinas numéricas.

   - **Episódio 2: Parâmetros em Sub-Rotinas:**
      -  Passagem de parâmetros por valor e por referência.
      -  Uso do atributo intent para indicar a intenção do uso dos parâmetros.
      -  Considerações sobre modificação de parâmetros dentro de sub-rotinas.

   - **Episódio 3: Variáveis Locais e Globais:**
      -  Escopo de variáveis locais e globais em sub-rotinas.
      -  Boas práticas relacionadas à utilização de variáveis locais e globais.
      -  Exemplos práticos de manipulação de variáveis em sub-rotinas.

   - **Episódio 4: Sub-rotinas Internas:**
      -  Explicação sobre sub-rotinas internas.
      -  Vantagens e casos de uso para sub-rotinas internas.
      -  Demonstração de como declarar e utilizar sub-rotinas internas.

   - **Episódio 5: Retorno de Múltiplos Resultados:**
      -  Técnicas para retornar múltiplos resultados de sub-rotinas.
      -  Uso de arrays e estruturas de dados como parâmetros de retorno.
      -  Exemplos práticos de sub-rotinas que retornam mais de um resultado.

   - **Episódio 6: Boas Práticas e Estilo em Sub-Rotinas:**
      -  Diretrizes de boas práticas ao escrever sub-rotinas em Fortran.
      -  Enfatizar clareza, modularidade e reutilização de código.
      -  Exemplos de código bem estruturado e fácil de manter.

5. **Intel VTune Profiler:**