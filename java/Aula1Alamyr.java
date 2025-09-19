import java.util.Scanner;

public class Aula1Alamyr {
 public static void main(String[] args) {
  String nome;
  int idade;
  double valor;
  Scanner sc = new Scanner(System.in);

  System.out.println("Digite seu nome: ");    
  nome = sc.nextLine();

  System.out.println("Digite sua idade: ");
  idade = sc.nextInt();
  
  System.out.println("Digite seu salario: ");
  valor = sc.nextDouble();
 }
    }