# Motivação
Vou mostrar como instalar e utilizar o compilador da Intel para Fortran. No início deste ano eu já havia demonstrado como realizar a intalação e configuração para utilizar o 'ifort', o compilador Fortran fornecido pela Intel. Mas algumas
coisas aconteceram e aquele vídeo está um pouco desatualizado, isto é, houve a depreciação do 'ifort' pela Intel e eu encontrei uma maneira mais eficiente para configurar o uso do compilador.

Você não deve mais utilizar o 'ifort', mas sim o 'ifx', como é o atualmente recomendado pela Intel. Uma das principais vantagens do 'ifx' é oferecer suporte a novas instruções de processador, bem como otimizações para GPUs.

# Instalação da base
Mas afinal, o que é OneAPi? Bem, trata-se de uma iniciativa da Intel para unificar o desenvolvimento de aplicações em diversas arquiteturas, como CPUs e GPUs.

Agora, pesquise por OneAPI, entre no link da Intel e selecione o download da base. Escolha Linux se você estiver em uma distribuição Linux. Quanto ao gerenciador de pacotes, escolha 'apt' se você estiver utilizando Ubuntu, ou outra que seja derivada do Debian. No meu caso, estou utilizando Fedora, então vou selecionar 'dnf'. Siga as instruções para download e instalação.

Após a conclusão da instalação, vamos instalar a outra parte. Selecionamos a opção 'Toolkit HPC'. A novidade é que agora podemos baixar todo o pacote HPC ou apenas os utilitários para Fortran. Como estou apenas interessado em Fortran, vou selecionar esta segunda opção. Então seguimos os mesmos passos anteriores.

# Carregando setvars
Agora devemos verificar se a instalação ocorreu com sucesso. Navegamos pelos diretórios até encontrar o arquivo 'setvars.sh', então executamos o script que carregará os programas. Verificamos se o 'ifx' está instalado ao buscar sua versão. Tudo certo até aqui!

Mas é chato carregar esse comando toda vez. Em meu antigo tutorial eu mostrei que poderíamos carregar esse comando no '.bashrc', então toda vez que abrimos um terminal esse script é executado e carrega as variáveis. Funciona, mas podemos ser mais eficientes.

Agora vou trocar para um computador com terminal shell, pois aqui estou utilizando o terminal zsh, e num outro momento vou mostrar como proceder com o terminal zsh. Navegamos até a nossa 'home', habilitamos a visualização de arquivos ocultos com 'ctr+h' e procuramos por '.bash_profile'.
A diferença fundamental deste para o '.bashrc', é que ele é executado a cada sessão, e não a cada novo terminal aberto, como era o caso com '.bashrc', ou seja, otimizamos o processo. Abrimos esse arquivo, e ao final, adionamos os comandos necessários. Salvamos, fechamos e testamos juntamente com o comando 'echo' para ficar mais claro o que estou querendo dizer. Como vimos, funcionou.

# Lapack via MKL
Além disso, podemos utilizar a bilioteca MKL, que oferece rotinas altamente otimizadas para álgebra linear, transformadas de Fourier e outras operações matemáticas, bem como a bilioteca Lapack, que é muito útil para rotinas de álgebra linear como a diagonalização de matrizes, eu utilizo essa parte em minha pesquisa de doutorado. Então, podemos utilizar a biblioteca Lapack através da flag para a biblioteca MKL. Em outras palavras, ao usar a biblioteca MKL temos acesso pela mesma flag à biblioteca Lapack.
No entato, a flag 'mkl' está depreciada, então seguimos a sugestão do compilador e trocamos por 'qmkl'. E novamente, tudo ocorreu bem. Em breve trarei um conteúdo especial de instalação e uso de Lapack mais completo.

Bons códigos para você!