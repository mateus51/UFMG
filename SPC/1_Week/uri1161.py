'''
Mateus Lopes Teixeira
2012055120

URI1161 - Soma de Fatoriais
Para resolver esse problema, lemos inteiros M e N da entrada.
Entao, calculamos seus respectivos fatoriais, fazemos a soma dos mesmos
e a imprimimos na tela.
'''

def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n-1)

while True:
	try:
		m, n = input().split()

		fact_m = factorial(int(m))
		fact_n = factorial(int(n))
		print(fact_m + fact_n)

	except ValueError:
		break
	except EOFError:
		break

