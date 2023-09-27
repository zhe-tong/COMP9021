# Written by *** for COMP9021
#
# Randomly generates a grid with 0s and 1s, whose dimension is
# controlled by user input, as well as the density of 1s
# in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West)
# and for a given size greater than 1, the number of triangles
# pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1
#   1 1
#     1
#
# The output lists, for every direction and for every size,
# the number of triangles pointing in that direction and of that size,
# provided there is at least one such triangle.
# For a given direction, the possible sizes are listed
# from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles,
# that is, obtained from the latter by ignoring at least one layer,
# starting from the base.


from random import seed, randint
import sys
from collections import defaultdict
import numpy as np


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                              )
              )


try:
    arg_for_seed, density, dim = \
        (int(e) for e in input('Enter three nonnegative integers: ').split())
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print()
# INSERT YOUR CODE HERE
# 找最大三角形用到的最大size为1/2dim
if dim % 2 == 0:
    half_dim = int(dim / 2)
else:
    half_dim = int((dim + 1) / 2)
# 找到有效点集north_point
north_grid_list = []
for i in range(dim):
    for j in range(dim):
        if grid[i][j] != 0:
            grid[i][j] = 1
            north_grid_list.append((i, j))
# print(grid)
north_grid = grid
# print(north_grid_list)

east_grid_list = []
origal = np.array(grid)
east_grid = np.rot90(origal, 1)

south_grid_list = []
south_grid = np.rot90(east_grid, 1)

west_grid_list = []
west_grid = np.rot90(south_grid, 1)

#N方向
north_point = []
for i in range(0, len(north_grid) - 1):
    for j in range(0, len(north_grid) - 1):
        # print((north_grid[i])[j])

        for k in range(2, half_dim + 1):

            temp = []
            for m in range(i, i + k):
                for n in range(j - (m - i), j + (m - i) + 1):
                    if 0 <= m < len(north_grid) and 0 <= n < len(north_grid):
                        if (north_grid[m])[n] == 1:
                            temp.append('-')
            if len(temp) == k ** 2:
                north_point.append(k)
#print(north_point)
north_result = dict()
for i in set(north_point):
    north_result[i] = north_point.count(i)
if len(north_result) != 0:
    print('For triangles pointing N, we have:')

    north_temp = zip(north_result.keys(), north_result.values())
    north_temp_1 = sorted(north_temp, reverse=True)

    if len(north_temp_1) == 1:
        if north_temp_1[0][1] == 1:
            print(f'     {north_temp_1[0][1]} triangle of size {north_temp_1[0][0]}')
        else:
            print(f'     {north_temp_1[0][1]} triangles of size {north_temp_1[0][0]}')
    else:
        if north_temp_1[0][1] == 1:
            print(f'     {north_temp_1[0][1]} triangle of size {north_temp_1[0][0]}')
        else:
            print(f'     {north_temp_1[0][1]} triangles of size {north_temp_1[0][0]}')
        for i in range(1, len(north_temp_1)):
            if int(north_temp_1[i][1])-int(north_temp_1[i-1][1]) == 1:
                print(f'     {int(north_temp_1[i][1]) - int(north_temp_1[i - 1][1])} triangle of size {north_temp_1[i][0]}')
            else:
                print(f'     {int(north_temp_1[i][1])-int(north_temp_1[i-1][1])} triangles of size {north_temp_1[i][0]}')
    print()



#E方向
east_point = []
for i in range(0, len(east_grid) - 1):
    for j in range(0, len(east_grid) - 1):
        # print((north_grid[i])[j])

        for k in range(2, half_dim + 1):

            temp = []
            for m in range(i, i + k):
                for n in range(j - (m - i), j + (m - i) + 1):
                    if 0 <= m < len(east_grid) and 0 <= n < len(east_grid):
                        if (east_grid[m])[n] == 1:
                            temp.append('-')
            if len(temp) == k ** 2:
                east_point.append(k)
#print(north_point)
east_result = dict()
for i in set(east_point):
    east_result[i] = east_point.count(i)
