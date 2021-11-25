public class StringsAndLists {
    public static void main(String[] args) {
        // Input variables
        String inputString = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.";

        int a = 22; 
        int b = 27; 
        int c = 97; 
        int d = 102;

        // Print result
        System.out.println(inputString.substring(a, b+1) + " " + inputString.substring(c, d+1));
    }
    
}
