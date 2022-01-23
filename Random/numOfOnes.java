/**
 * Find number of 1s in the binary represenation of a number
 * 
 * 
 * eg.
 * 
 * ones(2) => 10 => ans: 1
 * ones(3) => 11 => ans: 2
 * ones(5) => 110 => ans: 2
 * ones(7) => 111 => ans: 3
 * 
 * 
 * 
 * ex:
 * 
 *  x: 110
 * 
 *  sum: 0
 * 
 *  sum: 110 ^ 001 = 0
 * 
 */



public class numOfOnes {
    
    public static void main(String[] args) {
        System.out.println("Get Number of ones in a bit string");
        System.out.println(ones(6));
    }


    public static int ones(int x) {

        int sum = 0;

        while (x > 0) {            
            sum += x & 1;
            x >>= 1;
        }
        return sum;
    }
}
