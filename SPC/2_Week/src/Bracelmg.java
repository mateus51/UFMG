/**
 * Mateus Lopes Teixeira
 * 2012055120
 * SPOJBR - BRACELMG
 * 
 * Este problema pode ser resolvido apenas procurando uma string dentro de outra.
 * Neste caso, usamos o metodos indexOf() para procurar a string proibida dentro da string original.
 * Caso este metodo retorne -1, quer dizer que nao faz parte. O bracelete e circular, isso significa
 * que podemos concatenar ele nele mesmo para "simular" a sua caracteristica de ser circular.
 * Caso nao encontremos o padrao na string original, invertemos ela e procuramos. Caso nao esteja
 * na string reversa tambem, quer dizer que o padrao nao se encontra de jeito nenhum na string.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BracelMG {
	public static void main(String[] args) {
				
		try {
			BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
			
			int testCases = Integer.parseInt(reader.readLine());	
			// Read all test cases
			for(int i = 0; i < testCases; i++) {
				String[] words = reader.readLine().split(" ");
				String forbidden = words[0];
				String bracelet = words[1];
				
				// Since the bracelet is circular, we can solve this by concatenating itself twice
				bracelet += bracelet;
				
				// Search for the forbidden sequence in the bracelet				
				if(bracelet.indexOf(forbidden) != -1) {	// If found in the original bracelet
					System.out.println("S");
				}
				else {
					// Reverse it and search backwards
					bracelet = new StringBuilder(bracelet).reverse().toString();
					if(bracelet.indexOf(forbidden) != -1)	// If found in the reversed bracelet
						System.out.println("S");
					else									// If not found in any order
						System.out.println("N");
				}
			}
			
		} 
		catch (IOException e) {
			e.printStackTrace();
		}	
	}
}
