#!/bin/bash

# Instalador automatizado de pacotes científicos para distribuição Linux Ubuntu e Fedora.
# Há muito pacotes e configurações, e é ruim ficar lembrando de instalar e configurar um por um.
# Então uma alternativa viável foi criar (com o auxílio de IA) este programa.
#
# Matheus Roos, 28/06/2024
# Last updated, 01/11/2024

##########################################
####### Definição dos pacotes ############
##########################################
build_packs=("nano" "curl" "git" "pip" "pipx")
#nano: editor de texto
#curl: gerenciador de pacotes
#git: versionamento de código
#python3-pip: pip gerenciador de pacotes python
#pipx:

midia_packs=("inkscape" "gimp" "rsvg-convert" "obs-studio" "spotify" "brave")
#inkscape: desenho vetorial
#gimp: editor de imagens
#rsvg-convert: conversor svg -> eps
#obs: obs studio
#spotify: spotify
#brave: navegador

scientific_packs=("gfortran" "texlive" "gnuplot" "texstudio" "fortls" "conda" "lapack" "code")
#gfortran: compilador fortran
#texlive: compilador LaTEX
#gnuplot: editor de gráfico
#texstudio: editor LaTex
#fortls: linter parar fortran
#conda: pacotes python e ambiente virtual
#lapack: bibliotecas de álgebra linear
#code: vs code editor de código

manim_packs=("manim" "manim-slides")
#cairo, pango, ffmpeg: dep from manim
#manim: biblioteca python de animação matemática
#manim-slides: usa manim para gerar slides

terminal_packs=("zsh" "fonts-powerline" "Zsh-syntax-highlighting" "Zsh-autosuggestions" "FZF" "Plugin K")
#zsh: terminal alternativo ao shell
#fonts-powerline": fontes especiais
#Zsh-syntax-highlighting: analisador de sintaxe
#Zsh-autosuggestions: auto-sugestão
#FZF e Plugin K:plugins

function welcome {
  # Função de boas-vindas
  echo "**********************************************************"
  echo "** Bem-vindo ao Assistente de Instalação Personalizada! **"
  echo "**********************************************************"
}

function choose_distro {
  #### Escolha da distribuição Linux - gerenciador de pacotes #######

  # Os comando de instalação podem mudar entre as distribuições,
  # i.e., entre gerenciadores de pacotes, que são três, correspondentes
  # às derivações debian, rhel e arch.
  echo ""
  echo "Selecione o gerenciador de pacotes:"
  echo "1) apt"
  echo "2) dnf"
  echo "3) pacman"
  echo ""
  #-n 1 garante que o usuário digite apenas um caracter e após isso 'dá um enter' automaticamente
  read -n 1 distro

  # Validação da resposta
  while [[ ! $distro =~ ^[123]$ ]]; do
    echo "** Opção inválida! Digite 1 para apt, 2 para dnf ou 3 para pacman: **"
    read -n 1 distro
  done

  # Armazenamento da resposta
  if [[ $distro == 1 ]]; then
    distro="debian"
    prefix="apt"
  elif [[ $distro == 2 ]]; then
    distro="rhel"
    prefix="dnf"
  elif [[ $distro == 3 ]]; then
    distro="arch"
    prefix="pacman"
  fi
  echo ". Gerenciador de pacotes: $prefix"

  # Limpa o arquivo de log antes de iniciar
  >install.log

  # Regsitro no arquivo de log
  echo "Gerenciador de pacotes: $prefix" >>install.log
  echo "" >>install.log
}

function update_system {
  ######### Atualização de pacotes: ########
  if [[ $prefix == "apt" ]]; then
    sudo $prefix update
    sudo apt -y upgrade && sudo apt -y autoremove
  elif [[ $prefix == "rhel" ]]; then
    sudo $prefix -y update
  elif [[ $prefix == "pacman" ]]; then
    sudo $prefix -Syu --noconfirm
    # Não há removedor de pacotes automático, você deve analisar caso a caso.
  fi

  ##################################
  #### Instalação dos pacotes ######
  ##################################

  echo ""
  echo "**********************"
  echo "Atualização concluída!"
  echo "**********************"
}

