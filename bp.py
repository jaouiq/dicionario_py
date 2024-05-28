# importa biblioteca
import os

# dicionário
pessoa = {
    'Nome':'',
    'CPF':'',
    'RG':'',
    'Data de Nascimento':'',
    'Gênero':'',
    'E-mail':'',
    'Telefone':'',
    'Tipo sanguíneo':'',
    'Profissão':'',
    'Empresa':''
}

# adiciona nova chave
pessoa['Nome'] = input('Informe o seu nome:')
pessoa['CPF'] = input('Informe o seu CPF:')
pessoa['RG'] = input('Informe o seu RG:')
pessoa['Data de Nascimento'] = input('Informe a sua data de nascimento:')
pessoa['Gênero'] = input('Informe o seu gênero:')
pessoa['E-mail'] = input ('Informe o seu E-mail:')
pessoa['Telefone'] = input('Informe seu número de telefone:')
pessoa['Tipo sanguíneo'] = input('Informe o seu tipo sanguíneo:')
pessoa['Profissão'] = input('Informe a sua profissão:')
pessoa['Empresa'] = input('Informe a sua empresa:')

# limpa console
os.system('cls')

# laço
print(f'{'-'*30}DADOS DO USUÁRIO{'-'*30}')
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
