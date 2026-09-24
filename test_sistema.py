import pytest
import sistema
from datetime import datetime


@pytest.fixture(autouse=True)
def isola_csv(tmp_path, monkeypatch):
    # Evita que os testes leiam/escrevam no lancamentos.csv real do projeto
    monkeypatch.chdir(tmp_path)


def teste_saldo():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
            sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "Receita")
        )
    
    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "Despesa")
        )

    assert gerenciador.mostrar_saldo() == 50

def teste_novo_lancamento_receita():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.novo_lancamento(100, "Salário", "Salário do mês", "Receita")

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0].valor == 100

def teste_novo_lancamento_despesa():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.novo_lancamento(-50, "Alimentação", "Almoço", "Despesa")

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0].valor == -50

def teste_exclui_lancamento():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
        sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "Receita")
    )

    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "Despesa")
    )

    gerenciador.lancamentos.append(
        sistema.Lancamento(3, datetime.now(), -30, "Transporte", "Uber", "Despesa")
    )

    gerenciador.exclui_lancamento(2)

    assert len(gerenciador.lancamentos) == 2
    assert gerenciador.lancamentos[0]._id == 1
    assert gerenciador.lancamentos[1]._id == 2

def teste_exclui_lancamento_inexistente():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
        sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "Receita")
    )

    gerenciador.exclui_lancamento(999)

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0]._id == 1

def teste_ler_float_valor_invalido(monkeypatch):

    entradas = iter(["abc", "100"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(entradas)
    )

    valor = sistema.ler_float("Digite o valor: ")

    assert valor == 100

def teste_cricao_ids():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.novo_lancamento(100, "Salário", "Primeiro", "Receita")
    gerenciador.novo_lancamento(200, "Salário", "Segundo", "Receita")

    assert gerenciador.lancamentos[0]._id == 1
    assert gerenciador.lancamentos[1]._id == 2

def teste_limpar_lancamentos():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
            sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "Receita")
        )
    
    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "Despesa")
        )

    mensagem = gerenciador.limpa_lancamentos()

    assert len(gerenciador.lancamentos) == 0
    assert mensagem == "Lançamentos excluídos."

def teste_persistencia_carrega_dados():

    gerenciador1 = sistema.GerenciadorFinanceiro()
    gerenciador1.novo_lancamento(150, "Salário", "Salário do mês", "Receita")

    gerenciador2 = sistema.GerenciadorFinanceiro()

    assert len(gerenciador2.lancamentos) == 1
    assert gerenciador2.lancamentos[0].valor == 150
    assert gerenciador2.lancamentos[0].categoria == "Salário"

def teste_totais_receitas_e_despesas():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.novo_lancamento(1000, "Salário", "Salário", "Receita")
    gerenciador.novo_lancamento(-200, "Alimentação", "Mercado", "Despesa")
    gerenciador.novo_lancamento(-50, "Transporte", "Uber", "Despesa")

    assert gerenciador.total_receitas() == 1000
    assert gerenciador.total_despesas() == 250
    assert gerenciador.mostrar_saldo() == 750

def teste_despesas_por_categoria():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.novo_lancamento(1000, "Salário", "Salário", "Receita")
    gerenciador.novo_lancamento(-30, "Transporte", "Uber", "Despesa")
    gerenciador.novo_lancamento(-200, "Alimentação", "Mercado", "Despesa")
    gerenciador.novo_lancamento(-50, "Alimentação", "Almoço", "Despesa")

    assert gerenciador.despesas_por_categoria() == [("Alimentação", 250), ("Transporte", 30)]

def teste_ler_float_aceita_virgula(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda mensagem: "10,50")

    assert sistema.ler_float("Digite o valor: ") == 10.5
