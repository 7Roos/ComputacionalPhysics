#!/bin/bash

# Instalador automatizado de pacotes científicos para distribuição Linux Ubuntu e Fedora.
# Há muito pacotes e configurações, e é ruim ficar lembrando de instalar e configurar um por um.
# Então uma alternativa viável foi criar (com o auxílio de IA) este programa.
#
# Matheus Roos, 28/06/2024

##########################################
####### Definição dos pacotes ############
##########################################

# Driver Nvidia
#write: vá para o site "https://www.nvidia.com/en-us/drivers/unix/" e escolha o driver pra instalar

codec_packs=("openh264")
##apt
#sudo add-apt-repository ppa:djcj/hybrid
#sudo apt-get update
#apt-get install openh264
##dnf
#sudo dnf install gstreamer1-plugin-openh264 mozilla-openh264
##pacman
#sudo pacman -Syu base-devel cmake flac fontconfig freetype2 fribidi git harfbuzz jansson lame libass libbluray libjpeg-turbo libogg libsamplerate libtheora libvorbis libvpx libxml2 meson nasm ninja numactl opus python speex x264 xz
#sudo pacman -Syu desktop-file-utils gst-libav gst-plugins-good gtk4

midia_packs=("spotify" "daVinciResolve") #se tiver placa de vídeo.

#write: vá para "https://www.blackmagicdesign.com/br/products/davinciresolve" e baixe.


terminal_pack=("zsh" "fonts-powerline" "Zsh-syntax-highlighting" "Zsh-autosuggestions" "FZF" "Plugin K")
##pacman
#pacman -S zsh
#git clone https://github.com/powerline/fonts.git
#cd fonts
#./install

## all distributions
#chsh -s $(which zsh) #define zsh como padrão
#sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
#git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting #plugin
#git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
#git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install
#git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
#sudo nano ~/.zshrc #para ativar os plugins
#write: adicione na linha plugins escreva: plugins=(git zsh-syntax-highlighting fzf zsh-autosuggestions k)
#write: escolha um tema, vá para diretório ~/.oh-my-zsh/themes/.
#write abra o arquivo de configuração zsh: nano ~/.zshrc
#write: localize a linha que define o tema e altere para o nome do tema escolhido: ZSH_THEME="meu-tema-editado"
#write: recarregue as configurações.


# Array dos id dos pacotes
# Farão partes das intruções de terminal
id_packs=("gfortran" "texlive" "gnuplot" "texstudio" "inkscape" "python3-pip" "fortls" "git" "code" "lapack" "gimp" "rsvg-convert")

# Boas-vindas
echo "**********************************************************"
echo "** Bem-vindo ao Assistente de Instalação Personalizada! **"
echo "**********************************************************"

##########################################
#### Escolha da distribuição Linux #######
##########################################

# Pergunta sobre a distribuição, pois muda um pouco a instalação
#entre diferentes distribuições Linux
echo ""
echo "Selecione a sua distribuição Linux:"
echo "1) Ubuntu"
echo "2) Fedora"
echo ""
read -n 1 distro

# Validação da resposta
while [[ ! $distro =~ ^[12]$ ]]; do
  echo "** Opção inválida! Digite 1 para Ubuntu ou 2 para Fedora: **"
  read -n 1 distro
  #-n 1 garante que o usuário digite apenas um caracter e após isso 'dá um enter' automaticamente
done

# Armazenamento da resposta
if [[ $distro == 1 ]]; then
  distro="ubuntu"
  prefix="apt"
elif [[ $distro == 2 ]]; then
  distro="fedora"
  prefix="dnf"
fi
echo ". Distribuição escolhida: $distro"

##########################################
######### Atualização de pacotes #########
##########################################
sudo $prefix update
if [[ $distro == "ubuntu" ]]; then
  sudo apt -y upgrade && sudo apt -y autoremove
fi

echo "**********************"
echo "Atualização concluída!"
echo "**********************"
echo ""
echo "Vamos instalar os pacotes a seguir?"

# Percorre a lista imprimindo o nome de cada programa que será instalado
for pack in "${packs[@]}"; do
  echo "$pack" #SERIA LEGAL MUDAR A COR PRA DIFERENCIAR OS PACOTES A SEREM INSTALADOS.
done

echo "Pressione Enter para continuar..."
read

##########################################
#### Instalação de pacotes pessoais ######
##########################################

# Percorremos o array com o id dos pacotes a serem instalados
#automatizamos essas instalações juntamente com a criação do prefixo acima
for program in "${id_packs[@]}"; do
  #O loop for percorre a lista id_packs e verifica cada elemento.
  if which $program >/dev/null; then
    echo "$program já está instalado."
  else
    echo "Instalando $program..."

    if [[ $program == "texlive" ]]; then
      #Se o elemento for "texlive-full", um bloco if aninhado verifica o sistema operacional.
      if [[ $distro == "fedora" ]]; then
        # Primeiro instalamos o básico, que é rápido. Depois, ao final, retornamos e instalamos o full.
        # Isso é importante pois podemos enfretar problemas de instalação, e trancar toda a instalação (já me aconteceu),
        # Daí ficará mais fácil de resolver.
        sudo dnf install texlive-scheme-basic
        sudo dnf install -y 'tex(beamer.cls)'
        sudo dnf install -y 'tex(hyperref.sty)'
      elif [[ $distro == "ubuntu" ]]; then
        # Instalação do TexLive no Ubuntu
        sudo apt install -y texlive
      fi
    elif [ $program == "fortls" ]; then
      #linter p/Fortran
      python3 -m pip install --upgrade pip
      pip install fortls
    elif [ $program == "code" ]; then
      if [[ $distro == "fedora" ]]; then
        sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
        echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo >/dev/null
        dnf check-update
      elif [[ $distro == "ubuntu" ]]; then
        sudo apt-get install wget gpg
        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >packages.microsoft.gpg
        sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
        echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main"
        sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null
        rm -f packages.microsoft.gpg
        sudo apt install apt-transport-https
        sudo apt update
      fi
      sudo $prefix install -y $program
    elif [ $program == "lapack" ]; then
      if [[ $distro == "fedora" ]]; then
        sudo yum install lapack lapack-devel blas blas-devel
      elif [[ $distro == "ubuntu" ]]; then
        sudo apt install libblas-dev liblapack-dev
      fi
    elif [ $program == "rsvg-convert" ]; then
      if [[ $distro == "fedora" ]]; then
        sudo dnf install librsvg2-tools -y
      elif [[ $distro == "ubuntu" ]]; then
        sudo apt install librsvg2-bin
      fi
    else
      sudo $prefix install -y $program
    fi
  fi
done

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
#sudo dnf install -y texlive-scheme-full
#sudo apt install -y texlive-full
#spotify fedora
#flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
#flatpak install flathub com.spotify.Client
#sudo ln -s /var/lib/snapd/snap /snap
#snap install spotify
#spotify ubuntu
#snap install spotify

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
