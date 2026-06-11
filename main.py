from rich import print
import time

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
condicaoDeExecucao = True
while condicaoDeExecucao:
    try:
        print("Bem vindo ao banco [bold green]UNIVILLE[/bold green]")

        print("[1] - Fazer Log In")
        print("[2] - Criar Conta")
        print("[3] - Painel de Administrador")
        print("[0] - Encerrar sistema")

        opcao = int(input("Escolha um opcao: "))
        
        if opcao == 1:
            # Login de conta
            tentativas = 3
            acesso = False
            

            while tentativas > 0 and acesso != True:
                usuario = input("Digite o nome de usuario: ")
                senha = input("Digite sua senha: ")

                for c in usuarios:
                    if c["Nome"] == usuario and c["Senha"] == senha:
                        acesso = True
                        print("Login realizado com sucesso\n")
                        condicaoDeExecucao = False
                        break
                else:
                    tentativas -= 1
                    if tentativas > 0:
                        print("\nUsuario ou Senha invalida")
                        print(f"RESTAM {tentativas} TENTATIVA(s)!\n")
                    else:
                        print("\nNumero de tentativas esgotado")
                        print("Programa encerrado\n")
                        exit()
            
        elif opcao == 2:
            #Criação de conta
            print("Painel de criação de conta")
            nomeCriado = input('Digite o seu usuário de acesso: ')
            senhaCriada = input('Digite sua senha: ')
            senhaConfirmar = input('Confirme sua senha: ')

            while senhaCriada != senhaConfirmar:
                print('As senha digitas devem ser iguais, insira novamente:')
                senhaCriada = input('Digite sua senha: ')
                senhaConfirmar = input('Confirme sua senha: ')
        
            usuarios.insert(len(usuarios)-1, {"Nome": nomeCriado, "Senha": senhaCriada, "Saldo": 0, "Limite": 0, "Admin": 0})
            continue
            
        elif opcao == 3:
            # Painel Admin
            usuarioAdmin = input("Digite o nome de usuário de admin: ")
            senha = input("Digite sua senha: ")

            resultado = 0
            for c in usuarios_admin:
                if usuarioAdmin == c["Nome"] and senha == c["Senha"]:
                    resultado = 1
                    break
                    
            condicao = True
            if resultado == 1:
                while condicao:
                    print('Painel [bold yellow]Admin[/bold yellow] - Seja bem vindo')
                    print("[1] - Consultar Usuários")
                    print("[2] - Atualizar dados de Clientes")
                    print("[3] - Voltar para a página principal")
                    print("[0] - Sair do sistema")
                    opcao = int(input("Escolha uma opcão: "))

                    if opcao == 1:
                        print('Quantidade de usuários:', len(usuarios))
                        for c in usuarios:
                            print(f'Nome: {c["Nome"]}\nSenha: {c["Senha"]}, Saldo: {c["Saldo"]}, Limite: {c["Limite"]}\n')
                            break
                    
                    elif opcao == 2:
                        if len(usuarios) == 0:
                            print("[red]Nenhum usuário cadastrado no sistema[/red]")
                            continue
                        usuarioDesejado = input('Digite o usuário que deseja alterar: ')
                        indice = 0
                        for c in usuarios:
                            if c["Nome"] == usuarioDesejado:
                                print('[blue]Usuário encontrado![/blue]')
                                print("[1] - Nome")
                                print("[2] - Senha")
                                print("[3] - Saldo")
                                print("[4] - Limite")
                                
                                opcaoDeAlteração = int(input('Digite a opção: '))
                                if opcaoDeAlteração == 1:
                                    nomeNovo = input('Digite o nome novo: ')
                                    usuarios[indice]["Nome"] = nomeNovo
                                    print('[green]Nome alterado![/green]')
                                    time.sleep(1)
                                    break
                                elif opcaoDeAlteração == 2:
                                    senhaNovo = input('Digite a senha nova: ')
                                    usuarios[indice]["Senha"] = senhaNovo
                                    print('[green]Senha alterada![/green]')
                                    time.sleep(1)
                                    break
                                elif opcaoDeAlteração == 3:
                                    saldoNovo = input('Digite o saldo novo: ')
                                    usuarios[indice]["Saldo"] = saldoNovo
                                    print('[green]Saldo alterado![/green]')
                                    time.sleep(1)
                                    break
                                elif opcaoDeAlteração == 4:
                                    LimiteNovo = input('Digite o novo Limite: ')
                                    usuarios[indice]["Limite"] = LimiteNovo
                                    print('[green]Limite alterado![/green]')
                                    time.sleep(1)
                                    break
                                else:
                                    print("[red]Opção inválida, sistema retornando ao painel admin[/red]")
                                    break

                            indice += 1
                        else:
                            print("[red]Usuário inválido[/red]")
                            continue
                    elif opcao == 3:
                        condicao = False
                        continue
                    elif opcao == 0:
                        print("Obrigado por usar o banco [bold green]UNIVILLE[/bold green]!")
                        exit()
                    else:
                        print('[red]Opção inválida[/red]')
                        break
            else:
                print('Usuário inválido para o painel de administrados, contate o suporte para mais informações')
                continue        
        elif opcao == 0:
            print("Sistema encerrado")
            break
        else:
            print("Opcao invalida")
            continue
    except ValueError:
        print("[bold red]Erro![/bold red][red], não utilize letras em opções númericas\nRetornando ao painel inicial[/red]")
        continue
                
    # Logo após a logar, acesso do usuário
