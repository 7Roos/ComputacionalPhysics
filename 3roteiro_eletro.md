# Eletrostática 1D - Tutorial

**Próximos passos:**
- ✅ Construir animação
- ⏳ Narrar
- ⏳ Editar
- ⏳ Fazer Thumb

## Problema
Sejam duas cargas $q_1$ e $q_2$, separadas por uma distância $r$. Qual é a força $\vec{F}_{12}$ entre elas?

## Solução

### 1. Escolha do Sistema de Coordenadas
Primeiro, escolhemos o sistema de coordenadas: **cartesiano unidimensional** é a escolha mais óbvia, uma vez que, pela Lei de Coulomb, a força eletrostática é radial, isto é, aponta na direção que liga as duas cargas.

### 2. Definição do Sistema de Referência
Segundo, definimos o sistema de referência: a escolha mais conveniente é fixar uma das cargas na origem do sistema. Se queremos descobrir qual é a força que outras partículas exercem sobre a carga $q_1$, colocamos ela na origem.

### 3. Aplicação da Lei de Coulomb
Terceiro passo: substituímos os índices 1 e 2 na equação geral da Lei de Coulomb:

$$\vec{F}_{12} = k_0 \frac{q_1 q_2}{|\vec{r}_1 - \vec{r}_2|^3} (\vec{r}_1 - \vec{r}_2)$$

### 4. Identificação das Posições
Agora, precisamos identificar as posições das partículas neste sistema de coordenadas a partir do sistema de referência, isto é, identificar os vetores $\vec{r}_1$ e $\vec{r}_2$, referentes às partículas 1 e 2, em relação à origem. 

Como a partícula 1 está na origem, o vetor $\vec{r}_1$ na direção $x$ é igual ao vetor nulo: $\vec{r}_1 = 0\hat{x}$. 

A partícula 2 está a uma distância $R$ à direita da partícula 1, portanto, no eixo $x$ positivo: $\vec{r}_2 = R\hat{x}$.

### 5. Desenvolvimento Matemático
A partir de agora é matemática. A diferença vetorial entre as posições será:
$$\vec{r}_1 - \vec{r}_2 = 0\hat{x} - R\hat{x} = -R\hat{x}$$

Como é uma equação unidimensional, podemos simplificar a expressão, obtendo uma força proporcional ao inverso do quadrado da distância e apontando no sentido negativo do eixo $x$:

$$\vec{F}_{12} = -k_0 \frac{q_1 q_2}{R^2} \hat{x}$$

### 6. Terceira Lei de Newton
Mas o que acontece com a força $\vec{F}_{21}$? Agora movemos o sistema de referência para a carga $q_2$. Assim:
- $\vec{r}_2 = 0\hat{x}$ (carga 2 na origem)
- $\vec{r}_1 = -R\hat{x}$ (carga 1 à esquerda de $q_2$)

Dessa forma, a força $\vec{F}_{21}$ possui o mesmo módulo de $\vec{F}_{12}$, mesma direção $x$, porém com sentido oposto. 

**Importante:** Nem precisamos invocar explicitamente a terceira lei de Newton - o resultado $\vec{F}_{12} = -\vec{F}_{21}$ emerge naturalmente da matemática!

## Análise dos Sinais

### Cargas de Mesmo Sinal ($q_1 q_2 > 0$)
Se as duas cargas tiverem o mesmo sinal, isto é, o produto das cargas $q_1$ e $q_2$ for **positivo**, a força $\vec{F}_{12}$ aponta no sentido negativo do eixo $x$, e do resultado anterior, $\vec{F}_{21}$ aponta no sentido oposto, isto é, o sentido positivo do eixo $x$. 

**Conclusão:** As cargas se repelem.

### Cargas de Sinais Opostos ($q_1 q_2 < 0$)
Caso as duas cargas tenham sinais opostos, isto é, o produto $q_1 q_2$ for **negativo**, então tanto o sentido da força $\vec{F}_{12}$ como $\vec{F}_{21}$ será invertido, com $\vec{F}_{12}$ apontando agora no sentido positivo do eixo $x$ e $\vec{F}_{21}$ no sentido negativo.

**Conclusão:** As forças $\vec{F}_{12}$ e $\vec{F}_{21}$ serão atrativas.

### Vantagem da Abordagem Matemática
Note este aspecto importante dessa linguagem: você não precisa decorar aquela regra "*iguais se repelem e opostos se atraem*". Isso já está incluído na definição matemática - emerge naturalmente sem intervenção manual.

Num primeiro olhar, pode parecer que o "custo" dessa linguagem é o mesmo de decorar a regra mencionada. Porém, quando seu sistema for mais complexo (com muitas partículas), essa análise via "decoreba" começa a ficar complicada e sujeita a erros. 

Na linguagem matemática, basta:
1. Escolher o sistema de coordenadas
2. Definir o sistema de referência  
3. Identificar os vetores-posição
4. Aplicar a matemática até o resultado final
5. Fazer a análise física

## Análise de Escala

### Cargas de Mesmo Módulo
Se as cargas possuem o mesmo valor em módulo, podemos substituir $q_1 = Q$ e $q_2 = Q$:

$$\vec{F}_{12} = -k_0 \frac{Q^2}{R^2} \hat{x}$$

### Variação das Cargas
Se a segunda carga for o dobro da primeira ($q_2 = 2q_1$), a força será dobrada.

### Variação da Distância
**Impacto da distância:**
- Se a distância for o **dobro** ($R \to 2R$): como $R$ está ao quadrado, a força cairá por um fator de **4**.
- Se a distância for a **metade** ($R \to R/2$): a força aumentará por um fator de **4**.

## Substituição de Valores Numéricos

### Halliday 5ª Edição
No Halliday, 5ª edição, 3º volume, capítulo 25, exercício 3:
- $q_1 = 3{,}12 \times 10^{-6}$ C
- $q_2 = -1{,}48 \times 10^{-6}$ C  
- $r = 0{,}123$ m

### Halliday 12ª Edição
Este problema também está contido na 12ª edição, Vol. 3, Cap. 21, Problema 5, alterando apenas os valores das cargas e a distância entre elas.