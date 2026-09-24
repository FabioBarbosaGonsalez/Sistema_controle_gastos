# Controle Financeiro (CLI + Web)

Sistema para controle financeiro pessoal, feito em Python. Permite registrar receitas e despesas, consultar saldo, ver o extrato completo e manter um histórico salvo em CSV.

Este projeto foi construído como parte do meu portfólio, com foco em praticar lógica de programação, estruturação de código em módulos e manipulação de arquivos.

## Funcionalidades

- Cadastrar um novo lançamento (receita ou despesa), com categoria e descrição
- Excluir um lançamento pelo ID
- Verificar o saldo atual
- Verificar o extrato completo de lançamentos
- Limpar todos os lançamentos (com confirmação antes de executar)
- Salvamento automático dos dados em um arquivo CSV
- Interface web (Flask) com resumo de saldo, receitas e despesas, indicadores, gastos por categoria e extrato

## Como executar

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/FabioBarbosaGonsalez/Sistema_controle_gastos.git
cd Sistema_controle_gastos
pip install -r requirements.txt
```

### Versão terminal

```bash
python main.py
```

O programa vai abrir um menu interativo no terminal com as opções disponíveis.

### Versão web

```bash
python app.py
```

Depois acesse http://127.0.0.1:5000 no navegador. A interface web e o terminal compartilham o mesmo arquivo `lancamentos.csv`.

### Testes

```bash
python -m pytest
```

## Estrutura do projeto

```
.
├── main.py              # Menu principal e interação com o usuário (terminal)
├── app.py               # Servidor web Flask: rotas que chamam as funções do sistema
├── sistema.py           # Lógica do sistema: classes Lancamento e GerenciadorFinanceiro
├── templates/           # Páginas HTML (Jinja2): resumo e extrato
├── static/              # CSS (mobile first) e JavaScript dos modais
├── test_sistema.py      # Testes da lógica do sistema
├── test_app.py          # Testes das rotas web
├── requirements.txt     # Dependências do projeto
└── lancamentos.csv      # Arquivo gerado automaticamente com o histórico de lançamentos
```

## Tecnologias utilizadas

- Python 
- Módulo `csv` da biblioteca padrão
- Módulo `datetime` da biblioteca padrão
- Flask (interface web) com templates Jinja2
- HTML, CSS e JavaScript
- Módulo `pytest` para testes automatizados

## Próximos passos

Algumas melhorias que pretendo implementar:

- Geração de gráficos simples com os dados financeiros
- Filtros do extrato por período e categoria

## Sobre

Projeto desenvolvido como parte dos meus estudos em Ciência de Dados e Inteligência Artificial, com o objetivo de reforçar fundamentos de programação e construir um portfólio sólido.
