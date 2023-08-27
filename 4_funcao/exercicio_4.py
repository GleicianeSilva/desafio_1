'''
1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

2. "Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

'''


# Questão 1:

def soma (n1, n2, n3):
    soma_total = n1 + n2 +n3
    return soma_total

n1 = float(input('\nInforme seu primeiro número: '))
n2 = float(input('\nInforme seu segundo número: '))
n3 = float(input('\nInforme seu terceiro número: '))

print(f'\nA soma destes três argumentos é: {soma(n1, n2, n3)}')

print('\n')



# Questão 2:

def numero_reverso(numero):
    return int(str(numero)[::-1])

numero = int(input('\nInforme um número: '))

print(f'O número reverso é: {numero_reverso(numero)}')

print('\n')



# Questão 3:

def celsius_fahrenheit(temperatura_c):
    
    temperatura_fahrenheit = (float(1.8 * (temperatura_c)) + 32)
    return temperatura_fahrenheit
    
def fahrenheit_celsius(temperatura_f):

    temperatura_celsius = (float((temperatura_f) - 32) / 1.8)
    return temperatura_celsius

def menu(): 

    while True:
        opcao = int(input('\nQual temperatura você deseja converter ==> 1 - Celsius e 2 - Fahrenheit: '))
    
        if opcao == 1:
            temperatura_c = float(input('\nDigite uma temperatura em ºC: '))
            print(f'\nConvertendo a temperatura de Celsius para Fahrenheit é: {celsius_fahrenheit(temperatura_c):.2f}ºF')

        elif opcao == 2:
            temperatura_f = float(input('\nDigite uma temperatura em ºF: ')) 
            print(f'\nConvertendo a temperatura de Fahrenheit para Celsius é: {fahrenheit_celsius(temperatura_f):.2f}ºC')

        else:
            print('\nOpção incorreta! Tente novamente.')

menu()