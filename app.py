import os
from flask import Flask, render_template, request, redirect, url_for, flash
import sistema

ARQUIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lancamentos.csv")
CATEGORIAS_SUGERIDAS = ["Salário", "Alimentação", "Moradia", "Transporte", "Saúde", "Lazer", "Educação", "Investimentos"]

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-de-desenvolvimento")
gerenciador = sistema.GerenciadorFinanceiro(ARQUIVO_CSV)


#formata valores no padrão brasileiro: 1234.5 -> 1.234,50
@app.template_filter("moeda")
def moeda(valor):
    return f"{abs(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


#disponibiliza as sugestões de categoria para o formulário de novo lançamento em todas as páginas
@app.context_processor
def categorias_para_formulario():
    categorias_usadas = {lancamento.categoria for lancamento in gerenciador.listar_lancamentos()}
    return {"categorias_sugeridas": sorted(set(CATEGORIAS_SUGERIDAS) | categorias_usadas)}


def destino_apos_acao():
    return redirect(url_for("extrato") if request.form.get("origem") == "extrato" else url_for("home"))


@app.route("/")
def home():
    lancamentos = gerenciador.listar_lancamentos()
    receitas = gerenciador.total_receitas()
    despesas = gerenciador.total_despesas()
    saldo = gerenciador.mostrar_saldo()
    despesas_lancadas = [lancamento for lancamento in lancamentos if lancamento.valor < 0]

    return render_template(
        "index.html",
        saldo=saldo,
        receitas=receitas,
        despesas=despesas,
        ultimos_lancamentos=list(reversed(lancamentos))[:5],
        total_lancamentos=len(lancamentos),
        categorias=gerenciador.despesas_por_categoria(),
        maior_despesa=min(despesas_lancadas, key=lambda lancamento: lancamento.valor, default=None),
        taxa_economia=(saldo / receitas * 100) if receitas > 0 else None,
    )


#opção 1 do menu: novo lançamento
@app.route("/lancamentos", methods=["POST"])
def novo_lancamento():
    tipo = request.form.get("tipo", "")
    categoria = request.form.get("categoria", "").strip()
    descricao = request.form.get("descricao", "").strip()

    try:
        valor = float(request.form.get("valor", "").replace(",", "."))
    except ValueError:
        valor = 0

    if tipo not in ("Receita", "Despesa"):
        flash("Selecione se o lançamento é uma receita ou uma despesa.", "erro")
    elif valor <= 0:
        flash("Informe um valor maior que zero.", "erro")
    elif not categoria or not descricao:
        flash("Preencha a categoria e a descrição.", "erro")
    else:
        if tipo == "Despesa":
            valor = -valor
        gerenciador.novo_lancamento(valor, categoria, descricao, tipo)
        flash(f"{tipo} de R$ {moeda(valor)} cadastrada com sucesso!", "sucesso")

    return redirect(url_for("home"))


#opção 2 do menu: excluir lançamento
@app.route("/lancamentos/excluir", methods=["POST"])
def excluir_lancamento():
    try:
        id_informado = int(request.form.get("id", ""))
    except ValueError:
        flash("Informe um ID válido.", "erro")
        return destino_apos_acao()

    quantidade_antes = len(gerenciador.lancamentos)
    mensagem = gerenciador.exclui_lancamento(id_informado)
    flash(mensagem, "sucesso" if len(gerenciador.lancamentos) < quantidade_antes else "erro")
    return destino_apos_acao()


#opção 3 do menu: verificar saldo
@app.route("/saldo")
def verificar_saldo():
    saldo = gerenciador.mostrar_saldo()
    sinal = "-" if saldo < 0 else ""
    flash(f"Saldo atual: {sinal}R$ {moeda(saldo)}", "info")
    return redirect(url_for("home") + "#resumo")


#opção 4 do menu: verificar extrato
@app.route("/extrato")
def extrato():
    return render_template(
        "extrato.html",
        lancamentos=gerenciador.listar_lancamentos(),
        saldo=gerenciador.mostrar_saldo(),
        receitas=gerenciador.total_receitas(),
        despesas=gerenciador.total_despesas(),
    )


#opção 5 do menu: limpar lançamentos (exige confirmação)
@app.route("/lancamentos/limpar", methods=["POST"])
def limpar_lancamentos():
    if request.form.get("confirmacao") != "sim":
        flash("Ação cancelada: a limpeza precisa ser confirmada.", "erro")
    else:
        quantidade_antes = len(gerenciador.lancamentos)
        mensagem = gerenciador.limpa_lancamentos()
        flash(mensagem, "sucesso" if quantidade_antes > 0 else "info")
    return destino_apos_acao()


if __name__ == "__main__":
    app.run(debug=True)
