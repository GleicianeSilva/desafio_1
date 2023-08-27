'''

1. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda
estrangeira. Considere a tabela de conversão abaixo:

Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21

2. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 80,00 por dia e R$ 0,20 por km rodado.

3. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário.

Se o salário for até R$ 1000,00 o funcionário terá 20% de aumento.
Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de aumento.
Acima de R$ 2801,00 o funcionário terá 5% de aumento.

4. Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.
Ex: n = leiaInt(‘Digite um n’)

'''


# Questão 1:

valores = {'Dólar Americano': 4.91,'Peso Argentino': 0.02,'Dólar Australiano': 3.18,'Dólar Canadense': 3.64,'Franco Suiço': 0.42,'Euro': 5.36,'Libra Esterlina': 6.21}

dinheiro = float(input('\nInforme a quantidade de dinheiro que você tem em sua carteira: R$'))

for valor, valor_quantidade in valores.items():

    novo_valor = (dinheiro/valor_quantidade)

    print(f'\nValor ({valor}): {novo_valor:.2f}')
    
print('\n')



# Questão 2:

qnt_km = float(input('\nInforme a quantidade de quilometro percorrido pelo carro alugado: '))

qnt_dias = float(input('\nInforme a quantidade de dias que o carro foi alugado: '))

custo_km = qnt_km * 0.20

custo_dias = qnt_dias * 80

preco_pagar = custo_km + custo_dias

print(f'\nO preço total pago será: {preco_pagar:.2f}')



# Questão 3:

salario = float(input('\nInforme seu salário: R$'))

if salario <= 1000:
    novo_salario = salario + (salario * 0.2)

elif salario <= 1001 or salario <= 2800:
    novo_salario = salario + (salario * 0.1)

else:
    novo_salario = salario + (salario * 0.05)

print(f'\nNovo salário: R${novo_salario:.2f}')

print('\n')



# Questão 4:

def leiaInt(n):

    while True:

        try:
            numero_inteiro = int(input(n))
            return numero_inteiro
        
        except ValueError:

            print('\nERRO! Só é permitido valor númerico inteiro.')


inteiro = leiaInt('\nDigite um valor númerico: ')

print(f'\nO valor númerico informado foi: {inteiro}')

print('\n')