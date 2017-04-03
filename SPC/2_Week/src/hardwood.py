'''
Mateus Lopes Teixeira
2012055120

URI1260 - HARDWOOD SPECIES

Para resolver este problema, pode-se criar um dicionario em Python para armazenar
dados no seguinte formato:
{especie, ocorrencias}
aonde ocorrencias sao quantas vezes a especie foi mencionada na lista de entrada.
Feito isso, cria-se uma lista ordenada dos nomes das especies (para imprimir) e a percorremos.
Usamos o item atual para acessar o dicionario, no formato species_dict[item] e 
entao vemos quantas vezes a especie foi mencionada. Sabendo quantas linhas a entrada original tem
(pela variavel counter), podemos calcular a sua frequencia, e entao imprimimos no formato pedido.
'''

i = 0
test_cases = int(input())
input()	# Read a white line 

for i in range(test_cases):

	species_dict = {}
	counter = -1	# -1 just works...
	i += 1

	while(True):
		try:
			species = input()
		except (EOFError):
			break;

		counter += 1		# Add 1 to the overall counter

		if species == "":
			break

		if species not in species_dict:	# NEW ENTRY
			species_dict[species] = 1
		else:
			species_dict[species] += 1 	# UPDATE THE FREQUENCY

	sorted_species_list = sorted(species_dict.keys())

	# PRINTS THE ORDERED LIST AND THE PERCENTAGE OF OCCURRENCES
	for item in sorted_species_list:			# Sorts the list of names
		occurrences = species_dict[item]		# Then use the species name to access the dictionary with the frequencies
		frequency = float(occurrences / counter) * 100
		print(item + " ", end="")
		print("{0:.{1}f}".format(frequency, 4))

	# If there are more test cases to come, print a newline. The program ends otherwise.
	if i < test_cases:
		print("")