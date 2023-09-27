# Written by *** for COMP9021
#
# Randomly fills an array of size 10x10 with True and False,
# displayed as 1 and 0, and outputs the number of chess knights
# needed to jump from 1s to 1s and visit all 1s (they can jump back
# to locations previously visited).


from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('    ', ' '.join(str(int(e)) for e in row))


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        n = 1
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
for i in range(dim):
    for j in range(dim):
        if grid[i][j]:
            grid[i][j] = -1
        else:
            grid[i][j] = 0


def step(x, y):
    grid[x][y] = num
    step_8 = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for dx, dy in step_8:
        if 0 <= x + dx < 10 and 0 <= y + dy < 10 and grid[x + dx][y + dy] == -1:
            step(x + dx, y + dy)


num = 0
for i in range(dim):
    for j in range(dim):
        if grid[i][j] == -1:
            num += 1
            step(i, j)

print(num)
