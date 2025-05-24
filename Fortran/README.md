# Configuração do Ambiente Fortran no Cursor

Este guia demonstra como configurar o ambiente Fortran no Cursor IDE.

## Pré-requisitos

1. Intel OneAPI Toolkit instalado
2. Extensão C/C++ instalada no Cursor
3. Fortran Language Server (fortls) instalado
4. Findent (formatador Fortran) instalado

## Configuração do Ambiente

1. Instale a extensão C/C++ no Cursor
2. Certifique-se de que o Intel OneAPI está configurado no seu PATH
3. Instale as ferramentas de desenvolvimento Fortran:
   ```bash
   pip install fortls
   pip install findent
   ```

## Estrutura do Projeto

- `.vscode/settings.json`: Configurações do editor
    1. Este arquivo é importante porque:
        - Configura o Ambiente de Desenvolvimento:
        - Configura o servidor de linguagem (fortls)
        - Define o formatador de código (findent)
    2. Habilita Recursos Automáticos:
        - Formatação automática ao salvar
        - Formatação enquanto digita
        - Análise de código (linting)
    3. Personaliza o Comportamento:
        - Define o estilo de indentação
        - Configura como os arquivos são tratados
        - Define padrões de formatação
    No VS Code, você pode acessar essas configurações de duas formas:
    1. Através da interface gráfica: 'Ctrl+', ou 'Cmd+',
    2. Editando diretamente o arquivo 'settings.json'
    Estas configurações são específicas para o seu projeto e ajudam a manter um ambiente de desenvolvimento consistente e produtivo para programação em Fortran.
- `.vscode/tasks.json`: Configurações de build
    Este arquivo é importante porque:
    1. Automatiza o Processo de Build:
        - Define como compilar seu código Fortran
        - Configura o comando exato do compilador
        - Especifica os argumentos necessários
    2. Facilita o Desenvolvimento:
        - Permite compilar com um atalho (Ctrl+Shift+B ou Cmd+Shift+B)
        - Usa variáveis como ${file} para trabalhar com qualquer arquivo
        - Mantém a consistência do processo de compilação
    3. Personaliza o Comportamento:
        - Define como o terminal se comporta durante a compilação
        - Configura onde os erros são mostrados
        - Permite adicionar mais tasks conforme necessário
    Por exemplo, você poderia adicionar outras tasks como:
    - Limpar arquivos compilados
    - Executar testes
    - Gerar documentação
    - Compilar com diferentes flags
    - Cada projeto pode ter seu próprio tasks.json com configurações específicas, tornando o processo de desenvolvimento mais eficiente e padronizado.
- `Fortran_InDepth.f90`: Exemplo de código Fortran

## Comandos Úteis

- Compilar: `Ctrl+Shift+B` ou `Cmd+Shift+B`
- Formatar código: `Shift+Alt+F`
- Executar: `./nome_do_programa`

## Recursos do Ambiente

- Syntax highlighting
- Auto-completar
- Formatação automática
- Linting
- Compilação integrada
- Debugging

## Dicas para o Tutorial

1. Demonstre a instalação da extensão C/C++
2. Mostre a configuração do ambiente
3. Demonstre a edição e compilação de código
4. Mostre os recursos de formatação e linting
5. Demonstre o debugging 

1. Configuração do Ambiente:
Criamos .vscode/settings.json com configurações específicas para Fortran
Configuramos o compilador Intel Fortran (ifx)
Configuramos o formatador (findent) e o linter (fortls)
2. Sistema de Build:
Criamos .vscode/tasks.json para configurar a compilação automática
Configuramos atalhos de teclado para build e execução
3. Documentação:
Criamos um README.md detalhado com instruções
Incluímos dicas para o tutorial

Para o seu tutorial no YouTube, você pode seguir esta estrutura:
1. Introdução:
    - Apresentar o Cursor e suas capacidades
    -Explicar por que usar Fortran no Cursor
2. Configuração:
    - Mostrar a instalação da extensão C/C++
    - Demonstrar a configuração do ambiente
    - Explicar as configurações no settings.json
3. Desenvolvimento:
    - Mostrar a edição de código com syntax highlighting
    - Demonstrar auto-completar e formatação
    - Mostrar a compilação e execução
