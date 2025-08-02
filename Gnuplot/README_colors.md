# Visualizador de Cores do Gnuplot com Manim

Este projeto gera visualizações das cores predefinidas do Gnuplot usando Python e Manim.

## 📁 Arquivos

- `colornames.md` - Lista completa das 111 cores predefinidas do Gnuplot
- `gnuplot_colors_manim.py` - Script principal com classe GnuplotColorsStatic
- `gnuplot_colors_categorized.py` - Versões categorizadas e compactas
- `generate_color_charts.sh` - Script de conveniência para gerar todas as versões
- `colors.gnu` - Script Gnuplot original (corrigido)

## 🎨 Visualizações Disponíveis

### 1. GnuplotColorsStatic
- Layout em grid organizado
- Mostra nome da cor e código RGB
- Ideal para referência completa

### 2. GnuplotColorsCategorized  
- Cores organizadas por categorias (Vermelhos, Azuis, etc.)
- Mais fácil para encontrar tons similares
- Layout hierárquico

### 3. GnuplotColorsCompact
- Versão mais compacta
- Apenas os quadrados coloridos
- Ideal para visão geral rápida

## 🚀 Como Usar

### Método Rápido
```bash
./generate_color_charts.sh
```

### Método Manual
```bash
# Versão estática
manim -pql gnuplot_colors_manim.py GnuplotColorsStatic

# Versão categorizada
manim -pql gnuplot_colors_categorized.py GnuplotColorsCategorized

# Versão compacta
manim -pql gnuplot_colors_categorized.py GnuplotColorsCompact

# Alta qualidade
manim -pqh gnuplot_colors_manim.py GnuplotColorsStatic
```

## 📊 Informações das Cores

O arquivo `colornames.md` contém 111 cores predefinidas do Gnuplot, cada uma com:
- Nome da cor
- Código hexadecimal (#RRGGBB)
- Valores RGB (0-255)

### Exemplo de uso no Gnuplot:
```gnuplot
# Usar cor predefinida
set style line 1 lc rgb "dark-red"

# Ou usar código hex
set style line 2 lc rgb "#8b0000"

# Listar todas as cores disponíveis
show colornames
```

## 🔧 Dependências

- Python 3.10+
- Manim Community Edition
- Ambiente conda configurado

## 📂 Estrutura de Saída

```
media/
├── images/
│   ├── gnuplot_colors_manim/
│   │   └── GnuplotColorsStatic_ManimCE_v0.18.1.png
│   └── gnuplot_colors_categorized/
│       ├── GnuplotColorsCategorized_ManimCE_v0.18.1.png
│       └── GnuplotColorsCompact_ManimCE_v0.18.1.png
```

## 🎯 Uso Prático

1. **Para scripts Gnuplot**: Use os nomes das cores diretamente
2. **Para documentação**: Use as imagens geradas como referência
3. **Para desenvolvimento**: Consulte os códigos RGB para outras linguagens

## 🐛 Solução de Problemas

### Problema Original
O script `colors.gnu` original gerava imagem vazia (0 KB) porque faltava o comando `plot NaN`.

### Solução
- Adicionado `plot NaN notitle` ao final do script Gnuplot
- Criada alternativa em Python/Manim para maior flexibilidade
- Scripts organizados e documentados

## 📝 Notas

- As imagens são geradas em formato PNG
- Qualidade baixa (-pql) é mais rápida para testes
- Qualidade alta (-pqh) é melhor para documentação final
- O script automaticamente categoriza as cores por nome
