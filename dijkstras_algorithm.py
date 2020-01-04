#! python3
# ------- an unoptimized imlementation of Dijkstra's algorithm
#-------- Doesnt support graph with multiple edges between two nodes and self-loop

from pprint import pprint

# a,b,c,d,e
# matrix = [
#             [0 ,4 ,8 ,0 ,0],
#             [4 ,0 ,0 ,2 ,0],
#             [8, 0, 0, 1, 7],
#             [0, 2, 1, 0, 0],
#             [0, 0, 7, 0, 0]
# ]

# a,b,c,d,e,z
# matrix = [
#             [0, 4, 2, 0, 0, 0],
#             [4, 0, 1, 5, 0, 0],
#             [2, 1, 0, 8, 10, 0],
#             [0, 5, 8, 0, 2, 6],
#             [0, 0, 10, 2, 0, 3],
#             [0, 0, 0, 6, 3, 0]
# ]

# a,b,c,d,e,f
matrix = [
            [0, 2, 0, 3, 2, 0],
            [2, 0, 2, 4, 0, 0],
            [0, 2, 0, 2, 0, 2],
            [3, 4, 2, 0, 0, 4],
            [2, 0, 0, 0, 0, 3],
            [0, 0, 2, 4, 3, 0]
]
# enumNodes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
# enumNodes = {k:v for k,v in enumerate(['A', 'B', 'C', 'D', 'E'], start=0)}
# enumNodes = {k:v for k,v in enumerate(['A', 'B', 'C', 'D', 'E', 'Z'], start=0)}
enumNodes = {k:v for k,v in enumerate(['A', 'B', 'C', 'D', 'E', 'F'], start=0)}

# enumCols = {0: matrix[0], 1: matrix[1], 2: matrix[2], 3: matrix[3], 4: matrix[4]}
enumCols = {k: v for k, v in enumerate(matrix, start=0)}

# no. of nodes = no. of rows = no. of columns
sTable = [[] for _ in range(len(matrix))]

# first will always be 0 cuz its the starting point.
# Add (no of cols - 1) None aka. infinity
sTable[0] = [0] + [None for _ in range(len(matrix) - 1)]
# pprint(sTable, indent=4, width=40)

counter = 0

def findSmallestNum(row):
    # gotta find a number to initialize the smallest number varaible to compare. cannot do list[0] cuz of None
    smallest = 0
    for n in row:
        if str(n).isdecimal():
            smallest = n
            break

    for elem in row:
        if elem is not None and elem is not False:
            if elem < smallest:
                smallest = elem
    return smallest

def nodeToVisit(row, smallestNum):
    getCol = row.index(smallestNum)
    return enumCols[getCol]

def shortestDistance(matrix):
    lastRow = matrix[len(matrix) - 1]
    for col in lastRow:
        if col is not False:
            sd = col
            break # or return col

    return sd

def findShortestPath(matrix):
    node = []
    i = len(matrix) - 1
    while True:
        currRow = matrix[i]
        currColNum = findSmallestNum(currRow)
        currCol = currRow.index(currColNum)
        node.append(enumNodes[currCol])

        if i <= 0:
            break
        else:
            while True:
                upperRow = matrix[i-1]
                if upperRow[currCol] != currColNum:
                    i = i - 1
                    break
                else:
                    i = i - 1

    return node

def main():
    global counter
    for row in sTable:

        # len-1 because of counter+1 which is because of relation of next row with current visited node
        if counter >= len(sTable)-1:
            break

        u = findSmallestNum(row)
        chosenNode = nodeToVisit(row, u)
        print(f'Smallest element from {row} is {u}. Its corresponding Column is {enumNodes[row.index(u)]}={chosenNode}')
        # discontinue below column
        changeFalse = row.index(u)

        # start weighing next row with current row to decide the weights
        for col, weight in enumerate(chosenNode):
            print(f'Weight value from {enumNodes[row.index(u)]} is {weight}')
            prevWeight = row[col]
            print(f'previous weight was {prevWeight}')
            if weight != 0:
                print(f'{enumNodes[row.index(u)]}={chosenNode} is connected with {enumNodes[col]}={enumCols[col]}')
                if prevWeight == False:
                    print('Appended                                                                    ----------------- False')
                    sTable[counter+1].append(False)
                    # continue # doesnt have effect at this time
                else:
                    if prevWeight == None or u + weight < prevWeight:
                        print(f'compared and found that prevWeight was smaller or had None(was infinite). appended --------- {u+weight}')
                        sTable[counter+1].append(u + weight)
                    else:
                        print(f'new weight was bigger. so sticked with the previous Weight. hence we  appended -------- {prevWeight}')
                        sTable[counter+1].append(prevWeight)
            else:
                print(f'{enumNodes[row.index(u)]}={chosenNode} is not connected with {enumNodes[col]}={enumCols[col]}.appended Previous weight ---------- {prevWeight}')
                sTable[counter+1].append(prevWeight)

        # now get the column that had the smallest number > replace it with False keyword
        del sTable[counter+1][changeFalse]
        sTable[counter+1].insert(changeFalse, False)

        counter += 1

        print()

main()

pprint(sTable, indent=4)
print(f'\nShortest distance to travel from {enumNodes[0]} to {enumNodes[len(enumNodes)-1]} (sd) = {shortestDistance(sTable)}')
print(f'Shortest Path to travel from {enumNodes[0]} to {enumNodes[len(enumNodes)-1]} (sp) = {findShortestPath(sTable)[::-1]}')
print()
