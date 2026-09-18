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
    def __init__(self):
        self.lancamentos = []

    #adiciona receitas e despesas
    def novo_lancamento(self, categoria, descricao, tipo):
        _id = max((lancamento._id for lancamento in self.lancamentos), default=0) + 1
        data = datetime.now()
        if tipo == "receita":
            valor = ler_float("Digite o valor da receita: ")
            self.lancamentos.append(Lancamento(_id, data, valor, categoria, descricao, tipo))
            self.salva_dados()
        elif tipo == "despesa":
            valor = ler_float("Digite o valor da despesa: ") 
            self.lancamentos.append(Lancamento(_id, data, -valor, categoria, descricao, tipo))
            self.salva_dados()

    #lista histórico de lançamentos
    def listar_lancamentos(self):
        if len(self.lancamentos) == 0:
            print("Sem histórico de lançamentos.")
        else:
            for lancamento in self.lancamentos:
                print(lancamento) #"lancamento.__str__()"

    #mostra saldo atual
    def mostrar_saldo(self):
        saldo = sum([lancamento.valor for lancamento in self.lancamentos])
        return saldo

    def exclui_lancamento(self, id_informado):
        if len(self.lancamentos) == 0:
            print("Não há lançamentos a serem excluídos.")
        elif id_informado in [lancamento._id for lancamento in self.lancamentos]:
            for indice, lancamento in enumerate(self.lancamentos):
                if lancamento._id == id_informado:
                    self.lancamentos.pop(indice) 
                    break
            for novo_id, lancamento in enumerate(self.lancamentos, start=1):
                lancamento._id = novo_id
            self.salva_dados()
            print("Lançamento excluido com sucesso! Os ID's foram atualizados.")
        else:
            print("Lançamento não encontrado.")

    def limpa_lancamentos(self):
        if len(self.lancamentos) == 0:
            print("Não há lançamentos a serem excluídos.")
        else:
            self.lancamentos.clear()
            self.salva_dados()
            print("Lançamentos excluídos.")
        
    #salva dados em arquivo csv
    def salva_dados(self):
        campos = ["id", "data", "valor", "categoria", "descricao", "tipo"]
        with open("lancamentos.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
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
                valor = float(input(mensagem))
                return valor
            except ValueError:
                print("Entrada Inválida")


