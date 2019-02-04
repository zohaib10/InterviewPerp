public class MaxStack{

  //Design a stack with push(), pop() and, max() functions which returns the max value in the stack all of which are O(1) time.

  //Questiosn to ask
    //What kind of data?
    //Can we use linkedLists?

  /*

  For push() add to begining - change head
    push(1)
      1 -> null
    push(2)
      2 -> 1 -> null

  For pop() remove head and make the next new head
    -Everytime we pop we check to see if this was the max and if so we set max to old max of that node

  For max() have a pointer which points to max and we return its value




  */


  public static Node head;
  public static Node max;

  public static class Node{
    public int val;
    public Node next;
    public Node oldMax;
    Node(){}
    Node(int val){
      this.val = val;
    }

    public static Node push(int val){
      if(head == null){
        head = new Node(val);
        max = head;
      }else{
        Node temp = new Node(val);
        temp.next = head;
        head = temp;
        if(max.val < head.val){
          head.oldMax = max;
          max = head;
        }
      }
      return head;
    }

    public static void printList(){
      Node temp = head;
      while(temp != null){
        System.out.print(temp.val + " -> ");
        temp = temp.next;
      }
      System.out.println("null");
    }

    public static Node pop(){
      Node temp = head;
      head = head.next;
      if(temp == max){
        max = temp.oldMax;
      }
      temp.next = null;
      return head;
    }

    public static int max(){
      return max.val;
    }

  }

public static void main(String [] args){
    Node stack = new Node();
    stack.push(1);
    stack.push(4);
    stack.push(2);
    stack.push(19);
    stack.push(14);
    stack.push(24);
    stack.printList();
    System.out.println(stack.max());
    stack.pop();
    stack.printList();
    System.out.println(stack.max());
    stack.pop();
    stack.printList();
    System.out.println(stack.max());
    stack.pop();
    stack.printList();
    System.out.println(stack.max());
  }




}
