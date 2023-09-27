# Written by *** for COMP9021

# Prompts the user for two integers.
# - The first one should be between 1 and 4, with
#   * 1 meaning initially looking North,
#   * 2 meaning initially looking East,
#   * 3 meaning initially looking South,
#   * 4 meaning initially looking West.
# - The second one should be positive. When written in base 3, its consecutive
#   digits read from left to right represent the directions to take, with
#   * 0 meaning going in the direction one is initially looking at,
#   * 1 meaning 45 degrees left of the direction one is initially looking at,
#   * 2 meaning 45 degrees right of the direction one is initially looking at.
#
# Prints out:
# - the direction one is originally looking at, as an arrow,
# - the representation of the second digit in base 3,
# - the corresponding sequence of directions to take, as arrows,
# - in case one is originally looking North or South, the path,
#   so the sequence of arrows again, but nicely displayed.


import sys

try:
    initial_direction, directions = input('Enter an integer between 1 and 4 '
                                          'and a positive integer: '
                                          ).split()
    if len(initial_direction) != 1 \
            or len(directions) > 1 and directions[0] == '0':
        raise ValueError
    initial_direction = int(initial_direction)
    directions = int(directions)
    if initial_direction not in {1, 2, 3, 4} or directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print()

# INSERT YOUR CODE HERE
# first direction
if int(initial_direction) == 1:
    print('Ok, you want to first look this way:', chr(8679))
elif int(initial_direction) == 2:
    print('Ok, you want to first look this way:', chr(8680))
elif int(initial_direction) == 3:
    print('Ok, you want to first look this way:', chr(8681))
elif int(initial_direction) == 4:
    print('Ok, you want to first look this way:', chr(8678))
print()

# 10 to 3
n = int(directions)
temp = []
if n < 3:
    temp.append(n % 3)
else:
    while n >= 3:
        temp.append(n % 3)
        n = n // 3
        if n < 3:
            temp.append(n % 3)
            break
res = temp
for i in range(len(res) // 2):
    res[i], res[-(i + 1)] = res[-(i + 1)], res[i]
A = ''.join('%s' % n for n in res)
C = int(A)
print('In base 3, the second input reads as:', C)

# step
temp1 = []
if C == 0:
    B = [0]
else:
    while (C >= 1):
        temp1.append(C % 10)
        C = C // 10
    B = list(reversed(temp1))


def north():
    for k in range(len(B)):
        if B[k] == 1:
            print(chr(11009), end='')
        elif B[k] == 2:
            print(chr(11008), end='')
        elif B[k] == 0:
            print(chr(8679), end='')


def east():
    for k in range(len(B)):
        if B[k] == 1:
            print(chr(11008), end='')
        elif B[k] == 2:
            print(chr(11010), end='')
        elif B[k] == 0:
            print(chr(8680), end='')


def south():
    for k in range(len(B)):
        if B[k] == 1:
            print(chr(11010), end='')
        elif B[k] == 2:
            print(chr(11011), end='')
        elif B[k] == 0:
            print(chr(8681), end='')


def west():
    for k in range(len(B)):
        if B[k] == 1:
            print(chr(11011), end='')
        elif B[k] == 2:
            print(chr(11009), end='')
        elif B[k] == 0:
            print(chr(8678), end='')


print("So that's how you want to go:  ", end='')

if int(initial_direction) == 1:
    north()
elif int(initial_direction) == 2:
    east()
elif int(initial_direction) == 3:
    south()
elif int(initial_direction) == 4:
    west()
print()

# let's go

if int(initial_direction) == 2 or int(initial_direction) == 4:
    print()
    print("I don't want to have the sun in my eyes, but by all means have a go at it!")
# go south
elif int(initial_direction) == 3:
    print()
    print("Let's go then!")


    def south_1(k):
        if k == 1:
            return chr(11010)
        elif k == 2:
            return chr(11011)
        elif k == 0:
            return chr(8681)


    # go_south_test
    temp2 = []
    test_b = 0
    for test_a in range(len(B)):
        if B[test_a] == 1:
            test_b = test_b + 1
            temp2.append(test_b)
        elif B[test_a] == 0:
            test_b = test_b
            temp2.append(test_b)
        elif B[test_a] == 2:
            test_b = test_b - 1
            temp2.append(test_b)
    min_b = int(min(temp2))
    # print(' ' * , south_1())
    if min_b < 0:
        space_num = 0 - min_b
    else:
        space_num = min_b
    for w in range(len(B)):
        if B[w] == 1:
            space_num = space_num + 1
            print(' ' * space_num + south_1(B[w]))

        elif B[w] == 0:
            print(' ' * space_num + south_1(B[w]))
        elif B[w] == 2:
            space_num = space_num - 1
            print(' ' * space_num + south_1(B[w]))

# go_north
elif int(initial_direction) == 1:
    print()
    B = list(reversed(B))
    print("Let's go then!")


    def north_1(p):
        if p == 1:
            return chr(11009)
        elif p == 2:
            return chr(11008)
        elif p == 0:
            return chr(8679)


    # go_north_test
    temp2 = []
    test_b = 0
    for test_a in range(len(B)):
        if B[test_a] == 1:

            temp2.append(test_b)
            test_b = test_b + 1
        elif B[test_a] == 0:
            test_b = test_b
            temp2.append(test_b)
        elif B[test_a] == 2:

            temp2.append(test_b)
            test_b = test_b - 1
    min_b = int(min(temp2))
    # print(' ' * + north_1())
    if min_b < 0:
        space_num = 0 - min_b
    else:
        space_num = min_b
    for w in range(len(B)):
        if B[w] == 1:
            print(' ' * space_num + north_1(B[w]))
            space_num = space_num + 1
        elif B[w] == 0:
            print(' ' * space_num + north_1(B[w]))
        elif B[w] == 2:
            print(' ' * space_num + north_1(B[w]))
            space_num = space_num - 1


