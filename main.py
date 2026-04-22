opcao = -1
usuario_correto = "Tiago"
senha_correta = "123"
saldoDaConta = 1000
limiteUsuario = 500


while True:
    try:
        print("[1] - Acessar")
        print("[0] - Encerrar sistema")

        opcao = int(input("Escolha um opcao: "))
        if opcao == 1:
            print("Sistema foi iniciado")
        elif opcao == 0:
            print("Sistema encerrado")
            break
        else:
            print("Opcao invalida")
            continue
    except ValueError:
        print("Opcao invalida")
        continue

#TENTIVAS

    tentativas = 3
    acesso = False
        
    while tentativas > 0:
        usuario = str(input("Digite o nome de usuario: "))
        senha = input("Digite sua senha: ")
        

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso\n")
            acesso = True
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print("Usuario ou Senha invalida")
                print(f"\nRESTAM {tentativas} TENTATIVA(s)!\n")
            else:
                print("\nNumero de tentativas esgotado")
                print("Programa encerrado\n")
                exit()
                


    if acesso:
        while True:
            try:
                print("====- UNIVILLE Internet Banking -====\n")
                    #Menu
                    

                print(
                    '[1] - Consultar Saldo \n[2] - Realizar Saque \n[3] - Realizar depósito \n[4] - Consultar Limite \n[5] - Encerrar'
                )
                
                opcaoMenu = int(input('Escolha sua opção: '))

                    #Opção consultar saldo
                if opcaoMenu == 1:
                    print(f'\nSaldo: R${saldoDaConta:.2f}\n')
                    
                #Opção realizar saque
                elif opcaoMenu == 2:
                    print(f'Saldo Atual: R${saldoDaConta:.2f}\n')
                    valorSaque = int(input('Digite o valor do saque: '))
                    
                    if valorSaque > saldoDaConta:
                        print('Saldo insuficiente')
                    else:
                        saldoDaConta -= valorSaque
                        print(f'Saque Realizado!\nSaldo atual: R${saldoDaConta:.2f}\n')

                    #Opção realizar deposito
                elif opcaoMenu == 3:
                    print(f'Saldo Atual: R${saldoDaConta:.2f}\n')
                    valorDeposito = float(input('Digite o valor do deposito: '))
                    if valorDeposito <= 0:
                        print('Número inválido')
                        exit()
                    else:
                        saldoDaConta += valorDeposito
                        print(f'Deposito realizado! \nSaldo Atual: R${saldoDaConta:.2f}\n')
                  
                    #Opcao consultar limite
                      
                elif opcaoMenu == 4:
                    print(f'Limite atual: R${limiteUsuario:.2f}\n')
                    break
                
                #Encerrar
                        
                elif opcaoMenu == 5:
                    print("Sistema encerrado")
                    exit()           

                
            except ValueError:
                print("Digite apenas numeros")

            
                   