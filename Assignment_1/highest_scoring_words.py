import sys

try:
    n = input('Enter between 3 and 10 lowercase letters: ')
    lowercase_str = n.replace(' ', '')
    # 分离字母
    lowercase = list(lowercase_str)
    # 定义捕获异常的函数
    def input_litter(n):
        if ord(n) < 97 or ord(n) > 122:
            raise ValueError
    if len(lowercase) < 3 or len(lowercase) > 10:
        raise ValueError

    else:
        for i in lowercase:
            input_litter(i)

except (ValueError):
    print('Incorrect input, giving up...')
    sys.exit()


# 定义值计算函数
def value(n):
    temp = []
    for i in n:
        if i == 'e' or i == 'i' or i == 's':
            temp.append('1')
        elif i == 'a' or i == 'n' or i == 'r' or i == 't':
            temp.append('2')
        elif i == 'l' or i == 'o':
            temp.append('3')
        elif i == 'c' or i == 'd' or i == 'u':
            temp.append('4')
        elif i == 'b' or i == 'g' or i == 'h' or i == 'm' or i == 'p' or i == 'y':
            temp.append('5')
        elif i == 'f' or i == 'k' or i == 'v' or i == 'w':
            temp.append('6')
        elif i == 'j' or i == 'q' or i == 'x' or i == 'z':
            temp.append('7')
    value = 0
    for i in temp:
        value = int(i) + value

    return value

# 导入txt文件
# 筛选长度小于给定字符长度的word
first_test = []
for i in open(r'/home/wordsEn.txt', 'r'):
    line = i.strip('\n')
    if len(line) <= len(lowercase) and value(line) <= value(lowercase):
        first_test.append(line)
# print(first_test)
# 判断单词是否包含,得到单词子集
from collections import Counter
# 定义判断单词包含的函数
def testWord(word, letter):
    word_2, word_1 = Counter(word), Counter(letter)
    return all(word_2[k] <= word_1.get(k, 0) for k in word_2)

res = []
for i in first_test:
    if testWord(i, lowercase) == True:
        res.append(i)
# print(res)
# 分情况讨论
if res == []:
    print('No word is built from some of those letters.')
else:
    res_value = {}
    for i in res:
        word_value = value(i)
        res_value.update({i: word_value})
    # print(res_value)
    # 找到最大value
    max_value = max(res_value.values())
    # 最大值的结果集
    max_key = []
    for i,j in res_value.items():
        if j == max_value:
            max_key.append(i)
    # print(max_key)
    # 输出结果
    print(f'The highest score is {max_value}.')
    if len(max_key) == 1:
        print(f'The highest scoring word is {max_key[0]}')
    else:
        print('The highest scoring words are, in alphabetical order:')
        for i in max_key:
            print(' ' * 4 + i)
