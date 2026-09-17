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

lancamentos = [] #histórico de lançamentos

#adiciona receitas e despesas
def novo_lancamento(categoria, descricao, tipo, lancamentos):
    _id = max((lancamento._id for lancamento in lancamentos), default=0) + 1
    data = datetime.now()
    if tipo == "receita":
        valor = float(input("Digite o valor da receita: "))
        lancamentos.append(Lancamento(_id, data, valor, categoria, descricao, tipo))
        salva_dados(lancamentos)
    elif tipo == "despesa":
        valor = float(input("Digite o valor da despesa: ")) 
        lancamentos.append(Lancamento(_id, data, -valor, categoria, descricao, tipo))
        salva_dados(lancamentos)

#lista histórico de lançamentos
def listar_lancamentos(lancamentos):
    if len(lancamentos) == 0:
        print("Sem histórico de lançamentos.")
    else:
        for lancamento in lancamentos:
            print(lancamento) #"lancamento.__str__()"

#mostra saldo atual
def mostrar_saldo(lancamentos):
    saldo = sum([lancamento.valor for lancamento in lancamentos])
    print(f"Saldo: R$ {saldo:.2f}\n")

def exclui_lancamento(id_informado, lancamentos):
    if len(lancamentos) == 0:
        print("Não há lançamentos a serem excluídos.")
    elif id_informado in [lancamento._id for lancamento in lancamentos]:
        for indice, lancamento in enumerate(lancamentos):
            if lancamento._id == id_informado:
                lancamentos.pop(indice) 
                break
        for novo_id, lancamento in enumerate(lancamentos, start=1):
            lancamento._id = novo_id
        salva_dados(lancamentos)
        print("Lançamento excluido com sucesso! Os ID's foram atualizados.")
    else:
        print("Lançamento não encontrado.")

def limpa_lancamentos(lancamentos):
    if len(lancamentos) == 0:
        print("Não há lançamentos a serem excluídos.")
    else:
        lancamentos.clear()
        salva_dados(lancamentos)
        print("Lançamentos excluídos.")
    
#salva dados em arquivo csv
def salva_dados(lancamentos):
    campos = ["id", "data", "valor", "categoria", "descricao", "tipo"]
    with open("lancamentos.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(campos)
        for lancamento in lancamentos:
            escritor.writerow([
                lancamento._id,
                lancamento.data.strftime("%Y-%m-%d %H:%M:%S"),
                lancamento.valor,
                lancamento.categoria,
                lancamento.descricao,
                lancamento.tipo
            ])

#Implementações Futuras:
#Criar gráficos
#Interface HTML e CSS