import os
import sistema

ARQUIVO_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lancamentos.csv")
gerenciador = sistema.GerenciadorFinanceiro(ARQUIVO_CSV)

def exibe_menu():
    print("\n  SELECIONE UMA OPÇÃO:  \n ")
    print("1 => Novo lançamento")
    print("2 => Excluir lançamento")
    print("3 => Verificar saldo")
    print("4 => Verificar extrato")
    print("5 => Limpar lançamentos")
    print("6 => Encerrar\n")
    return sistema.ler_inteiro("Escolha uma opção: ")

def ler_valor_positivo(mensagem):
    valor = sistema.ler_float(mensagem)
    while valor <= 0:
        print("O valor deve ser maior que zero.")
        valor = sistema.ler_float(mensagem)
    return valor

def exibe_extrato():
    historico_lancamentos = gerenciador.listar_lancamentos()
    if len(historico_lancamentos) == 0:
        print("Sem histórico de lançamentos.")
    for lancamento in historico_lancamentos:
        print(lancamento)

opcao = exibe_menu()

while (opcao != 6):
    if opcao == 1:
        print("\n1 => Cadastrar receita")
        print("2 => Cadastrar despesa\n")
        opcao_lancamento = sistema.ler_inteiro("Tipo de lançamento: ")

        while(opcao_lancamento not in [1,2]):
            print("\n1 => Cadastrar receita")
            print("2 => Cadastrar despesa\n")
            opcao_lancamento = sistema.ler_inteiro("Tipo de lançamento: ")
        if opcao_lancamento == 1:
            tipo = "Receita"
            valor = ler_valor_positivo("Digite o valor da receita: ")
        elif opcao_lancamento == 2:
            tipo = "Despesa"
            valor = -ler_valor_positivo("Digite o valor da despesa: ")

        categoria = str(input("Categoria: "))
        descricao = str(input("Descrição: "))
        gerenciador.novo_lancamento(valor, categoria, descricao, tipo)
        print("Lançamento cadastrado com sucesso!")

    elif opcao == 2:
        exibe_extrato()
        if len(gerenciador.lancamentos) != 0:
            id_informado = sistema.ler_inteiro("ID do lançamento a ser excluído: ")
            mensagem = gerenciador.exclui_lancamento(id_informado)
            print(mensagem)

    elif opcao == 3:
        saldo = gerenciador.mostrar_saldo()
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == 4:
        exibe_extrato()

    elif opcao == 5:
        print("Tem certeza que deseja prosseguir? Não será possível reverter essa ação.\n")
        print("1 => Sim, desejo prosseguir")
        print("2 => Não, cancelar ação\n")
        opcao_desejo = sistema.ler_inteiro("Digite uma opção: ")

        while(opcao_desejo not in [1,2]):
            print("Tem certeza que deseja prosseguir? Não será possível reverter essa ação.\n")
            print("1 => Sim, desejo prosseguir")
            print("2 => Não, cancelar ação\n")
            opcao_desejo = sistema.ler_inteiro("Digite uma opção: ")

        if opcao_desejo == 1:
            mensagem = gerenciador.limpa_lancamentos()
            print(mensagem)

    else:
        print("Opção inválida")

    opcao = exibe_menu()
