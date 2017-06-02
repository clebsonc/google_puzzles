# coding=utf-8


class Solution(object):
    def __init__(self):
        pass;
    
    def solution(x, y):
        if (len(x) < len(y)):
            return [i for i in y if i not in x][0]
        return [i for i in x if i not in y][0]

def read_values():
    i = 0
    vector = list()
    value = input()
    value = value.split(" ")
    for v in value:
        vector.append(int(v))
    return vector;

if __name__ == '__main__':
    x = read_values();  # first reads the values for the smaller vector
    y = read_values();  # read the values for the second vector
    
    different = Solution.solution(x, y)
    print (different)

