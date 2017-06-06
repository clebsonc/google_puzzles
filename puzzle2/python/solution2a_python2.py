#coding=utf-8

import sys

class Node:
    def __init__(self, id):
        self.position_id = id;
        self.visited = False;
        self.predecessor_position = [-1, -1]
        self.discovered_distance = 0


class Matrix:
    def __init__(self, size):
        self.board = self.buildBoard(size)


    def buildBoard(self, size):
        board = [[] for i in range(0, size, 1)]
        id = 0
        for idx in range(0, size, 1):
            for values in range(0, size, 1):
                board[idx].append(Node(id))
                id += 1
        return board

    def printBoard(self):
        for line in self.board:
            for value in line:
                sys.stdout.write(str(value.position_id) + "\t")
            sys.stdout.write("\n")

    def knightHops(self, start, end):
        rsource = int(start / len(self.board))
        csource = start % len(self.board)
        queue = list()
        queue.append((rsource, csource))  # append a tuple of index
        self.board[rsource][csource].visited = True
        counter = 0
        while len(queue):
            line, column = queue.pop(0)
            if self.board[line][column].position_id == end:
                counter = self.board[line][column].discovered_distance
                queue = list()
            else:
                self.emplaceNeighbors(line, column, queue)
        return counter

    def emplaceNeighbors(self, line, column, q):
        positions = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
        for i, j in positions:
            if self.add_valid_neighbor(line-i, column-j, q):
                self.board[line-i][column-j].predecessor = [line, column]
                self.board[line-i][column-j].discovered_distance = \
                        self.board[line][column].discovered_distance + 1
        return q;

    def add_valid_neighbor(self, line, column, queue):
        if len(self.board) > line >= 0 and len(self.board) > column >=0 and \
                not self.board[line][column].visited:
            self.board[line][column].visited = True
            queue.append([line, column])
            return True
        return False


if __name__ == "__main__":
    matrix = Matrix(8)
    matrix.printBoard()
    hops = matrix.knightHops(0, 9)
    sys.stdout.write("Hops: "+ str(hops)+"\n")
    
