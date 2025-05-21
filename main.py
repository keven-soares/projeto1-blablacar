usuarios = {'kevensoares@gmail.com': ['joelderson keven soares da silva','keven123',['3', 'motorista legal']],
            'jubiscleudo@gmail.com': ['jubiscleudo jeberson santos', 'juju123',[]]}
caronas = {'kevensoares@gmail.com': ['conceição', 'cajazeiras', '17/05/2025', '22 horas', 4, '25', ['xuxubeleza@.com', '17/05/2025',]],
           'jubiscleudo@gmail.com': ['cajazeiras', 'pombal', '22/05/2025', '13 horas', 10, '20', []]}

op = 99
while op != 0:
    print('\n========= MENU ========')
    print('1- Cadastre-se')
    print('2- login')
    print('0- sair do programa')
    op = int(input('digite a opcao desejada: '))

    if op == 1:
        print('----------- CADASTRO ------------')
        nome_completo = input('digite seu nome completo: ')
        email = input('digite seu melhor email: ')
        while '@''.com' not in email:
            email = input('digite um email válido: ')
        senha = input('digite sua senha: ')
        usuarios[email] = [nome_completo, senha]
        print('usuário cadastrado com sucesso!')

    elif op == 2:
        print('-------- FAÇA SEU LOGIN ----------')
        email_login = input('digite seu email: ')
        senha_login = input('digite sua senha: ')
        login_valido = False
        for usuario in usuarios:
            if email_login in usuarios and usuarios[email_login][1] == senha_login:
                login_valido = True
                break

        if not login_valido:
            print('email ou senha invalidos')
        else:
            print(f'\nBem-vindo! Login realizado com sucesso!')
            op = 99
            while op != 0:
                print('\n============ MENU =============')
                print('1- Cadastro de carona')
                print('2- Listar todas as caronas')
                print('3- Buscar carona por origem e destino')
                print('4- Reservar vaga em carona')
                print('5- Cancelar reserva')
                print('6- Remover carona')
                print('7- Mostrar detalhes da carona')
                print('8- Caronas que você está cadastrado')
                print('9- função extra')
                print('10- LOGOUT')
                op = int(input('\ndigite a opcao desejada: '))

                if op == 1:
                    print('\n-----voce é o motorista da viagem, atualize as opções abaixo------')
                    origem = input('qual o local de origem da sua carona: ')
                    destino = input('qual o local de destino da sua carona: ')
                    data = input('digite a data de saida no formato dd/mm/aa: ')
                    horario = input('qual o horário de partida: ')
                    qtde_vaga = input('vagas disponíveis: ')
                    valor_vaga = float(input('qual o valor da viajem(por vaga): '))
                    print('\n viagem confirmada')
                    caronas[email_login] = [origem, destino, data, horario, qtde_vaga, valor_vaga, []]
                    print('-' * 50)
                elif op == 2:
                    print('\n--------- CARONAS DISPONÍVEIS --------')
                    for email in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email]
                        if int(vagas) > 0:
                            print(f'\nMotorista: {usuarios[email][0]}')
                            print(f'saindo De {origem} para {destino}')
                            print(f'Dia: {data} - {hora}')
                            print(f'Vagas: {vagas} - Preço: R${valor}')

                    print('-' * 50)

                elif op == 3:
                    print('\n----- Buscar Carona -----')
                    origem_busca = input('Digite a origem desejada: ')
                    destino_busca = input('Digite o destino desejado: ')

                    for email in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email]
                        if origem == origem_busca and destino == destino_busca and int(vagas) > 0:
                            print(f'\nMotorista: {usuarios[email][0]}')
                            print(f'De: {origem} para {destino}')
                            print(f'Data: {data} - {hora}')
                            print(f'Vagas: {vagas} - Preço: R${valor}')
                            break

                    else:
                        print('\nNenhuma carona disponível para essa rota no momento')

                    print('-' * 50)

                elif op == 4:
                    print('\n----- Reservar Vaga -----')
                    origem2 = input('Digite a origem: ')
                    destino2 = input('Digite o destino: ')

                    for email_motorista in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]

                        if origem == origem2 and destino == destino2 and int(vagas) > 0:

                            print(f'\nCarona encontrada:')
                            print(f'Motorista: {usuarios[email_motorista][0]}')
                            print(f'De: {origem} para {destino}')
                            print(f'Data: {data} - {hora}')
                            print(f'Vagas: {vagas} - Preço: R${valor}')

                            confirmar = input('\nReservar esta vaga? (s/n): ')
                            if confirmar == 's':
                                caronas[email_motorista][4] -= 1
                                caronas[email_motorista][6].append(email_login)
                                print('\nReserva confirmada!')
                            else:
                                print('\nReserva cancelada.')
                            break
                    else:
                        print('\nNenhuma carona disponível para essa rota.')

                    print('-' * 50)

                elif op == 5:
                    print('\n----- Cancelar Reserva -----')
                    encontrou_reserva = False
                    for email_motorista in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
                        if email_login in passageiros:
                            encontrou_reserva = True
                            print(f'\nReserva encontrada:')
                            print(f'Motorista: {usuarios[email_motorista][0]}')
                            print(f'De: {origem} para {destino}')
                            print(f'Data: {data} - {hora}')

                            confirmar = input('Cancelar reserva? (s/n): ')

                            if confirmar == 's':
                                caronas[email_motorista][6].remove(email_login)
                                caronas[email_motorista][4] += 1
                                print('Reserva cancelada com sucesso!')
                            break

                    else:
                        print('Você não tem reservas ativas.')

                    print('-' * 50)

                elif op == 6:
                    print('\n-------remover carona--------')
                    data_carona = input('digite a data da carona que você quer remover no formato dd/mm/aa: ')
                    for email_login in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_login]
                        if data == data_carona:
                            remover_carona = input('tem certeza que deseja remover sua carona? (s/n): ')
                            if remover_carona == 's':
                                del caronas[email_login]
                                print('sua carona foi removida com sucesso!!!')
                        else:
                            print('você nâo tem caronas cadastradas! cadastre alguma')

                    print('-' * 50)

                elif op == 7:
                    print('\n-------Mostrar detalhes da carona-------')
                    detcar_email = input('insira os dados do email do motorista: ')
                    detcar_data = input('insira os dados da data no formato dd/mm/aa: ')
                    for email_motorista in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
                        if detcar_email == email_motorista and detcar_data == data:
                            if int(vagas) > 0:
                                print(f'\nMotorista: {usuarios[email_motorista][0]}')
                                print(f'De {origem} para {destino}')
                                print(f'Dia: {data} - {hora}')
                                print(f'Vagas: {vagas} - Preço: R${valor}')
                                print(f'passageiros: {passageiros}' )
                            break
                    else:
                        print('Carona não encontrada com os dados fornecidos.')

                    print('-' * 50)

                elif op == 8:
                    print('\n----------CARONAS QUE VOCÊ SE CADASTROU------------')
                    encontrou_caronas = False
                    for email_motorista in caronas:
                        origem, destino, data, hora, vagas, valor, passageiros = caronas[email_motorista]
                        if email_login in passageiros:
                            encontrou_caronas = True
                            print(f'\nMotorista: {usuarios[email_motorista][0]}')
                            print(f'De {origem} para {destino}')
                            print(f'Dia: {data} - {hora}')
                            print(f'Vagas: {vagas} - Preço: R${valor}')
                            break
                    else:
                        print('\nVocê não está cadastrado em nenhuma carona no momento.')

                    print('-' * 50)

                elif op == 9:
                    print('\n--------- avaliações ----------')
                    print('avalie o motorista da sua carona')
                    email_motorista = input('digite o email do motorista que você deseja avaliar: ')
                    if email_motorista in caronas and email_login in caronas[email_motorista][6]:
                        nota = int(input('Nota (1-5): '))
                        comentario = input('Comentário: ')
                        print('Avaliação registrada!')
                        print('Avaliação registrada!')
                    else:
                        print('Você não participou de caronas desse motorista')

                    print('-' * 50)

                elif op == 10:
                    print('\n-----------logout-------------')
                    msg_confirmacao = input('tem certeza que gostaria de sair? (s/n): ')
                    if msg_confirmacao == 's':
                        print('logout realizado com sucesso, volte sempre!')
                        op = 0
                    else:
                        print('logout cancelado')

                    print('-' * 50)


                elif op == 0:
                    break

                else:
                    print('Email ou senha inválidos!')



                    
                        















