/**
 * The BubbleSort class provides an implementation of the Bubble Sort algorithm
 * for sorting an array of integers in ascending order.
 */
public class BubbleSort {

    /**
     * Sorts the given array of integers using the Bubble Sort algorithm.
     *
     * @param arr the array of integers to be sorted
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were swapped in the inner loop, the array is already sorted
            if (!swapped) {
                break;
            }
        }
    }

    /**
     * Main method to test the BubbleSort algorithm.
     *
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};

        System.out.println("Before sorting:");
        printArray(myArray);

        bubbleSort(myArray);

        System.out.println("After sorting:");
        printArray(myArray);
    }

    /**
     * Prints the elements of the given array.
     *
     * @param arr the array to be printed
     */
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}