color_print() {
  # $1: Texto a ser impresso
  # $2: Cor (opcional)
  # $3: Estilo (opcional)

  ### Dicionário:
  ## Cores (Códigos ANSI):
  #30: Preto
  #31: Vermelho
  #32: Verde
  #33: Amarelo
  #34: Azul
  #35: Magenta
  #36: Ciano
  #37: Branco
  ## Estilos:
  #1: Negrito
  #4: Sublinhado
  #7: Invertido

  color=${2:-32}m # Cor verde por padrão
  style=${3:-0}   # Estilo normal por padrão
  echo -e "\e[$style;$color$1\e[0m"
}

print_packages() {
  # Percorre a lista imprimindo o nome de cada pacote

  echo ""
  echo "Esses pacotes serão instalados"

  for pack in "${@}"; do
    color_print "$pack"
  done
  echo ""

  # Pausar a execução por 5 segundos
  sleep 2
}

function check_installation {
  # Não está funcionando perfeitamente, precisa de ajustes!
  # Não está capturando erros de instalação e programas já instalados
  #com nome diferente, e.g., texlive e pdflatex
  # $1: Nome do programa
  local program="$1"

  if [ $? -ne 0 ]; then
    color_print "Erro ao instalar $program" 31
    echo "Erro ao instalar $program" >>install.log
  else
    echo "$program instalado" >>install.log
  fi
}

suscess_install() {
  echo ""
  color_print "**********************" 33
  echo $1
  color_print "**********************" 33
  echo ""
  echo "Vamos prosseguir!"
}

welcome

######################
## Parte 1: Definição
######################
choose_distro

######################
## Parte 2: Atualização
######################
update_system

print_packages "${build_packs[@]}"
echo "build_packs:" >>install.log
echo "" >>install.log

######################
## Parte 3: instalação
######################
# Essentials
for program in "${build_packs[@]}"; do
  # Verifica se o programa já está instalado
  if ! command -v $program &>/dev/null; then
    if [[ $prefix == "apt" ]]; then
      if [[ $program == "pip" ]]; then
        sudo $prefix install -y python3-pip
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "dnf" ]]; then
      if [[ $program == "git" ]]; then
        sudo yum install git-all
      elif [[ $program == "pip" ]]; then
        sudo $prefix install -y python3-pip
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "pacman" ]]; then
      if [[ $program == "pipx" ]]; then
        python3 -m pip install --user pipx
        python3 -m pipx ensurepath
      elif [[ $program == "pip" ]]; then
        sudo $prefix install -y python3-pip
      else
        sudo $prefix -Syu -y $program
      fi
    fi

    check_installation "$program"

    if [[ $program == "pipx" ]]; then
      pipx ensurepath
    fi
  else
    echo "$program já estava instalado" >>install.log
  fi
done

suscess_install "Pacotes essenciais instalados"
print_packages "${midia_packs[@]}"
echo "" >>install.log
echo "midia_packs:" >>install.log
echo "" >>install.log

# Midia
for program in "${midia_packs[@]}"; do
  # Verifica se o programa já está instalado
  if ! command -v $program &>/dev/null; then
    if [[ $prefix == "apt" ]]; then
      if [[ $program == "rsvg-convert" ]]; then
        sudo $prefix install librsvg2-bin
      elif [[ $program == "brave" ]]; then
        sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
        echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
        sudo apt update
        sudo apt install -y brave-browser
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "dnf" ]]; then
      if [[ $program == "rsvg-convert" ]]; then
        sudo $prefix install librsvg2-tools
      elif [[ $program == "spotify" ]]; then
        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
        flatpak install flathub com.spotify.Client
        sudo ln -s /var/lib/snapd/snap /snap
        snap install spotify
      elif [[ $program == "brave" ]]; then
        sudo dnf install -y dnf-plugins-core
        sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
        sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
        sudo dnf install -y brave-browser
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "pacman" ]]; then
      if [[ $program == "rsvg-convert" ]]; then
        sudo $prefix -Syu librsvg
      elif [[ $program == "spotify" ]]; then
        sudo $prefix -Syu spotify-launcher
      elif [[ $program == "brave" ]]; then
        sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
        sudo zypper addrepo https://brave-browser-rpm-release.s3.brave.com/brave-browser.repo
        sudo zypper install brave-browser
      else
        sudo $prefix -Syu $program
      fi
    fi

    check_installation "$program"
  else
    echo "$program já estava instalado" >>install.log
  fi
