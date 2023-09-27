# Written by *** for COMP9021

# Prompts the user for 4 positive integers, the last three of which
# represent a number of points (nothing will need to be done if it is 0),
# an integer max_coordinate such that all coordinates to be generated
# will be between -max_coordinate and max_coordinate included, and a
# square window size (width and height).
#
# Generates a list of x coordinates and a list of y coordinates of common
# length the number of points requested. Shows these lists, possibly truncated.
#
# x-coordinates increase from left to right,
# y-coordinates increase from bottom to top.
#
# 1. Displays the points, without duplicates, from highest to lowest,
#    and from left to right for a given height.
#
# 2. Displays the size of the smallest rectangle, as well as its top left
#    and bottom right corners, in which all points fit.
#
# 3. Displays the maximum number of points that can fit in a square window
#    with the provided size. The window has to be fully included in the
#    enclosing rectangle. In case such a window exists, then displays the
#    top left and bottom right corners of the leftmost, topmost such window.


from random import seed, randrange
import sys

try:
    for_seed, nb_of_points, max_coordinate, window_size =\
            (int(e) for e in input('Enter four positive integers: ').split())
    if for_seed < 0 or nb_of_points < 0 or max_coordinate < 0\
       or window_size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not nb_of_points:
    print('No point to play with, see you later!')
    sys.exit()
seed(for_seed)
x_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                     for _ in range(nb_of_points)
                ]
y_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                     for _ in range(nb_of_points)
                ]
field_width = max(max(len(str(e)) for e in x_coordinates),
                  max(len(str(e)) for e in y_coordinates)
                 )
print('Here is how the x-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in x_coordinates)
                [: 80 // (field_width + 1) * (field_width + 1)]
     )
print('Here is how the y-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in y_coordinates)
                [: 80 // (field_width + 1) * (field_width + 1)]
     )

# INSERT CODE HERE
#
print()
print('Here are the points, without duplicates, from highest to lowest,')
print(' and from left to right for a given height:')

list_xy = [(m, n)for m, n in zip(x_coordinates, y_coordinates)]

tuple_temp_test = set(list_xy)
tuple_temp = sorted(tuple_temp_test,
      key = lambda x : (-x[1], x[0])
      )


#print(tuple_temp)
for j in tuple_temp:
    print(f'  {j}')
#
#
print()
test_y = list(set(y_coordinates))
test_x = list(set(x_coordinates))
test_y.sort(reverse=True)
test_x.sort(reverse=True)
length_y = test_y[0] - test_y[len(test_y) - 1]
length_x = test_x[0] - test_x[len(test_x) - 1]
size = length_y * length_x
top_corner = (test_x[len(test_x) - 1], test_y[0])
bottom_corner = (test_x[0], test_y[len(test_y) - 1])
print(f'All points fit in a rectangle of size {size},')
print(f' with {top_corner} as top left corner, and')
print(f' with {bottom_corner} as bottom right corner.')
print()
# 先满足规定size正方形包含最多的点
# 如果有多个正方形，取最左上的正方形
from collections import Counter
if window_size > length_x or window_size > length_y:
    print(f'The maximum number of points that fit in a square window of size {window_size}')
    print(' enclosed within the rectangle is 0.')
elif tuple_temp == [(0, 0)]:
    print(f'The maximum number of points that fit in a square window of size {window_size}')
    print(f' enclosed within the rectangle is 1.')
    print('The leftmost, topmost such window has (0, 0) as top left corner,')
    print(' and (0, 0) as bottom right corner.')
else:
    print(f'The maximum number of points that fit in a square window of size {window_size}')
    box_1 = []
    for k in range(int(top_corner[1]), int(bottom_corner[1]) + 1 - window_size, -1):
        for i in range(int(top_corner[0]), int(bottom_corner[0]) + 1 - window_size):
            for j in tuple_temp:
                if (i <= j[0] and j[0] <= i + window_size) and (k - window_size <= j[1] and j[1] <= k):
                    box = (i, k)
                    box_1.append(box)
    count_box = {}
    for i in box_1:
        if count_box.get(i) == None:
            count_box[i] = 1
        else:
            count_box[i] += 1
    key_point_box = []
    key_point = ()
    key_values = 0
    for i, j in count_box.items():
        if j == max(count_box.values()):
            key_values = j
            key_point_box.append(i)
    key_point_box_test = sorted(key_point_box,
                        key=lambda x: (-x[1], x[0])
                        )
    key_point = key_point_box_test[0]


    final_point = (key_point[0] + window_size, key_point[1] - window_size)
    print(f' enclosed within the rectangle is {key_values}.')
    print(f'The leftmost, topmost such window has {key_point} as top left corner,')
    print(f' and {final_point} as bottom right corner.')


