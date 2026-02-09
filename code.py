n = int(input())
grid = [input().strip() for _ in range(n)]
count = 0

for A in range(n):
    # Rotate each row by A positions to the right
    rotated = []
    for row in grid:
        if A == 0:
            rotated_row = row
        else:
            rotated_row = row[-A:] + row[:-A]
        rotated.append(rotated_row)
    
    # Check if the rotated grid is symmetric
    symmetric = True
    for i in range(n):
        for j in range(n):
            if rotated[i][j] != rotated[j][i]:
         