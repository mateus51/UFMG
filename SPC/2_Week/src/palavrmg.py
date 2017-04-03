'''
Mateus Lopes Teixeira
2012055120

PALAVRMG - Palavras Ordenadas
Para resolver esse problema, lemos um inteiro N da entrada, e depois N palavras.
Pode-se armazenar estas N palavras em um vetor, que entao deve ser percorrido e 
cada palavra e analisada pela funcao checkWord, para entao o resultado ser imprimido,
a fim de compactuar com o formato estabelecido pelo SPOJ. 
Na funcao checkWord, comparamos o index [i] com o index [j] da palavra, sendo j = i + 1,
ou seja, o proximo caracter. Caso o caracter a frente do caracter atual seja menor que ele,
portanto nao obedecendo a ordem alfabetica, retornamos False. Caso a palavra seja percorrida
sem que essa condicao seja encontrada, retornamos True.
'''

def checkWord(word):
	i = 0
	while(i < len(word) - 1):
		# If the word is not in alphabetical order, it will return False right here
		if(word[i+1] < word[i] or (word[i+1] == word[i])):
			return False
		i += 1

	return True

i = 0
n = int(input())
words = []

# Create the array containing all the input words
while i < n:
	word = input()
	words.append(word)
	i += 1

# Iterate through the array, and check every word
for i in range(0, len(words)):
	result = checkWord(words[i].lower())
	if result == False:
		print(words[i] + ": N\n", end="")
	else:
		print(words[i] + ": O\n", end="")