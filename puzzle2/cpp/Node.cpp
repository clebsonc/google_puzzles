#include <iostream>
#include <utility>

class Node{
  private:
    int position_id;
    bool visited;
    std::pair<int, int> predecessor_position;
    int distance;

  public:
    Node(){}

    Node(int pos){
      this->position_id = pos;
    }
    
    bool isVisited(){
      return visited;
    }

    void setVisited(bool status){
      this->visited = status;
    }

    void setPredecessor(int r, int c){
      this->predecessor_position = std::make_pair(r, c);
    }

    std::pair<int, int> getPredecessor(){
      return this->predecessor_position;
    }

    void setDistance(int d){
      this->distance = d;
    }

    int getDistance(){
      return this->distance;
    }

    int getPosition(){
      return this->position_id;
    }
};

