/**
 * 
 * Design a stack with a push, pop, and max function
 * which returns the max value in the stack, all of
 * which are run in O(1) time.
 */

public class Stack {
    public class Node {
        private int val;
        private Node next;
        private Node oldMax;


    }
    
    private Node stack;
    private Node max;

    public Stack() {}

    public void push(int x) {
        Node n = new Node();
        n.val = x;

        if (stack == null) {
            stack = n;
        } else {
            n.next = stack;
            stack = n;
        }

        if (max == null || n.val > max.val) {
            n.oldMax = max;
            max = n;
        }

    }

    public int pop() {
        if (stack == null) {
            throw new NullPointerException("Its Null bro");
        }

        Node n = stack;
        stack = stack.next;

        if (n.oldMax != null) {
            max = n.oldMax;
        }

        return n.val;
    }

    public int max() {
        if (max == null) {
            throw new NullPointerException("Its Null bro");
        }
        return max.val;
    }

    public void print() {
        if (stack == null) {
            throw new NullPointerException("Its Null bro");
        }
        Node n = stack;

        while(n != null) {
            System.out.println(n.val);
            n = n.next;
        }
    }


    public static void main(String[] args) {
        Stack myStack = new Stack();

        myStack.push(2);
        myStack.push(6);
        myStack.push(3);
        myStack.push(16);
        myStack.push(8);
        myStack.push(9);
        myStack.push(1);
        myStack.push(2);
        myStack.push(22);
        System.out.println("Max is -> " + myStack.max());
        myStack.print();
        myStack.pop();
        System.out.println("Max is -> " + myStack.max());

    }

}


