import sistema
from datetime import datetime

def teste_saldo():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
            sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "receita")
        )
    
    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "despesa")
        )

    assert gerenciador.mostrar_saldo() == 50

def teste_novo_lancamento_receita(monkeypatch):
    gerenciador = sistema.GerenciadorFinanceiro()

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "100"
    )

    gerenciador.novo_lancamento("Salário", "Salário do mês", "receita")

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0].valor == 100

def teste_novo_lancamento_despesa(monkeypatch):
    gerenciador = sistema.GerenciadorFinanceiro()

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "50"
    )

    gerenciador.novo_lancamento("Alimentação", "Almoço","despesa")

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0].valor == -50

def teste_exclui_lancamento():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
        sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "receita")
    )

    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "despesa")
    )

    gerenciador.lancamentos.append(
        sistema.Lancamento(3, datetime.now(), -30, "Transporte", "Uber", "despesa")
    )

    gerenciador.exclui_lancamento(2)

    assert len(gerenciador.lancamentos) == 2
    assert gerenciador.lancamentos[0]._id == 1
    assert gerenciador.lancamentos[1]._id == 2

def teste_exclui_lancamento_inexistente():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
        sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "receita")
    )

    gerenciador.exclui_lancamento(999)

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0]._id == 1

def teste_novo_lancamento_valor_invalido(monkeypatch):
    gerenciador = sistema.GerenciadorFinanceiro()

    entradas = iter(["abc", "100"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(entradas)
    )

    gerenciador.novo_lancamento("Salário", "Salário do mês", "receita")

    assert len(gerenciador.lancamentos) == 1
    assert gerenciador.lancamentos[0].valor == 100

def teste_cricao_ids(monkeypatch):
    gerenciador = sistema.GerenciadorFinanceiro()

    entradas = iter(["100", "200"])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(entradas)
    )

    gerenciador.novo_lancamento("Salário", "Primeiro", "receita")

    gerenciador.novo_lancamento("Salário", "Segundo", "receita")

    assert gerenciador.lancamentos[0]._id == 1
    assert gerenciador.lancamentos[1]._id == 2

def teste_limpar_lancamentos():
    gerenciador = sistema.GerenciadorFinanceiro()

    gerenciador.lancamentos.append(
            sistema.Lancamento(1, datetime.now(), 100, "Salário", "Salário", "receita")
        )
    
    gerenciador.lancamentos.append(
        sistema.Lancamento(2, datetime.now(), -50, "Alimentação", "Almoço", "despesa")
        )

    gerenciador.limpa_lancamentos()

    assert len(gerenciador.lancamentos) == 0
