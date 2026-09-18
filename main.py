import sistema
gerenciador = sistema.GerenciadorFinanceiro()

print("\n  SELECIONE UMA OPÇÃO:  \n ")
print("1 => Novo lançamento")
print("2 => Excluir lançamento")
print("3 => Verificar saldo")
print("4 => Verificar extrato")
print("5 => Limpar lançamentos")
print("6 => Encerrar\n")
opcao = sistema.ler_inteiro("Escolha uma opção: ")

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
            tipo = "receita"
        elif opcao_lancamento == 2: 
            tipo = "despesa"

        categoria = str(input("Categoria: "))
        descricao = str(input("Descrição: "))
        gerenciador.novo_lancamento(categoria, descricao, tipo)

    elif opcao == 2:
        gerenciador.listar_lancamentos()
        if len(gerenciador.lancamentos) != 0:
            id_informado = sistema.ler_inteiro("ID do lançamento a ser excluído: ")
            gerenciador.exclui_lancamento(id_informado)

    elif opcao == 3:
        saldo = gerenciador.mostrar_saldo()
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == 4:
        gerenciador.listar_lancamentos()

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
            gerenciador.limpa_lancamentos()


    else:
        print("Opção inválida")


    print("\n  SELECIONE UMA OPÇÃO:  \n ")
    print("1 => Novo lançamento")
    print("2 => Excluir lançamento")
    print("3 => Verificar saldo")
    print("4 => Verificar extrato")
    print("5 => Limpar lançamentos")
    print("6 => Encerrar\n")
    opcao = sistema.ler_inteiro("Escolha uma opção: ")