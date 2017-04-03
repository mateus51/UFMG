'''
Mateus Lopes Teixeira
2012055120

ELEICOES

Este problema pode ser resolvido criando um dicionario em Python, aonde
a chave do dicionario e o numero do candidato, e o seu valor sao os votos
que o candidato recebeu. Para cada valor de entrada, pode-se conferir
se o candidato ja esta no dicionario, e atualizar seus votos de acordo.
Para imprimir, basta ordenar o dicionario de acordo com as keys, e imprimir
o primeiro item do dicionario, que e o candidato com mais votos.
'''
# Get the input and create an empty dictionary
n = int(input())
candidates = {}  # candidates = {candidate_code, votes}

# Populate the dictionary: 
# if the candidate has already appeared before, add one vote 
# if it hasn't, then initialize its value with 1
for i in range(0, n):
  cand_code = input()
  
  if cand_code in candidates: 
    candidates[cand_code] += 1
  else:
    candidates[cand_code] = 1

# Sorts the dictionary based on the value, not the key, in a destructive way
sorted_dict = sorted(candidates, key=candidates.get, reverse=True)
# Gets the first item in the sorted dictionary, the candidate with the most votes
winner_candidate = list(sorted_dict)[0]

print(winner_candidate)