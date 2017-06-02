package uniqueid;

import java.util.Scanner;


class Test{
  public static Scanner reader  = new Scanner(System.in);

  static void readValues(int t, int[] vector){
    for(int i = 0; i < t; i++){
      int value = reader.nextInt();
      vector[i] = value;
    }
  }

  static void printValues(int[] vector){
    for(int i = 0; i < vector.length; i++){
      System.out.print(vector[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args){
    int t=0;
    t = reader.nextInt();

    int [] x = new int[t];  // allocate array of t values
    int [] y = new int[t+1];

    readValues(t, x);
    readValues(t+1, y);

    printValues(x);
    printValues(y);
    
    Solution solution = new Solution();
    int different = solution.solve(x, y);
    System.out.println(different);
  }
}

