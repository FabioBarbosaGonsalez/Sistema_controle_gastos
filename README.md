# Controle Financeiro (CLI)

Sistema para controle financeiro pessoal, feito em Python. Permite registrar receitas e despesas, consultar saldo, ver o extrato completo e manter um histórico salvo em CSV.

Este projeto foi construído como parte do meu portfólio, com foco em praticar lógica de programação, estruturação de código em módulos e manipulação de arquivos.

## Funcionalidades

- Cadastrar um novo lançamento (receita ou despesa), com categoria e descrição
- Excluir um lançamento pelo ID
- Verificar o saldo atual
- Verificar o extrato completo de lançamentos
- Limpar todos os lançamentos (com confirmação antes de executar)
- Salvamento automático dos dados em um arquivo CSV

## Como executar

Clone o repositório e rode o arquivo principal:

```bash
git clone https://github.com/FabioBarbosaGonsalez/Sistema_controle_gastos.git
cd Sistema_controle_gastos
python main.py
```

O programa vai abrir um menu interativo no terminal com as opções disponíveis.

## Estrutura do projeto

```
.
├── main.py       # Menu principal e interação com o usuário
├── sistema.py    # Lógica do sistema: classe Lancamento e funções de controle
└── lancamentos.csv  # Arquivo gerado automaticamente com o histórico de lançamentos
```

## Tecnologias utilizadas

- Python 3
- Módulo `csv` da biblioteca padrão
- Módulo `datetime` da biblioteca padrão
- Módulo `pytest` para testes automatizados

## Próximos passos

Algumas melhorias que pretendo implementar:

- Geração de gráficos simples com os dados financeiros
- Possível criação de uma interface web 

## Sobre

Projeto desenvolvido como parte dos meus estudos em Ciência de Dados e Inteligência Artificial, com o objetivo de reforçar fundamentos de programação e construir um portfólio sólido.
