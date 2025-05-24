# Instalação e configuração do findent e prettify

## Instalação via pip
pip install --user findent
pip install --user fprettify

## Adicionar ao PATH
No BASHRC ou ZSHRC escreva:
export PATH="/home/7roos/.local/bin:$PATH"

## Aplique as alterações
source ~/.zshrc

## Verificar a instalação
which findent
which fprettify

O comando which procura por um executável em todos os diretórios listados no seu PATH.