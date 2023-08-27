
'''
1.Faça um Programa que peça um número e então mostre a mensagem:-> O número informado foi[número].

2.Faça um Programa que peça dois números e imprima a soma.

3.Faça um Programa que peça a temperatura em graus Celsius,transforme e mostre em graus Fahrenheit.

4.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.
'''


# Questão 1:

numero = int(input('Informe um numero: '))
print(f'O número informado foi {numero}.')



# Questão 2:

numero1 = int(input('Informe seu primeiro número: '))
numero2 = int(input('Informe seu segundo número: '))

soma = numero1 + numero2

print(f'A soma dos números é: {soma}.')



# Questão 3:

temperatura_C = float(input('Informe uma temperatura em graus Celsius (°C): '))

temperatura_F = ((temperatura_C * 1.8) + 32)

print(f'O valor da temperatura em graus Fahrenheit é: {temperatura_F}.')



# Questão 4:

valor_hora = float(input('Informe quanto você ganha por hora trabalhada: '))

numero_horas = int(input('Informe o número de horas trabalhada no mês: '))

salario = valor_hora * numero_horas

print(f'Total do seu salário no mês é: R${salario}.')
