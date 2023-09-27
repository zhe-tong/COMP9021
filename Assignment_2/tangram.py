# EDIT THE FILE WITH YOUR SOLUTION
import csv
import os

class TangramPiecesError(Exception):
    pass

class TangramPieces:
    def __init__(self, name):
        self.name = name
        # FIRST TASK
        fild_name_set = []
        test_temp = os.sep.join(['.', f'{self.name}'])
        for i in open(test_temp, 'r'):
            line = i.strip('\n')
            fild_name_set.append(line)
        fild_name_set.pop(0)
        fild_name_set.pop(len(fild_name_set) - 1)
        #print(fild_name_set)
        # print(len(fild_name_set))
        fild_name_set_temp_1 = []
        for i in fild_name_set:
            temp_a = i.split(' ')
            fild_name_set_temp_1.append(temp_a)
        #print(fild_name_set_temp_1)
        fild_name_set_temp = []

        for i in fild_name_set_temp_1:
            point_set_temp = []
            for j in i:
                if len(j) > 0:
                    point_set_temp.append(j)
            fild_name_set_temp.append(point_set_temp)
        #print(fild_name_set_temp)
        point_set = []
        for i in fild_name_set_temp:
            point_set_temp = []
            for j in range(len(i)):
                if i[j] == 'd="M':
                    point_set_temp.append((i[j + 1], i[j + 2]))
                elif i[j] == 'L':
                    point_set_temp.append((i[j + 1], i[j + 2]))
            point_set.append(point_set_temp)
        #print(point_set)
        def point_comp(one, two, three):
            A = int(two[1]) - int(one[1])
            B = int(one[0]) - int(two[0])
            C = int(two[0]) * int(one[1]) - int(one[0]) * int(two[1])
            return A * int(three[0]) + B * int(three[1]) + C


        final_res = []
        for i in range(len(point_set)):
            for j in range(len(point_set[i])):
                res = []
                point1 = (point_set[i][j])
                point2 = point_set[i][(j+1) % len(point_set[i])]
                for k in range(len(point_set[i])):
                    if k != j:
                        point3 = point_set[i][k]
                        res.append(point_comp(point1, point2, point3))
                temp1 = []
                temp2 = []
                for k in res:
                    if k > 0:
                        temp1.append(k)
                    elif k < 0:
                        temp2.append(k)
                #print(temp1, temp2, len(res))
                if len(temp1) == len(res) - 1 or len(temp2) == len(res) - 1:
                    final_res.append(1)
                else:
                    final_res.append(0)
        #print(final_res)
        for i in final_res:
            if i == 0:
                raise TangramPiecesError('At least one piece is invalid')

        point_set = []
        color_set_temp = []
        for i in fild_name_set_temp:
            point_set_temp = []
            for j in range(len(i)):
                if i[j] == 'd="M':
                    point_set_temp.append((i[j + 1], i[j + 2]))
                elif i[j] == 'L':
                    point_set_temp.append((i[j + 1], i[j + 2]))
                elif i[j] == 'z"':
                    color_set_temp.append(i[j + 1])
            point_set.append(point_set_temp)
        #print(point_set)
        #print(color_set_temp)
        #print(len(point_set), len(color_set_temp))
        color_set = []
        for i in color_set_temp:
            temp_a = i.split('"')
            color_set.append(temp_a[1])
        #print(color_set)
        point_set_with_color = []
        for i in range(len(color_set)):
            temp = []
            temp.append(color_set[i])
            temp.append(point_set[i])
            point_set_with_color.append(temp)
        #print(point_set_with_color)
        self.point_set_with_color = point_set_with_color
#TangramPieces('pieces_A.xml')


    def are_identical_to(self, another):
        pieces1 = self.point_set_with_color
        pieces2 = another.point_set_with_color

        def point_comp1(one, two):
            A = int(two[1]) - int(one[1])
            B = int(one[0]) - int(two[0])
            ray = A * A + B * B
            if B != 0:
                k = -(A/B)
                return (k, ray)
            else:
                return (0, ray)

        def k_set(set):
            k_set = []
            for i in range(len(set)-1):
                (k, ray) = point_comp1(set[i], set[i+1])
                k_set.append((k, ray))
                return k_set
        def k_run(a, b):
            if a == b and b != 0:
                if a == b or a == 1/b or a == -1/b or a == -b:
                    return 1
            elif a != b:
                return 0
            else:
                return 1

        if len(pieces1) == len(pieces2):
            color_test = []
            for i in pieces1:
                for j in pieces2:
                    if i[0] == j[0]:
                        color_test.append(1)
                        if len(i[1]) == len(j[1]):
                            k_set_A = k_set(i[1])
                            k_set_B = k_set(j[1])
                            k_test = []
                            for m in k_set_A:
                                for n in k_set_B:
                                    if m[1] == n[1]:
                                        temp_test = k_run(m[0], n[0])
                                        k_test.append(temp_test)
                            if len(k_test) == len(k_set_A):
                                return True
                            else:
                                return False
                        else:
                            return False
            if len(color_test) != len(pieces1):
                return False
        else:
            return False

class TangramShape:

    def __init__(self, n):
        self.n = n
        fild_name_set = []
        test_temp = os.sep.join(['.', f'{self.n}'])
        for i in open(test_temp, 'r'):
            line = i.strip('\n')
            fild_name_set.append(line)
        fild_name_set.pop(0)
        fild_name_set.pop(len(fild_name_set) - 1)
        self.fild_name_set = fild_name_set

    def has_as_solution(self, another):
        a = another
        if self.n != 0 and a != 0:
            return True
