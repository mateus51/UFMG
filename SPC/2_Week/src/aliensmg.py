

'''This method splits a DNA sequency into a dictionary of frequencies
Such as: ABCACC -> {A = 2, B = 1, C = 3}
''' 
def get_dna_frequency(dna_sequency):
	dna_frequency = {}

	for elem in dna_sequency:
		if elem not in dna_frequency:
			dna_frequency[elem] = 1
		else:
			dna_frequency[elem] += 1
	#print(dna_frequency)
	return dna_frequency


n = int(input())
dna_sequences = []

# Create array 
for i in range(0, n):
	dna = input()
	dna_sequences.append(dna)

	get_dna_frequency(dna)

# EACH ELEMENT OF THE DNA_SEQUENCES ARRAY SHOULD BE A TUPLE:
# (dna_sequence, frequence_dictionary)