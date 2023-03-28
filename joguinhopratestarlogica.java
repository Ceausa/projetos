package projeto01;

import java.util.Scanner;

public class Main{

	
	public static void main(String[]args) {
		Scanner scanner = new Scanner(System.in);
		int pontos = 0;
		System.out.println("------ QUIZZZZZZZZZZZ --------");
		System.out.println("OBS: Todas as respostas do jogo devem ser escritas com letras minusculas!");
		System.out.println("");
		System.out.println("Bem vindo! Pressione S para continuar!.");
		String string = scanner.nextLine();
		if(string.equals("s")) {
			System.out.println("Qual a capital do Brasil?");
		    string = scanner.nextLine();
			
		    if(string.equals("brasilia")) {
				System.out.println("Voce pontuou!");
				pontos++;
				System.out.println("Deseja continuar (s) ou desistir? (d)");
				string = scanner.nextLine();
				
				if(string.equals("s")) {
					//prox pergunta.
					System.out.println("Em qual continente fica o Brasil?");
					string = scanner.nextLine();
					
					if(string.equals("america do sul")){
						System.out.println("Voce pontuou!");
						pontos++;	
						System.out.println("Deseja continuar (s) ou desistir? (d)");
						string = scanner.nextLine();
						if(string.equals("s")) {
						 	//proxima pergunta   
							System.out.println("Qual a moeda da india?");
							string = scanner.nextLine();
							if(string.equals("rupia")) {
								pontos++;
								System.out.println("PARABENS, VOCE ZEROU O JOGO!");
								System.out.println("A sua pontuação foi de: "+pontos);
							 }else {
								 System.out.println("Game Over! sua pontuação foi de: "+pontos);
							 }
							
					       }else {
								System.out.println("Game-Over! sua pontuação foi de: "+pontos);
							}	
						}else {
							System.out.println("Game-Over! sua pontuação foi de: "+pontos);
						}
					}else {
					 System.out.println("Game-Over! Sua pontuação foi de:" +pontos);
				 }																		
				}else { 
					System.out.println("Game-over! Sua pontuação foi de: "+pontos);
				}
			}else {
				System.out.println("Acabou o jogo... voce pontuou "+pontos);
 		    }
	}
}

	
