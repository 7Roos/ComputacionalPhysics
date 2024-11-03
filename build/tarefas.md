[] Fazer versão em inglês
[] Alterar o mecanismo de escolha da distribuição, i.e., automatizar 
    # Detectar a distribuição
    distro=$(lsb_release -id | cut -f 2)
[] Criar um dicionário com as distribuições e a distribuição raiz debian, pacman, rhel.
[] Criar um dicionário com o nome dos pacotes que serão informados ao usuário que será instalado.
[] Criar um dicionário com o nome dos pacotes padrão das distribuições
[] Criar um dicionário com pacotes relacionados a computação.
[] Criar três dicionários para os casos particulares do debian, rhel e pacman.
[] Parte 2: configuração do ambiente: git, intel openMP,ssh,...
[] Criar identificador de placa de vídeo

** Ordem de instalação **
[] criar um menu iterativo: 
    # instalar placa de vídeo
    # instalar pacotes padrão
    # configurar 
    # sair