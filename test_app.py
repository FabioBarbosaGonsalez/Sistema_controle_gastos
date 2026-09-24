import pytest
import app as aplicacao
import sistema


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    # Usa um CSV temporário para não alterar os dados reais
    gerenciador = sistema.GerenciadorFinanceiro(str(tmp_path / "lancamentos.csv"))
    monkeypatch.setattr(aplicacao, "gerenciador", gerenciador)
    aplicacao.app.config["TESTING"] = True
    with aplicacao.app.test_client() as cliente:
        yield cliente, gerenciador


def teste_home_exibe_saldo_receitas_e_despesas(cliente):
    cliente, gerenciador = cliente
    gerenciador.novo_lancamento(1500, "Salário", "Salário", "Receita")
    gerenciador.novo_lancamento(-250.5, "Alimentação", "Mercado", "Despesa")

    html = cliente.get("/").get_data(as_text=True)

    assert "R$ 1.249,50" in html
    assert "R$ 1.500,00" in html
    assert "R$ 250,50" in html

def teste_novo_lancamento_despesa_fica_negativa(cliente):
    cliente, gerenciador = cliente

    resposta = cliente.post("/lancamentos", data={"tipo": "Despesa", "valor": "40,90", "categoria": "Lazer", "descricao": "Cinema"})

    assert resposta.status_code == 302
    assert gerenciador.lancamentos[0].valor == -40.9
    assert gerenciador.lancamentos[0].tipo == "Despesa"

def teste_novo_lancamento_rejeita_valor_invalido(cliente):
    cliente, gerenciador = cliente

    cliente.post("/lancamentos", data={"tipo": "Receita", "valor": "-10", "categoria": "Salário", "descricao": "Teste"})
    cliente.post("/lancamentos", data={"tipo": "Receita", "valor": "abc", "categoria": "Salário", "descricao": "Teste"})

    assert len(gerenciador.lancamentos) == 0

def teste_excluir_lancamento(cliente):
    cliente, gerenciador = cliente
    gerenciador.novo_lancamento(100, "Salário", "Salário", "Receita")

    cliente.post("/lancamentos/excluir", data={"id": "1"})

    assert len(gerenciador.lancamentos) == 0

def teste_limpar_exige_confirmacao(cliente):
    cliente, gerenciador = cliente
    gerenciador.novo_lancamento(100, "Salário", "Salário", "Receita")

    cliente.post("/lancamentos/limpar", data={})
    assert len(gerenciador.lancamentos) == 1

    cliente.post("/lancamentos/limpar", data={"confirmacao": "sim"})
    assert len(gerenciador.lancamentos) == 0

def teste_extrato_e_saldo(cliente):
    cliente, gerenciador = cliente
    gerenciador.novo_lancamento(100, "Salário", "Pagamento", "Receita")

    assert "Pagamento" in cliente.get("/extrato").get_data(as_text=True)
    resposta = cliente.get("/saldo", follow_redirects=True)
    assert "Saldo atual: R$ 100,00" in resposta.get_data(as_text=True)
