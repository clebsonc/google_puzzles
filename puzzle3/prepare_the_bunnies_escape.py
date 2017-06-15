import sys
from copy import deepcopy




def changeWalls(matrix, current_wall, new_wall):
    for li in range(len(matrix)):
        for ci in range(len(matrix[0])):
            if matrix[li][ci] == current_wall:
                matrix[li][ci] = new_wall



def printMatrix(matrix):
    for line in matrix:
        for value in line:
            sys.write(str(value)+'\t')
        sys.stdout.write("\n")



def verifyPossibleRemoval(matrix, line, column, wall):
    count_free_pass = 0
    if matrix[line][column] == wall:
        for i, j in [(line-1, column), (line+1, column), (line, column-1), (line, column+1)]:
            if  len(matrix) > i >= 0 and len(matrix[0]) > j >=0 and matrix[i][j] == 0:
                count_free_pass += 1
    return (False if count_free_pass < 2 else True)



def getWallsPosition(matrix, wall='x'):
    walls_to_remove = list()
    for li in range(len(matrix)):
        for ci in range(len(matrix[0])):
            if verifyPossibleRemoval(matrix, li, ci, wall):
                walls_to_remove.append((li, ci))
    return walls_to_remove



def add_neighbors(matrix, line, column, q):
    index = [(line-1, column),  (line+1, column), (line, column-1), (line, column+1)]
    for li, ci in index:
        if 0 <= li < len(matrix) and             0 <= ci < len(matrix[0]) and             matrix[li][ci] == 0:  # add the index in the queue
            matrix[li][ci] = matrix[line][column] + 1  # all neighbors will have the same distance
            q.append((li, ci))



def bfs_search(matrix):
    queue = list()
    matrix[0][0] = 1
    queue.append((0, 0))
    while(len(queue) > 0):
        line, column = queue.pop(0)
        add_neighbors(matrix, line, column, queue)
    return matrix[len(matrix)-1][len(matrix[0])-1]



def answer(maze):
    changeWalls(maze, 1, 'x')
    min_dis = sys.maxsize
    positions = getWallsPosition(matrix=maze, wall='x')
    for li, ci in positions:
        matrix = deepcopy(maze)
        matrix[li][ci] = 0
        distance = bfs_search(matrix)
        min_dis = distance if distance < min_dis and distance > 0 else min_dis
        maze[li][ci] = 'x'
    return min_dis


if __name__ == "__main__":
    a = [[0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1], 
            [0, 0, 0, 0, 0, 0]]

    b = [[0, 1, 1, 0],
            [0, 0, 0, 1], 
            [1, 1, 0, 0], 
            [1, 1, 1, 0]]

    c = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(answer(a))
    print(answer(b))
    print(answer(c))


