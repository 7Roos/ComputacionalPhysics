# Função `create_exercise_statement`

## Descrição
Função utilitária para criar enunciados de exercícios padronizados com caixa decorativa, número do exercício e conteúdo formatado.

## Sintaxe
```python
create_exercise_statement(exercise_number, problem_content, box_colors=[BLUE, AS2700.Y15_SUNFLOWER])
```

## Parâmetros

### `exercise_number` (int)
- **Obrigatório**
- Número do exercício que aparecerá no título
- Exemplo: `2` resulta em "Exercício 2"

### `problem_content` (VGroup ou list)
- **Obrigatório**
- Conteúdo do enunciado do problema
- Pode ser uma lista de objetos `MathTex` ou um `VGroup` já formatado
- Se for uma lista, a função automaticamente organizará os elementos verticalmente

### `box_colors` (list, opcional)
- **Padrão:** `[BLUE, AS2700.Y15_SUNFLOWER]`
- Lista com duas cores para criar o gradiente da caixa
- Primeira cor: início do gradiente
- Segunda cor: fim do gradiente

## Retorno
- **VGroup**: Grupo contendo a caixa decorativa e o problema formatado
- Pronto para ser posicionado e adicionado à cena

## Exemplos de Uso

### Exemplo Básico
```python
problem_content = [
    MathTex("\\text{Uma carga } q_1 \\text{ está a uma distância } R"),
    MathTex("\\text{de uma segunda carga } q_2 \\text{.}")
]

exercise_box = create_exercise_statement(1, problem_content)
exercise_box.to_edge(UL)
self.add(exercise_box)
```

### Exemplo com Cores Customizadas
```python
problem_content = [
    MathTex("\\text{Duas cargas fixas...}").set_color_by_tex_to_color_map({
        "q_1": RED,
        "q_2": BLUE
    })
]

custom_colors = [GREEN, PURPLE]
exercise_box = create_exercise_statement(3, problem_content, custom_colors)
```

### Exemplo com VGroup Pré-formatado
```python
problem_statement = VGroup(
    MathTex("\\text{Primeiro parágrafo}"),
    MathTex("\\text{Segundo parágrafo}")
).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

exercise_box = create_exercise_statement(2, problem_statement)
```

## Vantagens

1. **Consistência Visual**: Todos os exercícios terão o mesmo estilo visual
2. **Facilidade de Uso**: Uma única função para criar enunciados complexos
3. **Flexibilidade**: Suporte a diferentes tipos de conteúdo e cores
4. **Manutenibilidade**: Mudanças no estilo podem ser feitas em um local único
5. **Reutilização**: Código limpo e sem repetição

## Estrutura Gerada

A função retorna um VGroup com a seguinte estrutura:
```
VGroup(
    ├── SurroundingRectangle (caixa decorativa com gradiente)
    └── VGroup (problema)
        ├── Text (título do exercício)
        └── VGroup (conteúdo do problema)
```

## Integração com Classes Existentes

Para usar em suas classes existentes, substitua:

**Antes:**
```python
numberOfExercise = Text("Exercício 2", ...)
problem_statement = VGroup(...)
problem = VGroup(numberOfExercise, problem_statement)
box = SurroundingRectangle(problem, ...)
```

**Depois:**
```python
problem_content = [...]
exercise_box = create_exercise_statement(2, problem_content)
```

Isso reduz significativamente a quantidade de código e garante consistência entre todos os exercícios.

## Sistema de Execução de Cenas

O script agora suporta seleção inteligente de cenas através de argumentos de linha de comando.

### Uso via linha de comando:
```bash
# Executar Prob3
python v3_cartesian.py 3

# Executar Prob2
python v3_cartesian.py 2

# Executar Summary
python v3_cartesian.py summary

# Executar sem argumentos (padrão: Prob2)
python v3_cartesian.py
```

### Uso via script de teste:
```bash
# Mostrar opções disponíveis
./test_scenes.sh

# Executar cena específica
./test_scenes.sh 3
./test_scenes.sh summary
```

