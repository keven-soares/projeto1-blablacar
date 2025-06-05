def mostrar_linha():
    print('-' * 50)

def verificar_email(email):
    while not ('@' in email and '.' in email.split('@')[1]):
        email = input('digite um email válido (deve conter @ e .com): ')

def verificar_data():
    dia_limite = 1
    mes_limite = 5
    ano_limite = 2025

    while True:
        data_carona = input('Insira a data da carona no formato: DD/MM/AAAA. ')

        if len(data_carona) == 10 and data_carona[2] == '/' and data_carona[5] == '/' and \
                data_carona[:2].isdigit() and data_carona[3:5].isdigit() and data_carona[6:].isdigit():

            dia = int(data_carona[0:2])
            mes = int(data_carona[3:5])
            ano = int(data_carona[6:10])

            if dia <= 0 or dia > 31:
                print('Insira valores de 1 a 31 para o dia.')
            elif mes <= 0 or mes > 12:
                print('Insira valores de 1 a 12 para o mês.')
            elif ano < 2025:
                print('Não existe máquina do tempo. Insira um valor válido para o ano.')
            elif ano < ano_limite or (ano == ano_limite and mes < mes_limite) or (
                    ano == ano_limite and mes == mes_limite and dia < dia_limite):
                print("a carona não pode ser no passado!")
            else:
                print("Data válida para carona!")
                return data_carona
        else:
            print("Formato inválido. Certifique-se de usar o formato DD/MM/AAAA.")

