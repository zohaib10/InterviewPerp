public class coins {

  public static void main(String [] args){
    System.out.println("Coins program");
    int [] coins = {25, 10, 5, 1};
    System.out.println(makeChange(55,coins));
  }

  //Given an input X, write a function to determine minimum number of coins required to make the exact amount of change.
  public static int makeChange(int amount, int [] coins){
        if(amount == 0) return 0;
        int min = amount;
        for(int coin : coins){
          if(amount - coin >= 0){
            int c = makeChange(amount-coin, coins);
            if(min > c+ 1){
              min = c + 1;
            }
          }
        }
        return min;
  }




}
