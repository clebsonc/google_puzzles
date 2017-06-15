from fractions import Fraction
from fractions import gcd
from copy import deepcopy
from functools import reduce
import sys


def getProbability(matrix):
    prob = list()
    for r in range(len(matrix)):
        denominator = sum(matrix[r])
        prob.append(list())
        for c in range(len(matrix[r])):
            if denominator == 0:
                prob[r].append(Fraction(0, 1))
            else:
                prob[r].append(Fraction(matrix[r][c], denominator))
    return prob


def getFinalStates(matrix):
    index = [idx for idx in range(0, len(matrix)) if sum(matrix[idx]) == 0]
    return index


def addFinalProbabilityToFinalStates(matrix, final_states):
    for state in final_states:
        matrix[state][state] = Fraction(1, 1)


def printMatrix(matrix):
    for line in matrix:
        for value in line:
            if value.numerator == 0:
                sys.stdout.write("0\t")
            else:
                sys.stdout.write(str(value.numerator)+"/"+str(value.denominator)+"\t")
        sys.stdout.write("\n")


def getSubMatrix(matrix, line_i, line_j, column_i, column_j):
    new_matrix = list()
    i = line_i
    while i <= line_j:
        line = list()
        j = column_i
        while j <= column_j:
            line.append(matrix[i][j])
            j += 1
        new_matrix.append(line)
        i += 1
    return new_matrix


def moveLines(original_matrix, lines):
    matrix = deepcopy(original_matrix)
    line = list()
    um = 0
    for idx in lines:
        line.append(matrix.pop(idx-um))
        um+=1
    for l in line[::-1]:
        matrix.insert(0, l)
    return matrix


def moveColumns(original_matrix, columns):
    matrix = deepcopy(original_matrix)  # copy the matrix
    removed_columns = list()
    sc = 0
    for col_idx in columns:
        col = list()
        for row_idx in range(len(matrix)):
            col.append(matrix[row_idx].pop(col_idx-sc))
        removed_columns.append(col)
        sc += 1
    for cols in removed_columns:
        idx_row = 0
        for value in cols:
            matrix[idx_row].append(value)
            idx_row += 1
    return matrix
            

def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors



def subtractMatrix(A, B):
    matrix = deepcopy(B)
    for ri in range(len(A)):
        for ci in range(len(A)):
            if ri < len(B) and ci < len(B):
                matrix[ri][ci] = A[ri][ci] - B[ri][ci]
    return matrix



def subtractMatrix(A, B):
    matrix = deepcopy(B)
    for ri in range(len(A)):
        for ci in range(len(A)):
            if ri < len(B) and ci < len(B):
                matrix[ri][ci] = A[ri][ci] - B[ri][ci]
    return matrix



def multiplyMatrix(A, B):
    matrix = list()
    try:
        if len(A[0]) != len(B):
            raise ArithmeticError("Number of columns in A differ from the number of lines in B. It must be equal.")
        for line in A:
            new_line = list()
            for col_idx in range(len(B[0])):
                value = Fraction(0, 1)
                for idx_v in range(len(B)):
                    value += line[idx_v] * B[idx_v][col_idx]
                new_line.append(value)
            matrix.append(new_line)
            
    except ArithmeticError as ae:
        print(ae)
    return matrix


def lcm(numbers):
    return reduce(lambda x,y: x*y//gcd(x, y), numbers)


def getIdentityMatrix(size):
    matrix = [[Fraction(0, 1) for x in range(size)] for x in range(size)]
    for idx in range(size):
        matrix[idx][idx] += 1
    return matrix


def answer(m):
    if len(m) == 1:
        return [1, 1]
    a = m
    final_states = getFinalStates(a)
    prob = getProbability(a)
    addFinalProbabilityToFinalStates(prob, final_states)
    matrix = moveLines(prob, final_states)
    intermediary_state = [x for x in range(len(prob)) if x not in final_states]
    matrix = moveColumns(matrix, intermediary_state)

    q = getSubMatrix(matrix, len(final_states), len(matrix)-1, len(final_states), len(matrix)-1)
    identity = getIdentityMatrix(len(q))

    iq = subtractMatrix(identity, q)
    inverse_matrix = getMatrixInverse(iq)

    r = getSubMatrix(matrix, len(final_states), len(matrix)-1, 0, len(final_states)-1)

    probabilities = multiplyMatrix(inverse_matrix, r)
    denominators = [x.denominator for x in probabilities[0]]
    lcm_value = lcm(denominators)
    vector = [int((lcm_value/x.denominator) * x.numerator) for x in probabilities[0]]
    vector.append(lcm_value)
    return vector

