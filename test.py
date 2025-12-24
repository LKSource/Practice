def detonate(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [['O'] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'O':
                result[i][j] = '.'
                if i > 0: result[i-1][j] = '.'
                if i < rows - 1: result[i+1][j] = '.'
                if j > 0: result[i][j-1] = '.'
                if j < cols - 1: result[i][j+1] = '.'
    return [''.join(row) for row in result]

def bomberMan(n, grid):
    if n == 1:
        return grid
    full = ['O' * len(grid[0]) for _ in range(len(grid))]
    if n % 2 == 0:
        return full
    s3 = detonate(grid)
    if n % 4 == 3:
        return s3
    else:
        return detonate(s3)
    
grid =['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
#grid = ['.......','...O.O.','....O..','..O....','OO...OO','OO.O...']
n = 3
result = bomberMan(n,grid)
print(result)