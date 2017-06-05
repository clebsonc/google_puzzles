#include <iostream>

#include "Matrix.cpp"



int main(){
  Matrix matrix(8);
  matrix.printMatrix();
  int hops = matrix.knightHops(0, 1);
  std::cout << "\nHops: " << hops << std::endl;

  return 0;
}

