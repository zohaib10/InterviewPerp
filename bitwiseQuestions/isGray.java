/*
Questions: Given Two integers determine if they differ by ony one bit.

4 & 5

0100
0101
^
0001

--------

4 & 7

0100
0111
^
0011

*/

public class isGray{



public static boolean isGray(int num1, int num2){
  int numX = num1 ^ num2;
  while(numX > 0){
    if(numX % 2 == 1 && numX >> 1 != 0){
      return false;
    }
    numX = numX >> 1;
  }
  return true;
}

  public static void main(String [] args){
    if(isGray(4,7)){
      System.out.println("isGray");
    }else{
      System.out.println("Not isGray");
    }


  }


}
