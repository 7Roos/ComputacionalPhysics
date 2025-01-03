# Introdução
Em um vídeo anterior havíamos explorado as principais propriedades e operações envolvendo vetores. Aquela discussão anterior é válida para qualquer sistema de coordenadas, mas ainda assim estava um pouco abstrato demais. Então agora vamos analisar como construir vetores e suas operações no sistema de coordenadas cartesiano, que é o mais popular, e portanto, estará presente na imensa maior parte dos problemas. Este é o último capítulo de revisão antes de começarmos a resolver problemas de eletrostática propriamente dito.

>Mostrar trechos do vídeo anterior e deixar o link da descrição<

# Sitema cartesiano
## 1D
### Definições
Começamos considerando um eixo horizontal que se extende de menos infinito a mais infinito, vamos chamá-lo x. Também definimos um versor 'i', que é um vetor unitário, ou seja, que tem comprimento igual a 1, e nesse caso, que sai da origem zero e aponta na direção positiva de x. 
### Multiplicação por escalar
Podemos multiplicar esse esse versor por um escalar positivo, ou seja, que dá a escala do vetor. Dessa forma, podemos definir um vetor unidimensional com #\vec{A} = a\hat{i}$ que sai da origem, possui comprimento 'a' e aponta da direção positiva do eixo x. 
### Reflexão de vetor
Podemos refletir esse vetor para o sentido negativo, assim $ \vec{A'} = - \vec{A} = a(-\hat{i}) $. Também podemos definir um segundo vetor $ \vec{B} = b\hat{i} $. 
### Soma entre dois vetores
A soma dos vetores A e B será um terceiro vetor $ \vec{C} = (a + b)\hat{i} $. Se ambos os vetores apontam na mesma direção, o vetor C também apontará na mesma direção mais com comprimento maior do que A e B, ou seja, igual a soma dos comprimento A e B. 
### Subtração
Caso os vetores apontem em direções opostas, o vetor C apontará na direção daquele que é o maior vetor, e com comprimento entre A e B. 
### Produto escalar
Também podemos tomar o produto escalar entre A e B. Assim $ \vec{A} \cdot \vec{B} = a\hat{i} \cdot b\hat{i} = ab(\hat{i}\cdot\hat{i}) = ab $. Onde passamos o módulo a e b à frente, uma vez que o produto escalar se dá entre vetores, o produto escalar entre dois vetores paralelos a alinhado é um, se estiverem antialinhados o resultado é -1. Uma outra forma de construir o produto escalar é através do módulo dos vetores envolvidos e o ângulo entre eles. Nesse caso teríamos $ \vec{A} \cdot \vec{B} = ab cos(\theta) $, com $ \theta = 0 $ se estiverem alinhados e $ \theta =  180$ caso estejam antialinhados. Então, par ao primeiro caso, $ cos(0) = 1 $ e $ \vec{A}\cdot\vec{B} = ab $, caso contrário, $ cos(180) = -1 $ e $ \vec{A}\cdot\vec{B} = -ab $. 
### Módulo
Por fim, podemos calcular o módulo de um vetor, que é trivial nesse caso unidimensional. O módulo de A será $ |vec{A}\cdot\vec{A}| = \sqrt{(\vec{A}\cdot\vec{A})} = \sqrt{(a)^{2}} = a $, que é positivo definido. Em outras palavras, é sempre positivo

Ainda está um pouco abstrato, vamos substituir a=2 e b=1, o resultado é esse que você está vendo. Mas já esgotamos todas as operações relevantes em 1D. Vamos para o pŕoximo nível!

>Criar as animações<

## 2D