board = [
        ['-', 'T', '-', 'X', '-'],
        ['-', '-', '-', 'T', '-'],
        ['X', '-', '-', '-', 'T'],
        ['-', '-', '-', 'X', '-'],
        ['-', '-', '-', '-', '-']]

for row, col in enumerate(board):
    print(f"row indices: {row} and column: {col}\n")
    for i, val in enumerate(col):
        print(f"col indices: {i} and value of col: {val}")
    print()
    
# tup = (1, 0)
# print(tup[0])

treasures = frozenset({(0,1), (1,3), (2,4)})
print(f"accessing treasure: {[i for i in treasures]}")
for i in treasures:
    print("i: ", i)
    
"""
row indices: 3 and column: ['-', '-', '-', 'X', '-']

col indices: 0 and value of col: -
col indices: 1 and value of col: -
col indices: 2 and value of col: -
col indices: 3 and value of col: X
col indices: 4 and value of col: -

row indices: 4 and column: ['-', '-', '-', '-', '-']

col indices: 0 and value of col: -
col indices: 1 and value of col: -
col indices: 2 and value of col: -
col indices: 3 and value of col: -
col indices: 4 and value of col: -

accessing treasure: [(0, 1), (2, 4), (1, 3)]
i:  (0, 1)
i:  (2, 4)
i:  (1, 3)
"""