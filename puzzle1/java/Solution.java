package uniqueid;

import java.util.HashSet;

class Solution{
  /**
   * Default Constructor
   * */
  Solution(){}

  /**
   * Copy values of a vector to a HashSet
   * */
  private void emplace(int [] vector, HashSet<Integer> hash){
    for (int value : vector){
      hash.add(value);
    }
  }

  /**
   * Verify if the given HashSet contains the elements in the array
   * */
  private int verify(HashSet<Integer> hash, int[] vector){
    int value = 0;
    for (int i = 0; i < vector.length; i++){
      if (!hash.contains(vector[i])){
        value = vector[i];
        break;
      }
    }
    return value;
  }

  /**
   * Solve the problem of finding the element that is not unique in both vectors
   * return: the value that is not common to both vectors
   * */
  public int solve(int [] x, int [] y){
    HashSet<Integer> hash = new HashSet<Integer>();
    int value=0;
    if (x.length < y.length){
      emplace(x, hash);
      value = verify(hash, y);
    }
    else{
      emplace(y, hash);
      value = verify(hash, x);
    }
    return value;
  }
}