#print(east_result)
if len(east_result) != 0:

    print('For triangles pointing E, we have:')

    east_temp = zip(east_result.keys(), east_result.values())
    east_temp_1 = sorted(east_temp, reverse=True)

    if len(east_temp_1) == 1:
        if east_temp_1[0][1] == 1:
            print(f'     {east_temp_1[0][1]} triangle of size {east_temp_1[0][0]}')
        else:
            print(f'     {east_temp_1[0][1]} triangles of size {east_temp_1[0][0]}')
    else:
        if east_temp_1[0][1] == 1:
            print(f'     {east_temp_1[0][1]} triangle of size {east_temp_1[0][0]}')
        else:
            print(f'     {east_temp_1[0][1]} triangles of size {east_temp_1[0][0]}')
        for i in range(1, len(east_temp_1)):
            if int(east_temp_1[i][1])-int(east_temp_1[i-1][1]) == 1:
                print(f'     {int(east_temp_1[i][1]) - int(east_temp_1[i - 1][1])} triangle of size {east_temp_1[i][0]}')
            else:
                print(f'     {int(east_temp_1[i][1])-int(east_temp_1[i-1][1])} triangles of size {east_temp_1[i][0]}')
    print()

#S方向
south_point = []
for i in range(0, len(south_grid) - 1):
    for j in range(0, len(south_grid) - 1):
        # print((north_grid[i])[j])

        for k in range(2, half_dim + 1):

            temp = []
            for m in range(i, i + k):
                for n in range(j - (m - i), j + (m - i) + 1):
                    if 0 <= m < len(south_grid) and 0 <= n < len(south_grid):
                        if (south_grid[m])[n] == 1:
                            temp.append('-')
            if len(temp) == k ** 2:
                south_point.append(k)
#print(north_point)
south_result = dict()
for i in set(south_point):
    south_result[i] = south_point.count(i)
#print(south_result)
if len(south_result) != 0:

    print('For triangles pointing S, we have:')

    south_temp = zip(south_result.keys(), south_result.values())
    south_temp_1 = sorted(south_temp, reverse=True)

    if len(south_temp_1) == 1:
        if south_temp_1[0][1] == 1:
            print(f'     {south_temp_1[0][1]} triangle of size {south_temp_1[0][0]}')
        else:
            print(f'     {south_temp_1[0][1]} triangles of size {south_temp_1[0][0]}')
    else:
        if south_temp_1[0][1] == 1:
            print(f'     {south_temp_1[0][1]} triangle of size {south_temp_1[0][0]}')
        else:
            print(f'     {south_temp_1[0][1]} triangles of size {south_temp_1[0][0]}')
        for i in range(1, len(south_temp_1)):
            if int(south_temp_1[i][1])-int(south_temp_1[i-1][1]) == 1:
                print(f'     {int(south_temp_1[i][1]) - int(south_temp_1[i - 1][1])} triangle of size {south_temp_1[i][0]}')
            else:
                print(f'     {int(south_temp_1[i][1])-int(south_temp_1[i-1][1])} triangles of size {south_temp_1[i][0]}')
    print()

#W方向
west_point = []
for i in range(0, len(west_grid) - 1):
    for j in range(0, len(west_grid) - 1):
        # print((north_grid[i])[j])

        for k in range(2, half_dim + 1):

            temp = []
            for m in range(i, i + k):
                for n in range(j - (m - i), j + (m - i) + 1):
                    if 0 <= m < len(west_grid) and 0 <= n < len(west_grid):
                        if (west_grid[m])[n] == 1:
                            temp.append('-')
            if len(temp) == k ** 2:
                west_point.append(k)
#print(north_point)
west_result = dict()
for i in set(west_point):
    west_result[i] = west_point.count(i)
#print(west_result)
if len(west_result) != 0:

    print('For triangles pointing W, we have:')

    west_temp = zip(west_result.keys(), west_result.values())
    west_temp_1 = sorted(west_temp, reverse=True)

    if len(west_temp_1) == 1:
        if west_temp_1[0][1] == 1:
            print(f'     {west_temp_1[0][1]} triangle of size {west_temp_1[0][0]}')
        else:
            print(f'     {west_temp_1[0][1]} triangles of size {west_temp_1[0][0]}')

    else:
        if west_temp_1[0][1] == 1:
            print(f'     {west_temp_1[0][1]} triangle of size {west_temp_1[0][0]}')
        else:
            print(f'     {west_temp_1[0][1]} triangles of size {west_temp_1[0][0]}')
        for i in range(1, len(west_temp_1)):
            if int(west_temp_1[i][1])-int(west_temp_1[i-1][1]) == 1:
                print(f'     {int(west_temp_1[i][1]) - int(west_temp_1[i - 1][1])} triangle of size {west_temp_1[i][0]}')
            else:
                print(f'     {int(west_temp_1[i][1])-int(west_temp_1[i-1][1])} triangles of size {west_temp_1[i][0]}')


