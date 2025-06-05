usuarios = {'kevensoares@gmail.com': ['joelderson keven soares da silva','keven123',['3', 'motorista legal']],
            'jubiscleudo@gmail.com': ['jubiscleudo jeberson santos', 'juju123']}

import utilidade
def cadastrar_usuario():
    print('----------- CADASTRO ------------')
    nome_completo = input('digite seu nome completo: ')
    email = input('digite seu melhor email: ')
    while not ('@' in email and '.' in email.split('@')[1]):
        email = input('digite um email válido (deve conter @ e .com): ')
    senha = input('digite sua senha: ')
    usuarios[email] = [nome_completo, senha, []]
    print('usuário cadastrado com sucesso!')

def fazer_login():
    print('-------- FAÇA SEU LOGIN ----------')
    email_login = input('digite seu email: ')
    senha_login = input('digite sua senha: ')
    if email_login in usuarios and usuarios[email_login][1] == senha_login:
        return email_login
    return None

def sair_programa():
    print('\n-----------logout-------------')
    msg_confirmacao = input('Tem certeza que gostaria de sair? (s/n): ')
    if msg_confirmacao.lower() == 's':
        print('Logout realizado com sucesso, volte sempre!')
    else:
        print('Logout cancelado')
    utilidade.mostrar_linha()

