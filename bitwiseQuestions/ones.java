public class ones{

  public static void main(String [] args){
      //Question: Find number of ones in a binary representation of a number
      System.out.println(ones(7));
  }

  public static int ones(int n){
    int count = 0;
    //count each one once and shift right by one bit
    while(n > 0){
      count += n & 1;
      n = n >> 1;
    }
    return count;
  }


}