4. Recursos Avançados:
    - Demonstrar o linting
    - Mostrar o debugging
    - Explicar as configurações de build
5. Dicas e Truques:
    - Compartilhar atalhos de teclado úteis
    - Mostrar como personalizar o ambiente
    - Dar dicas de produtividade
    Essas configurações podem transformar sua experiência de desenvolvimento!
Algumas coisas legais que você pode fazer com esses arquivos de configuração:
1. Portabilidade:
    - Você pode compartilhar seu projeto com outros desenvolvedores
    - Eles terão exatamente o mesmo ambiente que você
    - Não precisam configurar nada manualmente
2. Personalização por Projeto:
    - Cada projeto pode ter suas próprias regras de formatação
    - Diferentes compiladores para diferentes necessidades
    - Configurações específicas de linting
3. Automação:
    - Atalhos de teclado personalizados
    - Tarefas automatizadas (build, clean, test)
    - Formatação automática do código
4. Consistência:
    - Mesmo estilo de código em todo o projeto
    - Mesmos padrões de compilação
    - Mesmo ambiente de desenvolvimento
Se você quiser explorar mais, pode:
    - Adicionar mais tasks específicas
    - Configurar diferentes perfis de compilação
    - Adicionar regras de linting personalizadas
    - Configurar atalhos de teclado específicos

## Makefile vs. tasks.json
Similaridades:
1. Ambos automatizam tarefas
2. Podem ser usados para compilar código
3. Permitem definir sequências de comandos
4. Podem ser reutilizados em diferentes projetos
Diferenças:
1. Escopo:
    - Makefile: Mais focado em compilação e build
    - tasks.json: Mais focado em integração com o IDE
2. Capacidades:
    - Makefile:
        - Mais poderoso para compilação
        - Melhor para dependências entre arquivos
        - Mais flexível para projetos complexos
        - Funciona independentemente do IDE
    - tasks.json:
        - Melhor integração com o IDE
        - Mais fácil para tarefas simples
        - Melhor para debugging
        - Mais amigável para iniciantes
3. Uso Ideal:
    - Makefile:
        - Ideal para código em produção
        - Necessário em ambientes HPC (High Performance Computing)
        - Compatível com clusters e supercomputadores
        - Permite controle fino sobre flags de otimização
        - Facilita a portabilidade entre diferentes sistemas
        - Essencial para compilação em batch jobs (tarefas enviadas para execução em fila no cluster)
    - tasks.json:
        - Focado no ambiente de desenvolvimento local
        - Otimizado para o fluxo de trabalho no IDE
        - Facilita o desenvolvimento iterativo
        - Bom para prototipagem e testes
        - Melhor para debugging e desenvolvimento
        - Integrado com ferramentas de desenvolvimento
    Em outras palavras, no contexto de computação científica:
    1. O código é desenvolvido localmente (usando tasks.json para facilitar)
    2. Depois é transferido para clusters (usando Makefile para produção). Onde o ambiente de produção geralmente não tem IDEs ou ferramentas de desenvolvimento
    Você poderia até ter:
        - Um Makefile para produção no cluster
        - Um Makefile diferente para desenvolvimento local
        - E o tasks.json para facilitar o desenvolvimento

## Integrando makefile e tasks.json
1. Makefile
    - Gerencia a compilação completa
    - Lida com dependências entre arquivos
    - Permite flags de compilação personalizadas
    - Facilita a limpeza e rebuild
2. Tasks.json:
    - Integra o Makefile com o IDE
    - Fornece atalhos para tarefas comuns
    - Permite execução em sequência (ex: build e run)
    - Mantém a interface amigável
Como usar:
1. Ctrl+Shift+B ou Cmd+Shift+B: Compila usando o Makefile
2. Ctrl+Shift+P ou Cmd+Shift+P e digite "Tasks: Run Task":
    - "Clean": Limpa arquivos gerados
    - "Run": Compila e executa o programa
Vantagens desta integração:
1. Mantém a complexidade do build no Makefile
2. Mantém a facilidade de uso no IDE
3. Permite escalar o projeto facilmente
4. Facilita a colaboração com outros desenvolvedores