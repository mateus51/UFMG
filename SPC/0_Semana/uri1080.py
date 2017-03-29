'''
Mateus Lopes Teixeira
2012055120

URI1080 - Maior e Posicao
Este problema baseia-se em em achar o maior numero entre 100 elementos 
distintos, e retorna o seu valor e sua posicao.
Para isso, basta ler todos os inteiros da entrada, armazena-los em 
um vetor, e percorrer o vetor. Cria-se uma variavel 'max' e seu valor e
igual ao valor do primeiro item do vetor. Caso um numero maior seja encontrado,
trocamos o valor de 'max', e mantemos a posicao que o elemento foi encontrado
em uma outra variavel.
'''

# Get all the input values, and append them to an array
nums = []
for i in range(0, 100):
	nums.append(int(input()))

# Search manually for the largest element on the array
max_value = nums[0]
max_value_index = 0

for index, item in enumerate(nums):
	if item > max_value:
		max_value = item
		max_value_index = index + 1
		
print(max_value)
print(max_value_index)