if acesso:
    while True:
        try:
            #Armazenamento das informações do usuário no estado atual para facilitar consulta de limite ou de saldo
            indice = 0
            for c in usuarios:
                if usuario == c["Nome"]:
                    usuarioAtual = c
                    break
                indice += 1

            print("\n==== [bold green]UNIVILLE[/bold green] [green]Internet Banking[/green] ====\n")
                #Menu

            print('[1] - Consultar Saldo \n[2] - Realizar Saque \n[3] - Realizar depósito \n[4] - Consultar Limite \n[5] - Encerrar')
            
            opcaoMenu = int(input('Escolha sua opção: '))

                
            if opcaoMenu == 1:
                #Opção consultar saldo
                print(f'Saldo atual: {usuarioAtual['Saldo']}')
                time.sleep(2)
                continue
            
            elif opcaoMenu == 2:
                #Opção realizar saque
                print(f'Saldo atual: {usuarioAtual['Saldo']}')
                valorSaque = float(input('Digite o valor do saque: '))
                
                if valorSaque > usuarioAtual['Saldo']:
                    print('[red]Saldo insuficiente[/red]')
                else:
                    usuarios[indice]["Saldo"] = usuarioAtual["Saldo"] - valorSaque
                    print(f'[green]Saque Realizado![/green]\nSaldo atual: R${usuarios[indice]["Saldo"]}')
                    time.sleep(2)
                    continue
                
            elif opcaoMenu == 3:
                #Opção realizar deposito
                print(f'Saldo atual: {usuarioAtual['Saldo']}')
                valorDeposito = float(input('Digite o valor do deposito: '))

                if valorDeposito <= 0:
                    print('Número inválido')
                    time.sleep(1)
                    continue
                else:
                    usuarios[indice]["Saldo"] += valorDeposito
                    print(f'[green]Deposito realizado![/green] \nSaldo Atual: R$ {usuarios[indice]["Saldo"]}')
                    time.sleep(2)
                    continue
                    
            elif opcaoMenu == 4:
                #Opcao consultar limite
                print(f'Limite atual: {usuarioAtual['Limite']}')
                time.sleep(2)
                continue
                    
            elif opcaoMenu == 5:
                print("[red]Sistema encerrado[/red]")
                exit()           
        except ValueError:
            print("[bold red]Erro![/bold red][red], não utilize letras em opções númericas")