'''
1. "Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno,imprima o número de alunos com média maior ou igual a 7.0."

2. Programa nome ao contrário em maiúsculas.Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

3. Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim, imprima True. Caso contrário, imprima Falso.

4. "Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.As perguntas são: 

""Telefonou para a vítima?"" 

""Esteve no local do crime?"" 

""Mora perto da vítima?"" 

""Devia para a vítima?"" 

""Já trabalhou com a vítima?""

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será classificado como""Inocente"".
'''


# Questão 1:

numero_aluno = 0

medias_alunos = []

media_maior = 0

for numero_aluno in range(10):

    nota1 = float(input(f'\nDigite a primeira nota do {numero_aluno+1}º aluno: '))
    nota2 = float(input(f'Digite sua segunda nota {numero_aluno+1}º aluno: '))
    nota3 = float(input(f'Digite sua terceira nota {numero_aluno+1}º aluno: '))
    nota4 = float(input(f'Digite sua quarta nota {numero_aluno+1}º aluno: '))

    media = ((nota1 + nota2 + nota3 + nota4) / 4)

    medias_alunos.append(media)

    if medias_alunos[numero_aluno] >= 7.0:
        media_maior += 1

print('\nMédias dos 10 alunos: ', medias_alunos)

print('\nQuantidade de alunos com média maior: ', media_maior)

print('\n')
        


# Questão 2:

nome = str(input('\nDigite seu nome em letras maiúsculas ou minúsculas: ')).upper()

print(f'\nNome invertido e em maiúscula: {nome[::-1]}')

print('\n')



# Questão 3:

dicionario = {'Cidade': 'Vitória', 'Telefone':81999999999, 'Data de Nascimento': '',  'Curso':()}

for palavra, posicao in dicionario.items():
    if not posicao: 
        print(f'\n({palavra} => {posicao}) é: False')
    else:
        print(f'\n({palavra} => {posicao}) é: True')

print('\n')



# Questão 4:

classificacao = ('Suspeita', 'Cúmplice', 'Assassino', 'Inocente')

quetionario = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ' ]

soma = 0

for pergunta in range(len(quetionario)):
    resposta = str(input(quetionario[pergunta]))
    if(resposta.capitalize() == 'Sim'):
        soma+=1

if(soma == 2):
    print(f'\nA pessoa é {classificacao[0].upper()} na participação do crime.')
elif(soma == 3 or soma == 4):
    print(f'\nA pessoa é {classificacao[1].upper()} na participação do crime.')
elif (soma == 5):
    print(f'\nA pessoa é {classificacao[2].upper()} na participação do crime.')
else:
    print(f'\nA pessoa é {classificacao[3].upper()} na participação do crime.')

print('\n')