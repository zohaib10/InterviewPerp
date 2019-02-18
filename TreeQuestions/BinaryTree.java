import java.util.LinkedList;
import java.util.Queue;


public class BinaryTree{
  /*
          5
       2      7
     1  3   6  8
         4      64
               29
  */
   static Node root;

  BinaryTree(){}

  public static void insert(int val){
    root = insertNode(root, val);
  }

  public static Node insertNode(Node curr, int value){
    if(curr == null){
      //System.out.println("inserting");
      return new Node(value);
    }
    if(value < curr.value){
      //System.out.println("going left");
      curr.left = insertNode(curr.left, value);
    }else if(value > curr.value){
      //System.out.println("going right");
      curr.right = insertNode(curr.right, value);
    }else{
      return curr;
    }
    return curr;
  }

  //########################################################################################################
  //Print Tree in Level Order

  public static void printLevelOrder(){
    Queue<Node> q = new LinkedList<>();

    q.add(root);
    while(q.size() != 0){
      Node item = q.remove();
      System.out.print(item.value + ", ");
      if(item.left != null){
        q.add(item.left);
      }
      if(item.right != null){
        q.add(item.right);
      }
    }
    System.out.println();

    /*
      5, 2, 7, 1, 3, 6, 8, 4, 13, 64, 29,

      Refernces:
        1. https://www.geeksforgeeks.org/queue-interface-java/
    */
  }

//########################################################################################################
//Determine whether the Tree is a binary search Tree

  public static boolean isBst(){
    if(isBst(root.left, Integer.MIN_VALUE, root.value) && isBst(root.right, root.value, Integer.MAX_VALUE)){
      return true;
    }
    return false;
  }

  public static boolean isBst(Node n, int min, int max){
    if(n == null){
      return true;
    }
    if(n.value > max || n.value < min){
      return false;
    }
    return isBst(n.left, min, n.value) &&
          isBst(n.right, n.value, max);
  }

//########################################################################################################
/*
Question: Given a BinaryTree write a function to determine whether the tree is Balanced
Approach: A tree is balanced if the height of the Left subtree and Right subtree differ only by 1
*/

public static int isTreeBalanced(Node curr){
  if(curr == null){
    return 0;
  }

  int left = isTreeBalanced(curr.left);
  int right = isTreeBalanced(curr.right);

  if(left == -1 || right == -1) return -1;
  if(Math.abs(left - right) > 1) return -1;

  if(right > left) return right + 1;
  else return left + 1;

}

public static boolean isTB(){
  if(isTreeBalanced(root) == -1){
    return false;
  }
  return true;
}


//########################################################################################################
//Questions: Given a tree write a function to find the length of the longest branch of nodes in increasing consecutive order.
/*
                            5
                          /   \
                        2      6
                      /  \      \
                    1    3       7
                         \        \
                         4        8


if val of current Node == val of parnet + 1 -

*/



public static int longestConsecutiveIncBranch(){
  return Math.max(maxLen(root.left,root.value,0),maxLen(root.right,root.value,0));
}


public static int maxLen(Node curr, int parent, int length){
  if (curr == null) return length;

  if(parent + 1 == curr.value){
    int lv = maxLen(curr.left, curr.value, length+1);
    int rv = maxLen(curr.right, curr.value, length+1);
    return Math.max(lv,rv);
  }else{
    int lv = maxLen(curr.left, curr.value, length+1);
    int rv = maxLen(curr.right, curr.value, length+1);
    return Math.max(Math.max(lv,rv),length);
  }

}





//########################################################################################################

  public static BinaryTree createBinaryTree(){
    BinaryTree bst = new BinaryTree();

    bst.insert(5);
    bst.insert(2);
    bst.insert(1);
    bst.insert(3);
    bst.insert(6);
    bst.insert(7);
    bst.insert(64);
    bst.insert(4);

    return bst;
  }


  public static void main(String [] args){
    BinaryTree bst = createBinaryTree();
    System.out.println(longestConsecutiveIncBranch());

     // if(isTB()){
     //   System.out.println("Balanced Tree");
     // }else{
     //   System.out.println("Tree not Balanced");
     // }
    //bst.printLevelOrder();
  }



}