done

suscess_install "Pacotes de midia instalados"
print_packages "${scientific_packs[@]}"
echo "" >>install.log
echo "scientific_packs:" >>install.log
echo "" >>install.log

for program in "${scientific_packs[@]}"; do
  # Verifica se o programa já está instalado
  if ! command -v $program &>/dev/null; then
    if [[ $prefix == "apt" ]]; then
      if [[ $program == "texlive" ]]; then
        sudo apt install -y texlive
        sudo apt install -y texlive-full
      elif [[ $program == "fortls" ]]; then
        python3 -m pip install --upgrade pip
        pip install fortls
      elif [[ $program == "conda" ]]; then
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
      elif [[ $program == "lapack" ]]; then
        sudo apt install libblas-dev liblapack-dev
      elif [[ $program == "code" ]]; then
        sudo apt-get install wget gpg
        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg
        sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
        echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main"
        sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null
        rm -f packages.microsoft.gpg
        sudo apt install apt-transport-https
        sudo apt update
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "dnf" ]]; then
      if [[ $program == "gfortran" ]]; then
        sudo $prefix install -y gcc-gfortran
      elif [[ $program == "texlive" ]]; then
        sudo $prefix install -y texlive-scheme-basic
        sudo $prefix install -y 'tex(beamer.cls)'
        sudo $prefix install -y 'tex(hyperref.sty)'
        sudo $prefix install -y texlive-scheme-full
      elif [[ $program == "fortls" ]]; then
        python3 -m pip install --upgrade pip
        pip install fortls
      elif [[ $program == "conda" ]]; then
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
      elif [[ $program == "lapack" ]]; then
        sudo yum install lapack lapack-devel blas blas-devel
      elif [[ $program == "code" ]]; then
        sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
        echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo >/dev/null
        dnf check-update
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "pacman" ]]; then
      if [[ $program == "gfortran" ]]; then
        sudo $prefix -Syu gcc-gfortran
      elif [[ $program == "texlive" ]]; then
        sudo $prefix -Syu texlive-most
        sudo $prefix -Syu install texlive-* #full
      elif [[ $program == "fortls" ]]; then
        python3 -m pip install --upgrade pip
        pip install fortls
      elif [[ $program == "conda" ]]; then
        mkdir -p ~/miniconda3
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
      elif [[ $program == "lapack" ]]; then
        sudo $prefix -Syu blas lapack
      elif [[ $program == "code" ]]; then
        sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
        echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/zypp/repos.d/vscode.repo >/dev/null
        sudo zypper refresh
        sudo zypper install code
      else
        sudo $prefix -Syu $program
      fi
    fi
    check_installation "$program"
  else
    echo "$program já estava instalado" >>install.log
  fi
done

suscess_install "Pacotes científicos instalados"
print_packages "${manim_packs[@]}"
echo "" >>install.log
echo "manim_packs:" >>install.log
echo "" >>install.log

