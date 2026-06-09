from rich import print

opcao = -1
saldoDaConta = 1000
limiteUsuario = 500



############ ADMIN
# Seleciona se é usuario normal ou Administrador
# Admin coloca suas credenciais
# Acessa um menu diferente de um usuário normal
# Menu administrador deve consultar e atualizar os dados de todos os clientes do banco
# Loop até ele sinalizar que deseja sair do programa

############ USUARIOS
# Modificar o sistema de arquivamentos de usuarios de forma que uma pessoa possa ter suas informações dentro de um array
# Admin deve poder acessar esse array depois para mudar ou consultar informações
# Array usuario deve conter: usuário, senha, saldo, limite

usuarios = []
usuarios_admin = [{"Nome": "Admin", "Senha": "123A"}]
while True:
    try:
        print("bem vindo ao banco [bold green]UNIVILLE[/bold green]")

        print("[1] - Fazer Log In")
        print("[2] - Criar Conta")
        print("[3] - Painel de Administrador")
        print("[0] - Encerrar sistema")

        opcao = int(input("Escolha um opcao: "))

        #Criação de conta
        if opcao == 2:
            print("Painel de criação de conta")
            nomeCriado = input('Digite o seu usuário de acesso: ')
            senhaCriada = input('Digite sua senha')
            senhaConfirmar = input('Confirme sua senha')

            while senhaCriada != senhaConfirmar:
                print('As senha digitas devem ser iguais, insira novamente:')
                senhaCriada = input('Digite sua senha: ')
                senhaConfirmar = input('Confirme sua senha: ')
        
            usuarios.insert(len(usuarios)-1, {"Nome": nomeCriado, "Senha": senhaCriada, "Saldo": 0, "Limite": 0, "Admin": 0})
            continue


        if opcao == 3:
            usuarioAdmin = input("Digite o nome de usuario de admin: ")
            senha = input("Digite sua senha: ")

            resultado = 0
            for c in usuarios_admin:
                if usuarioAdmin == c["Nome"] and senha == c["Senha"]:
                    resultado = 1
                    break
    
            if resultado == 1:
                print('Painel Admin - Seja bem vindo')
                print("[1] - Consultar Usuários")
                print("[2] - Atualizar dados de Clientes")
                opcao = int(input("Escolha um opcao: "))

                if opcao == 1:
                    print('Quantidade de usuários:', len(usuarios))
                    for c in usuarios:
                        print(f'Nome: {c["Nome"]}\nSenha: {c["Senha"]} Saldo: {c["Saldo"]} Limite: {c["Limite"]}\n')
                
                #Atualizar > perguntar o nome do cliente > Verificar se o cliente ta dentro da array > Se estiver,
                # perguntar o que deseja mudar > Input com a nova informação > Inserir Usuário Atualizado no mesmo indice
                # if opcao == 2:
                #     print("Atualizar usuarios")
                #     for c in usuarios:
                #         pesquisaUsuario ==
                    
            else:
                print('Usuário inválido para o painel de administrados, contate o suporte para mais informações')
                continue


            
                    

                    

            

        elif opcao == 1:
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