### Cenas Disponíveis:
- `1` → Unidimensional_vertical
- `2` → Prob2 (padrão)
- `3` → Prob3
- `vertical` → Prob1_vertical
- `summary` → Summary

### Configuração Automática
O script utiliza um dicionário de mapeamento para determinar qual cena executar:

```python
AVAILABLE_SCENES = {
    "1": "Unidimensional_vertical",
    "2": "Prob2", 
    "3": "Prob3",
    "vertical": "Prob1_vertical",
    "summary": "Summary"
}
```

### Vantagens do Sistema:
1. **Flexibilidade**: Execução de qualquer cena via argumento
2. **Facilidade**: Scripts de teste automatizados
3. **Robustez**: Fallback para cena padrão se argumento inválido
4. **Produtividade**: Teste rápido de diferentes exercícios

## Sistema de Execução de Cenas Melhorado

O sistema agora inclui:

### 1. Sistema de Ajuda Integrado
```bash
# Exibir ajuda completa
python v3_cartesian.py help
python v3_cartesian.py --help
python v3_cartesian.py -h

# Via script de teste
./test_scenes.sh help
```

### 2. Execução Simplificada
```bash
# Execução padrão (Prob2)
python v3_cartesian.py

# Execução por número
python v3_cartesian.py 3      # Executa Prob3
python v3_cartesian.py 1      # Executa Unidimensional_vertical

# Via script de teste (mais amigável)
./test_scenes.sh 3            # Executa Prob3 com feedback
./test_scenes.sh             # Mostra opções e executa padrão
```

### 3. Mapeamento de Cenas Disponível
- `1` → `Unidimensional_vertical`
- `2` → `Prob2` (padrão)
- `3` → `Prob3`
- `vertical` → `Prob1_vertical`
- `summary` → `Summary`

## ✅ Melhorias Implementadas

### Sistema de Execução Aprimorado
1. **Estrutura Reorganizada**: Movido o bloco `if __name__ == "__main__":` para o final do arquivo, após todas as classes e funções
2. **Sistema de Ajuda Completo**: Adicionado suporte para `help`, `-h`, `--help` com informações detalhadas
3. **Feedback de Execução**: O sistema agora informa qual cena está sendo executada
4. **Script de Teste Melhorado**: Atualizado `test_scenes.sh` com opções de ajuda expandidas

### Benefícios das Melhorias
- **🎯 Facilidade de Uso**: Execução mais intuitiva via linha de comando
- **📚 Documentação Integrada**: Ajuda acessível diretamente no script
- **🔧 Debuging Simplificado**: Fácil identificação de qual cena está executando
- **⚡ Workflow Otimizado**: Teste rápido de diferentes exercícios

### Exemplos de Uso Prático
```bash
# Desenvolvimento de novo exercício
python v3_cartesian.py 3      # Testa Prob3 rapidamente

# Comparação entre exercícios
./test_scenes.sh 2            # Executa Prob2
./test_scenes.sh 3            # Executa Prob3

# Verificação completa
./test_scenes.sh help         # Ver todas as opções
python v3_cartesian.py summary # Executar resumo
```

O sistema agora permite desenvolvimento e teste eficiente de múltiplos exercícios com uma interface user-friendly!

## Função create_book_covers

A função `create_book_covers` importa e exibe as capas dos livros Jackson e Griffiths no canto inferior direito das animações Manim.

### Sintaxe
```python
create_book_covers()
```

### Parâmetros
- **Nenhum parâmetro necessário** - Função específica para os livros Jackson e Griffiths

### Retorno
- **Group**: Grupo Manim contendo as capas dos livros Jackson e Griffiths formatadas

### Exemplo de Uso

```python
# Uso simples - sem parâmetros necessários
books = create_book_covers()
self.add(books)
```

### Características
- **Simplificada**: Sem necessidade de parâmetros complexos
- **Específica**: Desenvolvida para os dois livros do projeto (Jackson e Griffiths)
- **Posicionamento Fixo**: Sempre no canto inferior direito
- **Tratamento de Erros**: Cria placeholders em caso de erro no carregamento
- **Escalas Predefinidas**: Jackson (0.22) e Griffiths (1.92)
- **Caminhos Fixos**: 
