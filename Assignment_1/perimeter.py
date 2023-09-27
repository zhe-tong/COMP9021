# Insert your code here
#import datetime
#start = datetime.datetime.now()
#读取文件到列表中
fild_name = input('Which data file do you want to use?')
fild_name_set = []
for i in open(fr'/home/{fild_name}', 'r'):
    line = i.strip('\n')
    fild_name_set.append(line)
#print(fild_name_set)

#整理数据

fild_name_set_new = []
for i in fild_name_set:
    n = i.replace(' ', ',')
    fild_name_set_new.append(n)

#print(fild_name_set_new)
# 定义读取文档返回坐标的函数
def readCoordinate(n):
    n = n.split(',', 4)
    x1, y1, x2, y2 = n[0], n[1], n[2], n[3]
    return int(x1), int(y1), int(x2), int(y2)
#print(readCoordinate(fild_name_set_new[0]))

#确定正好涵盖所有矩形的矩形范围
x_range = []
y_range = []
for i in fild_name_set_new:
    temp = readCoordinate(i)
    x_range.append(temp[0])
    x_range.append(temp[2])
    y_range.append(temp[1])
    y_range.append(temp[3])
x_range_temp = x_range
y_range_temp = y_range
x_range = []
y_range = []
#print(x_range_temp)
#print(y_range_temp)
##找到最值
for i in x_range_temp:
    n = int(i)
    x_range.append(n)
for i in y_range_temp:
    n = int(i)
    y_range.append(n)
star_x = min(x_range)
star_y = min(y_range)
end_x = max(x_range)
end_y = max(y_range)
#print(star_x, star_y, end_x, end_y)

#开始循环

#总周长
total = 0
for i in fild_name_set_new:
    temp = readCoordinate(i)
    res_temp = (int(temp[2]) - int(temp[0])) * 2 + (int(temp[3]) - int(temp[1])) * 2
    total = total + res_temp
#print(total)

# 定义判断点数是否在矩形内的函数
def inRange(a, b, c, d, e, f):
    if a > c and a < e and b > d and b < f:
        return 'in'
    elif a == c and b >= d and b <= f:
        return 'on'
    elif a == e and b >= d and b <= f:
        return 'on'
    elif b == d and a >= c and a <= e:
        return 'on'
    elif b == f and a >= c and a <= e:
        return 'on'

point_set = []


for item in fild_name_set_new:
    temp = readCoordinate(item)
    for y in range(temp[1], temp[3] + 1):
        if y == temp[1] or y == temp[3]:
            for x in range(temp[0], temp[2] + 1):
                point_set.append((x, y))
        else:
            point_set.append((temp[0], y))
            point_set.append((temp[2], y))

point_set = set(point_set)
in_line = []
on_line = []
for item in point_set:
    x = item[0]
    y = item[1]
    for i in fild_name_set_new:
        temp = readCoordinate(i)
        l = inRange(x, y, temp[0], temp[1], temp[2], temp[3])
        if l == 'in':
            in_line.append((x, y))
        elif l == 'on':
            on_line.append((x, y))
in_line = set(in_line)
on_line = len(on_line) - len(set(on_line))
result = total - (len(in_line) + on_line)
print(f'The perimeter is: {result}')
#end = datetime.datetime.now()
#print( end - start )


