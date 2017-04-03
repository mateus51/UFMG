/*
Mateus Lopes Teixeira
2012055120

SPOJ - BSEARCH1 - Binary Search

Para resolver este problema, pode ser implementado uma simples busca binaria em C. 
O diferencial deste exercicio e que deve-se imprimir na tela a primeira ocorrencia 
do numero procurado, e na busca binaria, isso nao e equivalente a imprimir sua ocorrencia
assim que o numero for encontrado, pois o vetor, apesar de ordenado, pode-se assemelhar
a algo como: 0 1 1 1 1 1 1 1 1 2.
Para contornar isso, cria-se uma variavel first_occurrance, e caso o numero procurado seja
encontrado no vetor, seu indice é armazenado nela. O algoritmo continua sua execucao normalmente
(a primeira metade do vetor, pois e irrelevante se houver um numero igual em um indice maior).
Caso outro valor igual seja encontrado em um indice menor do vetor, atualiza-se o valor
dessa variavel, ate que o algoritmo acabe sua execucao. Assim, sabe-se que esta sendo
impresso a primeira ocorrencia do numero no vetor.
*/

#include <stdio.h>
#include <stdlib.h>

int binary_search(int *array, int query, int size) {
    int low, high, mid;
    int first_occurrence = -1;  // We mark the first occurrence of the queried number
    
    low = 0;
    high = size - 1;
    
    while(low <= high) {
        
        mid = (low + high) / 2;
        
        // If we find the item, we mark it as the first occurrence and keep
        // running the algorithm. 
        if(array[mid] == query) {
            first_occurrence = mid;
            high = mid - 1;
        }
        else if(array[mid] > query) 
            high = mid - 1;
        else if(array[mid] < query)
            low = mid + 1;
    }
    // This will make sure that the 1st occ is the smallest
    // index that we could find a match
    if(first_occurrence != -1) 
        return first_occurrence;
    else
        return -1;
}

int main(void) {
	int n, queries, query;
	int i = 0;
	int position;
	
	// Read N and Q from input
	scanf("%d %d", &n, &queries);
	
	int *array = (int*) malloc (n * sizeof(int)); // Allocate n-sized array
	
	for(i = 0; i < n; i++) 
	    scanf("%d", &array[i]);

	// Do a binary search in every query
	for(i = 0; i < queries; i++) {
	    scanf("%d", &query);
	    position = binary_search(array, query, n);
        printf("%d\n", position);
	}
	
	return 0;
}

