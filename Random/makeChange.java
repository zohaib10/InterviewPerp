class MakeChange {
    public static void main(String[] args) {
        System.out.println("Hello");
        int [] change = {25, 10, 5, 1};

        int ans = makeChange(32, change);
        System.out.println(ans);
    }


    public static int makeChange(int total, int [] coins) {

        if (total == 0) {
            return 0;
        }
        int min = total;
        for (int i = 0; i < coins.length; i++) {
              int remainder = total - coins[i];
              
              if (remainder >= 0) {
                  int ans = makeChange(remainder, coins);

                  if (ans < min) {
                      min = ans + 1;
                  }
                }
        }

        return min;
    }


}


/**
 * 
 * Total: 32
 * coins: [25, 10, 5, 1]
 * 
 * min: 32
 * 
 * i = 0
 * 
 *  t: 32
 *  c: 25
 *  r: 7
 *     
 *      i: 0     
 *      t: 7
 *      c: 25
 *      r: -18
 * 
 *      i: 1
 *      t: 7
 *      c: 10
 *      r: -3
 * 
 *      i: 2
 *      t: 7
 *      c: 5
 *      r: 2
 * 
 *          i: 0, 1, 2 SKIPS BECAUSE ALL ARE NEGATIVE
 *          
 *          i: 3
 *          t: 2
 *          c: 1
 *          r: 1
 *                                                                  -> min was 1 + 1 = 2
 *              i: 0, 1, 2 SKIPS BECAUSE ALL ARE NEGATIVE
 * 
 *              i: 3
 *              t: 1
 *              c: 1
 *              r: 0
 *              
 *           
 *
 * 
 * 
 * 
 * 
 * 
 * 
 */