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

# 遍历棋盘为大列表
# print(grid)
grid_str = []
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == False:
            grid_str.append(0)
        else:
            grid_str.append(1)
#print(grid_str)

# 定义找到马脚的函数
num = 6


def step(n):
    grid_str[n] = num
    step_8 = []
    if n % 10 >= 1:
        step_8.append(n - 2 * 10 - 1)
        step_8.append(n + 2 * 10 - 1)
    if n % 10 >= 2:
        step_8.append(n - 10 - 2)
        step_8.append(n + 10 - 2)
    if n % 10 <= 7:
        step_8.append(n - 10 + 2)
        step_8.append(n + 10 + 2)
    if n % 10 <= 8:
        step_8.append(n - 2 * 10 + 1)
        step_8.append(n + 2 * 10 + 1)
    for i in step_8:
        if 0 <= i < 100 and grid_str[i] == 1:
            step(i)


for i in range(len(grid_str)):
    if grid_str[i] == 1:
        step(i)
        num += 1

#print(grid_str)
temp = set(grid_str)
k = len(temp)
print(k)
#print(n)
if k == {0}:
    print('No chess knight has explored this board.')
elif k == 2:
    print(f'At least {k-1} chess knight have explored this board.')
else:
    print(f'At least {k-1} chess knights have explored this board.')