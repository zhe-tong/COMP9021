'''import datetime
start = datetime.datetime.now()'''

while True:
    try:
        rolling_num = input('Enter the desired goal cell number: ')
        if int(rolling_num) <= 0:
            raise ValueError
    except (TypeError):
        print('Incorrect value, try again')
        continue
    except (ValueError):
        print('Incorrect value, try again')
        continue
    else:
        n = int(rolling_num)
        break
# die sum
flag = 7
# beginning suitation
top = 3
front = 2
right = 1
bottom = flag - top
back = flag - front
left = flag - right

# bottom number
on = flag - top

# two kinds of die
#die = {'top': 3, 'front': 2, 'right': 1, 'bottom': 4, 'back': 5, 'left':6}

die_list = [3,4,6,1,2,5]

# the length of step
step = [1, 1, 1]
for i in range(2, 50):
	step.append(i)
	step.append(i)

# changing point
changepoint = []
sum_n = 0
for x in step:
	sum_n += x
	changepoint.append(sum_n)

step.pop(0)
#print(changepoint)

def top( List ):
	List[0], List[4] = List[4], List[0]
	List[1], List[5] = List[5], List[1]
	List[4], List[5] = List[5], List[4]

def bottom( List ):
	List[0], List[4] = List[4], List[0]
	List[1], List[5] = List[5], List[1]
	List[0], List[1] = List[1], List[0]

def right( List ):
	List[0], List[2] = List[2], List[0]
	List[1], List[3] = List[3], List[1]
	List[2], List[3] = List[3], List[2]

def left( List ):
	List[0], List[2] = List[2], List[0]
	List[1], List[3] = List[3], List[1]
	List[0], List[1] = List[1], List[0]

#move元素是移动的步长，切换元素就切换方向
move = []
#n=1特殊处理
'''if n == 1:
    print('On cell 1, 6 is at the top, 2 at the front, and 3 on the right.')'''
#把输入的数字和切换的节点进行比较，然后生成真正的步长，因为1特殊，所以-1处理

trans = 0
for i in range(len(changepoint)):
    if changepoint[i] <= n:
        trans += 1

for i in range(trans-1):
    move.append(step[i])
#把余下的步长也加入到容器中
der = n - changepoint[trans - 1]
move.append(der)
#print(move)

#根据步长进行旋转
turn = 0
for i in range(len(move)):
    if turn == 4:
        turn = 0


    if turn == 0:
        temp = move[i]
        for j in range(temp):
            right(die_list)

    elif turn == 1:
        temp = move[i]
        for j in range(temp):
            bottom(die_list)

    elif turn == 2:
        temp = move[i]
        for j in range(temp):
            left(die_list)

    elif turn == 3:
        temp = move[i]
        for j in range(temp):
            top(die_list)

    turn += 1
print(f'On cell {n}, {die_list[0]} is at the top, {die_list[4]} at the front, and {die_list[3]} on the right.')
#print(die_list)
'''
# 1 2 3 5 7 10
# 1 1 2 2
end = datetime.datetime.now()
print( end - start )'''
