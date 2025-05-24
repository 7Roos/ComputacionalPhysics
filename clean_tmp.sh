#!/bin/bash

# Diretórios temporários a serem limpos
TMP_DIRS=("/tmp" "/var/tmp")

# Idade máxima dos arquivos em dias
MAX_AGE=7

# Log file
LOG_FILE="/var/log/clean_tmp.log"

# Função para log
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Verifica se é root
if [ "$(id -u)" != "0" ]; then
    echo "Este script precisa ser executado como root"
    exit 1
fi

# Limpa cada diretório
for dir in "${TMP_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        log_message "Limpando $dir"
        # Remove arquivos mais velhos que MAX_AGE dias
        find "$dir" -type f -atime +$MAX_AGE -delete
        # Remove diretórios vazios
        find "$dir" -type d -empty -delete
        log_message "Limpeza de $dir concluída"
    else
        log_message "AVISO: $dir não existe"
    fi
done

log_message "Limpeza concluída" 