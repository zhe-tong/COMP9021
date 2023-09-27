# Written by *** for COMP9021
#
# Given a sequence L of numbers, the greedy increasing subsequence of L,
# say G, is inductively defined as follows:
# - If L is of length at most 1 then G is L.
# - If L is of the form (e_0, e_1, ..., e_n) with n >= 1, then:
#   - either e_1 is greater than e_0, in which case G is e_0 followed by the
#     greedy increasing subsequence of (e_1, ..., e_n),
#   - or e_1 is less than or equal to e_0, in which case G is the greedy
#     increasing subsequence of (e_0, e_2,..., e_n).
#
# 1. Generates a random list L of digits whose length is chosen by the user
#    (done).
# 2. Displays L (done),
# 3. Displays the integer made from these digits (without the leading 0s,
#    if any).
# 4. Graphically displays the greedy increasing subsequence of L as
#    horizontal bars.
# 5. Graphically displays the nonzero values in L as steps.


from random import seed, randrange
import sys


try: 
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(10) for _ in range(length)]
print('Here are the generated digits:', values)
# INSERT CODE HERE:
str_values = ""
for i in values:
    str_values = str_values + str(i)
#print(str_values)
#print(type(str_values))
int_values = int(str_values)
print()
print('The integer made from these digits is:', int_values)
#print(type(int_values))
print()
print('Here is the greedy increasing subsequence of values, '
      'horizontally displayed:'
     )
print()
# INSERT CODE HERE:
def greedy(values):
    head = values[0]
    res = []
    sign = '-'
    if values[0] != 0:
        res.append(sign * values[0])
    for i in range(1, len(values)):
        if head < values[i]:
            res.append(sign * values[i])
            head = values[i]
        return res
for s in greedy(values):
	print(' ' * 4 + s)
print()
#print(values)
print('Here are the nonzero values, displayed as stairs:')
# INSERT CODE HERE:
print()
def nonzero(values):
    temp = 5
    res = []
    sign1 = ' '
    sign2 = '-'
    #res.append(sign2 * values[0])
    for j in range(len(values)):
        if values[j] != 0:
            res.append(sign1 * temp + sign2 * values[j])
            temp = temp + values[j]
    return res


for k in nonzero(values):
    print(k)
print()