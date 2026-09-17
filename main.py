import sistema

print("\n  SELECIONE UMA OPÇÃO:  \n ")
print("1 => Novo lançamento")
print("2 => Excluir lançamento")
print("3 => Verificar saldo")
print("4 => Verificar extrato")
print("5 => Limpar lançamentos")
print("6 => Encerrar\n")
opcao = int(input("Escolha uma opção: "))

while (opcao != 6):
    if opcao == 1:
        print("\n1 => Cadastrar receita")
        print("2 => Cadastrar despesa\n")
        opcao_lancamento = int(input("Tipo de lançamento: "))

        while(opcao_lancamento not in [1,2]):
            print("\n1 => Cadastrar receita")
            print("2 => Cadastrar despesa\n")
            opcao_lancamento = int(input("Tipo de lançamento: "))
        if opcao_lancamento == 1:
            tipo = "receita"
        elif opcao_lancamento == 2: 
            tipo = "despesa"

        categoria = str(input("Categoria: "))
        descricao = str(input("Descrição: "))
        sistema.novo_lancamento(categoria, descricao, tipo, sistema.lancamentos)

    elif opcao == 2:
        sistema.listar_lancamentos(sistema.lancamentos)
        if len(sistema.lancamentos) != 0:
            id_informado = int(input("ID do lançamento a ser excluído: "))
            sistema.exclui_lancamento(id_informado, sistema.lancamentos)

    elif opcao == 3:
        sistema.mostrar_saldo(sistema.lancamentos)

    elif opcao == 4:
        sistema.listar_lancamentos(sistema.lancamentos)

    elif opcao == 5:
        print("Tem certeza que deseja prosseguir? Não será possível reverter essa ação.\n")
        print("1 => Sim, desejo prosseguir")
        print("2 => Não, cancelar ação\n")
        opcao_desejo = int(input("Digite uma opção: "))

        while(opcao_desejo not in [1,2]):
            print("Tem certeza que deseja prosseguir? Não será possível reverter essa ação.\n")
            print("1 => Sim, desejo prosseguir")
            print("2 => Não, cancelar ação\n")
            opcao_desejo = int(input("Digite uma opção: "))

        if opcao_desejo == 1: 
            sistema.limpa_lancamentos(sistema.lancamentos)


    else:
        print("Opção inválida")


    print("\n  SELECIONE UMA OPÇÃO:  \n ")
    print("1 => Novo lançamento")
    print("2 => Excluir lançamento")
    print("3 => Verificar saldo")
    print("4 => Verificar extrato")
    print("5 => Limpar lançamentos")
    print("6 => Encerrar\n")
    opcao = int(input("Escolha uma opção: "))