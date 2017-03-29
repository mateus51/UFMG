'''
Mateus Lopes Teixeira
2012055120

SOMA
Este problema baseia-se em somar N inteiros e retornar sua soma.
Le-se um inteiro N da entrada, e depois lemos N inteiros. A cada iteracao,
a soma total e atualizada com o novo valor lido.
'''

n = int(input())
sum = 0
for i in range(0, n):
	sum += int(input())

print(sum)
