import java.util.Scanner;

public class SquareCalculator {
    public static void main(String[] args) {
        System.out.println("This program computes the square of an integer");
        System.out.println();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int n = scanner.nextInt();
        scanner.close();

        int acc = 0;
        int odd = 1;
        for (int i = 0; i < n; i++) {
            acc += odd;
            odd += 2;
        }
        System.out.println("The square of " + n + " is " + acc);
    }
}
