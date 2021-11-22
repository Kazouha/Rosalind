public class ConditionsAndLoops {
    public static void main(String[] args) {
        // Input variables
        int a = 100;
        int b = 200;

        // Calculation
        int sum = 0;

        for(int i = a; i <= b; i++) {
            if(i % 2 == 1) { // Only adds i to sum if i is odd
                sum += i;
            }
        }

        System.out.println(sum);
    }
}
