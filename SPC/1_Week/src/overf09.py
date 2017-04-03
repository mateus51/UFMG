'''
Mateus Lopes Teixeira
2012055120

OVERF09 - Overflow
Para detectarmos se havera overflow na operacao,
primeiro lemos a entrada e a separamos em tres variaveis:
um digito, um caracter representando a operacao, e outro digito.
Caso o resultado da operacao detalhada seja maior que o N lido, em que N
representa o maior numero que o computador consegue representar, imprimimos 'OK'.
 Caso contrario, imprimimos 'OVERFLOW'.
'''

def make_operation(digit1, digit2, operation):
	if operation == '+':
		return digit1 + digit2
	else:
		return digit1 * digit2

max_num = int(input())
digit1, operation, digit2 = input().split()
digit1 = int(digit1)
digit2 = int(digit2)
result = make_operation(digit1, digit2, operation)

if result > max_num:
	print("OVERFLOW")
else:
	print("OK")
