'''#Exercicio 11
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

A = (2*num1)*(num2/2)
B = (3*num1)+ num3
C = num3**3

print('O produto do dobro do primeiro com metade do segundo: ',A)
print('A soma do triplo do primeiro com o terceiro: ',B)
print('O terceiro elevado ao cubo: ',C)'''
'''#Exercicio 12

altura = float(input('Digite a sua altura: '))
pesoideal = (72.7*altura)-58
print(f'O seu peso ideal é {pesoideal} Kg.')'''
'''#Exercicio 13

genero = str(input('Digite seu gênero (F para feminino e M para Masculino): '))
if genero == 'M' or genero == 'F':
    if genero == 'M':
        altura = float(input('Digite a sua altura: '))
        pesoideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é {pesoideal} Kg.')
    else:
        altura = float(input('Digite a sua altura: '))
        pesoideal = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é {pesoideal} Kg.')
else:
    print('Erro!!!')'''
'''#Exercicio 14

peso_de_peixes = float(input('Digite o peso total dos peixes: '))

excesso = peso_de_peixes - 50

if excesso > 0:
    multa = excesso * 4

print(f'O peso total de peixes é {peso_de_peixes} kg')
if excesso > 0:
    print(f'O excesso de peso foi {excesso} kg')
    print(f'O valor da multa é de {multa}')
else:
    print('Não houve excesso de peso e nenhuma multa.')'''
'''#Exercicio 15

valor_hora = float(input('Informe o valor da hora trabalhada: '))
horas_mes = int(input('Informe quantas horas trabalha no mês: '))

salario_bruto = valor_hora * horas_mes
IR = salario_bruto * (11/100)
INSS = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - IR - INSS - sindicato
print(f'Salário Bruto : R${salario_bruto}')
print(f'IR (11%) : R${IR}')
print(f'INSS (8%) : R${INSS}')
print(f'Sindicato (5%) : R${sindicato}')
print(f'Salário Líquido : R${salario_liquido}')'''
'''#Exercício 16

metro_quadrado = float(input('Informe quantos metros quadrados será a área a ser pintada: '))

if metro_quadrado <= 54:
    print('Você irá precisa de 1 lata de tinta e o valor é R$80,00')
else:
    divisor_quant = metro_quadrado//54
    resto_divisão = metro_quadrado%54
    if resto_divisão >0:
        divisor_quant = divisor_quant+1
    preco_total = divisor_quant * 80
    print(f'Você irá precisar de {divisor_quant} latas de tintas e o valor é de R${preco_total}.')'''





