public class BinaryTree{
  /*
          5
       2     7
     1  3  6  8

  */
   static Node root;

  BinaryTree(){}

  public static void insert(int val){
    root = insertNode(root, val);
  }

  public static Node insertNode(Node curr, int value){
    if(curr == null){
      System.out.println("inserting");
      return new Node(value);
    }
    if(value < curr.value){
      System.out.println("going left");
      curr.left = insertNode(curr.left, value);
    }else if(value > curr.value){
      System.out.println("going right");
      curr.right = insertNode(curr.right, value);
    }else{
      return curr;
    }
    return curr;
  }

  public static BinaryTree createBinaryTree(){
    BinaryTree bst = new BinaryTree();

    bst.insert(5);
    bst.insert(2);
    bst.insert(1);
    bst.insert(3);
    bst.insert(7);
    bst.insert(8);
    bst.insert(6);

    return bst;
  }


  public static void main(String [] args){
    BinaryTree bst = createBinaryTree();



    System.out.println("Works");
  }



}