for program in "${midia_packs[@]}"; do
  # Verifica se o programa já está instalado
  if ! command -v $program &>/dev/null; then
    if [[ $prefix == "apt" ]]; then
      if [[ $program == "manim" ]]; then
        sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
        pip3 install manim
      elif [[ $program == "manim-slides" ]]; then
        pipx install -U "manim-slides[pyside6-full]"
      fi
    elif [[ $prefix == "dnf" ]]; then
      if [[ $program == "manim" ]]; then
        sudo dnf install cairo-devel pango-devel
        sudo dnf install python3-devel
        sudo dnf install ffmpeg
        pip3 install manim
      elif [[ $program == "manim-slides" ]]; then
        pipx install -U "manim-slides[pyside6-full]"
      fi
    elif [[ $prefix == "pacman" ]]; then
      if [[ $program == "manim" ]]; then
        sudo pacman -S cairo pango ffmpeg
        pip3 install manim
      elif [[ $program == "manim-slides" ]]; then
        pipx install -U "manim-slides[pyside6-full]"
      fi
    fi
  else
    echo "$program já estava instalado" >>install.log
  fi
done

suscess_install "Pacotes manim instalados"
print_packages "${terminal_packs[@]}"
echo "" >>install.log
echo "terminal_packs:" >>install.log
echo "" >>install.log

for program in "${terminal_packs[@]}"; do
  # Verifica se o programa já está instalado
  if ! command -v $program &>/dev/null; then
    if [[ $prefix == "apt" ]]; then
      if [[ $program == "Zsh-syntax-highlighting" ]]; then
        sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
      elif [[ $program == "Zsh-autosuggestions" ]]; then
        git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
      elif [[ $program == "FZF" ]]; then
        git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
      elif [[ $program == "Plugin K" ]]; then
        git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "dnf" ]]; then
      if [[ $program == "Zsh-syntax-highlighting" ]]; then
        sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
      elif [[ $program == "Zsh-autosuggestions" ]]; then
        git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
      elif [[ $program == "FZF" ]]; then
        git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
      elif [[ $program == "Plugin K" ]]; then
        git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
      else
        sudo $prefix install -y $program
      fi
    elif [[ $prefix == "pacman" ]]; then
      if [[ $program == "fonts-powerline" ]]; then
        git clone https://github.com/powerline/fonts.git
      elif [[ $program == "Zsh-syntax-highlighting" ]]; then
        sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
      elif [[ $program == "Zsh-autosuggestions" ]]; then
        git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
      elif [[ $program == "FZF" ]]; then
        git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
      elif [[ $program == "Plugin K" ]]; then
        git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
      else
        sudo $prefix install -y $program
      fi
    fi
  else
    echo "$program já estava instalado" >>install.log
  fi
done

######################
## Parte 4: configuração
######################
echo ""
echo "**********************"
echo "Configurar Git? [y/n]"
echo "**********************"
read -n 1 git
if [[ $git == "y" ]]; then
  echo "Qual é o nome de usuário?"
  read user
  git config --global user.name "$user"
  echo "Qual é o e-mail?"
  read email
  git config --global user.email $email

  #Configuramos o VS Code como editor padrão
  git config --global core.editor 'code --wait'

  #Verificação de configuração
  git config --list
fi

# Instalações extras

#ADICIONAR MAIS PACOTES A PARTIR DAQUI

# Percorrer a lista e verificar cada programa
#for id_packs in $programas; do
#  if which $programa >/dev/null; then
#    echo "$programa instalado com sucesso!"
#  else
#    echo "Erro: Falha na instalação do $programa."
#  fi
#done
# which verifica se um comando ou programa específico está instalado e
#retorna o caminho do arquivo executável
# >/dev/null redireciona a saída do comando which para o dispositivo nulo,
#isso quer dizer que a saída do comando não será exibida na tela.

# Font para muitos dos comandos: https://command-not-found.com/

#Talvez no futuro implementar um menu iterativo
# Cria uma caixa de diálogo com duas opções
#choice=$(whiptail --title "Escolha uma opção" --menu "O que você deseja fazer?" 10 30 2 \
#  "Instalar pacotes" "1" \
#  "Atualizar o sistema" "2" 3>&1 1>&2 2>&3)
