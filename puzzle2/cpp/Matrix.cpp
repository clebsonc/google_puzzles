#include <vector>
#include <queue>

#include "Node.cpp"

class Matrix{
  private:
    std::vector<std::vector<Node>> board;

    void build_matrix(int board_size){
      int id = 0;
      for (int i=0; i < board_size; i++){
        std::vector<Node> row(board_size);

        for (int j = 0; j < board_size; j++){
          Node n(id);
          n.setVisited(false);
          n.setPredecessor(-1, -1);
          row.at(j) = n;
          id++;
        }
        board.emplace_back(row);
      }
    }

    void initialize(){
      for (int i = 0; i < board.size(); i++){
        for (int j = 0; j < board.at(i).size(); j++){
          board.at(i).at(j).setPredecessor(-1, -1);
          board.at(i).at(j).setVisited(false);
        }
      }
    }

    bool add_valid_neighbor(int row, int column, 
        std::queue<std::pair<int, int>> & q){
      if (row >= 0 && row < board.size() && 
          column >= 0 && column < board.size() && 
          !board.at(row).at(column).isVisited()){
        board.at(row).at(column).setVisited(true);
        q.emplace(std::pair<int, int>(row, column));
        return true;
      }
      return false;
    }

    void emplace_neighbors(const std::pair<int, int> & u, 
        std::queue<std::pair<int, int>> & q){
      if (add_valid_neighbor(u.first-1, u.second-2, q)){
        board.at(u.first-1).at(u.second-2).setPredecessor(u.first, u.second);
        board.at(u.first-1).at(u.second-2).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first-1, u.second+2, q)){
        board.at(u.first-1).at(u.second+2).setPredecessor(u.first, u.second);
        board.at(u.first-1).at(u.second+2).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first-2, u.second-1, q)){
        board.at(u.first-2).at(u.second-1).setPredecessor(u.first, u.second);
        board.at(u.first-2).at(u.second-1).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first-2, u.second+1, q)){
        board.at(u.first-2).at(u.second+1).setPredecessor(u.first, u.second);
        board.at(u.first-2).at(u.second+1).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }


      if (add_valid_neighbor(u.first+1, u.second-2, q)){
        board.at(u.first+1).at(u.second-2).setPredecessor(u.first, u.second);
        board.at(u.first+1).at(u.second-2).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first+1, u.second+2, q)){
        board.at(u.first+1).at(u.second+2).setPredecessor(u.first, u.second);
        board.at(u.first+1).at(u.second+2).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first+2, u.second-1, q)){
        board.at(u.first+2).at(u.second-1).setPredecessor(u.first, u.second);
        board.at(u.first+2).at(u.second-1).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
      if (add_valid_neighbor(u.first+2, u.second+1, q)){
        board.at(u.first+2).at(u.second+1).setPredecessor(u.first, u.second);
        board.at(u.first+2).at(u.second+1).setDistance(board.at(u.first).at(u.second).getDistance()+1);
      }
    }

  public:
    /**
     * Constructor
     * */
    Matrix(int board_size){
      build_matrix(board_size);
    }

    void printMatrix(){
      for (auto l : board){
        for (auto v : l){
          std::cout << v.getPosition() << "\t";
        }
        std::cout << std::endl;
      }
    }
    

    int knightHops(int start, int end){
      int rsource = start / board.size();  // gets the start row
      int csource = start % board.size();  // gets the start column
      std::queue<std::pair<int, int>> q;
      q.emplace(std::pair<int, int>(rsource, csource));

      board.at(rsource).at(csource).setVisited(true);
      board.at(rsource).at(csource).setDistance(0);
      while (!q.empty()){
        std::pair<int, int> u = q.front();
        std::cout << "Visiting: " << board.at(u.first).at(u.second).getPosition();
        std::cout << "\tCount: " << board.at(u.first).at(u.second).getDistance() << std::endl;
        q.pop();
        if (board.at(u.first).at(u.second).getPosition() == end){
          return board.at(u.first).at(u.second).getDistance();
        }
        else{
          emplace_neighbors(u, q);
        }
      }
      return -1;
    }
};

