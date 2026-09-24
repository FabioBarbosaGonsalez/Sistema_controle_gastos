from datetime import datetime
import csv

class Lancamento:
    def __init__(self,_id, data, valor, categoria, descricao, tipo):
        self._id = _id
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao
        self.tipo = tipo

    def __str__(self):
        return (
            f"ID: {self._id}\n"
            f"Data: {self.data.strftime('%d/%m/%Y')}\n"
            f"Tipo: {self.tipo.capitalize()}\n"
            f"Categoria: {self.categoria}\n"
            f"Descrição: {self.descricao}\n"
            f"Valor: R$ {self.valor:.2f}\n"
        )

class GerenciadorFinanceiro:
    def __init__(self, arquivo="lancamentos.csv"):
        self.arquivo = arquivo
        self.lancamentos = []
        self.carrega_dados()

    #adiciona receitas e despesas
    def novo_lancamento(self, valor, categoria, descricao, tipo):
        _id = max((lancamento._id for lancamento in self.lancamentos), default=0) + 1
        data = datetime.now()
        self.lancamentos.append(Lancamento(_id, data, valor, categoria, descricao, tipo))
        self.salva_dados()
        
    #lista histórico de lançamentos
    def listar_lancamentos(self):
        return self.lancamentos

    #mostra saldo atual
    def mostrar_saldo(self):
        saldo = sum([lancamento.valor for lancamento in self.lancamentos])
        return saldo

    #soma de todas as receitas
    def total_receitas(self):
        return sum(lancamento.valor for lancamento in self.lancamentos if lancamento.valor > 0)

    #soma de todas as despesas (valor positivo)
    def total_despesas(self):
        return -sum(lancamento.valor for lancamento in self.lancamentos if lancamento.valor < 0)

    #total gasto em cada categoria, da maior para a menor
    def despesas_por_categoria(self):
        categorias = {}
        for lancamento in self.lancamentos:
            if lancamento.valor < 0:
                categorias[lancamento.categoria] = categorias.get(lancamento.categoria, 0) - lancamento.valor
        return sorted(categorias.items(), key=lambda item: item[1], reverse=True)

    #exclui um lançamento
    def exclui_lancamento(self, id_informado):
        if len(self.lancamentos) == 0:
            return "Não há lançamentos a serem excluídos."
        elif id_informado in [lancamento._id for lancamento in self.lancamentos]:
            for indice, lancamento in enumerate(self.lancamentos):
                if lancamento._id == id_informado:
                    self.lancamentos.pop(indice) 
                    break
            for novo_id, lancamento in enumerate(self.lancamentos, start=1):
                lancamento._id = novo_id
            self.salva_dados()
            return "Lançamento excluido com sucesso! Os ID's foram atualizados."
        else:
            return "Lançamento não encontrado."

    #exclui todos os lançamentos
    def limpa_lancamentos(self):
        if len(self.lancamentos) == 0:
            return "Não há lançamentos a serem excluídos."
        else:
            self.lancamentos.clear()
            self.salva_dados()
            return "Lançamentos excluídos."

    #carrega dados salvos anteriormente no csv, se existir
    def carrega_dados(self):
        try:
            with open(self.arquivo, "r", newline="", encoding="utf-8-sig") as arquivo:
                leitor = csv.DictReader(arquivo, delimiter=";")
                for linha in leitor:
                    self.lancamentos.append(
                        Lancamento(
                            int(linha["id"]),
                            datetime.strptime(linha["data"], "%Y-%m-%d %H:%M:%S"),
                            float(linha["valor"]),
                            linha["categoria"],
                            linha["descricao"],
                            linha["tipo"]
                        )
                    )
        except FileNotFoundError:
            pass

    #salva dados em arquivo csv
    def salva_dados(self):
        campos = ["id", "data", "valor", "categoria", "descricao", "tipo"]
        with open(self.arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(campos)
            for lancamento in self.lancamentos:
                escritor.writerow([
                    lancamento._id,
                    lancamento.data.strftime("%Y-%m-%d %H:%M:%S"),
                    lancamento.valor,
                    lancamento.categoria,
                    lancamento.descricao,
                    lancamento.tipo
                ])

#tratamentos de erros
def ler_inteiro(mensagem):
        while True:
            try:
                opcao = int(input(mensagem))
                return opcao
            except ValueError:
                print("Entrada Inválida")

def ler_float(mensagem):
        while True:
            try:
                valor = float(input(mensagem).replace(",", "."))
                return valor
            except ValueError:
                print("Entrada Inválida")