def main():
    """
    Função principal que gerencia o fluxo do sistema bancário.
    """
    # Constantes
    LIMITE_SAQUES = 3
    
    # Variáveis de estado
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    # Menu de opções
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """

    # Loop principal do programa para interagir com o usuário
    while True:
        try:
            # Obtém a opção do menu do usuário
            opcao = int(input(menu))
            
            if opcao == 1:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
                
            elif opcao == 2:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
    
            elif opcao == 3:
                exibir_extrato(saldo, extrato=extrato)
    
            elif opcao == 4:
                print("Saindo do sistema. Obrigado por usar nosso serviço!")
                break
    
            else:
                print("Operação inválida, por favor, selecione uma opção válida.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número correspondente à opção desejada.")
        except EOFError:
            print("Erro: A entrada de dados foi encerrada inesperadamente.")
            break


def depositar(saldo, valor, extrato):
    """
    Função para realizar a operação de depósito.
    Recebe o saldo, valor e extrato como parâmetros e retorna o novo saldo e extrato.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para realizar a operação de saque.
    Recebe o saldo, valor, extrato, limite, número de saques e o limite de saques como parâmetros.
    Retorna o novo saldo, extrato e número de saques.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, *, extrato):
    """
    Função para exibir o extrato.
    Recebe o saldo e o extrato (como argumento posicional) e exibe o extrato.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


main()