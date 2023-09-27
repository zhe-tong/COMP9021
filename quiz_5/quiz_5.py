# Uses data available at http://data.worldbank.org/indicator
# on Forest area (% of land area) and Agricultural land area (% of land area).
#
# Prompts the user for two distinct years between 1960 and 2020,
# separated by two consecutive hyphens with possibly spaces before
# and after, as well as a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area (as a ratio) has strictly increased from
#   oldest input year to most recent input year;
# - forest area (as a ratio) has strictly increased from oldest input
#   year to most recent input year;
# - the ratio of increase in agricultural land area to
#   increase in forest area (so a ratio of ratio differences)
#   determines output order.
#
# Countries are output from those whose ratio of increases is largest
# to those whose ratio of increases is smallest, as a floating point
# number with 2 digits after the decimal point.
#
# In the unlikely case where many countries share the same ratio
# of increases, countries are output in lexicographic order.
#
# In case fewer than N countries are found, only that number of
# countries is output.
#
# If no country has data for both years, then a special message is output.
#
# The data directory is stored in the working directory.


from collections import defaultdict
import csv
import os
from pathlib import Path
import sys


# INSERT YOUR CODE HERE
# 输入数据，中间必须是两个杠，可以有空格，年份必须在要求的之间，顺序不重要

import sys
# 第一个数据输入
try:
    n = input('Input two distinct years in the range 1960 -- 2020: ')
    year = n.replace(' ', '')
    year_set = year.split('--')
    year = list(year)
    if len(year_set) != 2:
        raise ValueError
    elif len(year) != 10:
        raise ValueError
    elif int(year_set[0]) < 1960 or int(year_set[0]) > 2020:
        raise ValueError
    elif int(year_set[1]) < 1960 or int(year_set[1]) > 2020:
        raise ValueError
    elif int(year_set[0]) == int(year_set[1]):
        raise ValueError
except (ValueError):
    print('Not a valid range of years, giving up...')
    sys.exit()
except (TypeError):
    print('Not a valid range of years, giving up...')
    sys.exit()

#print(year_set)
# 得到两个年份
if year_set[0] > year_set[1]:
    year1 = int(year_set[1])
    year2 = int(year_set[0])
else:
    year1 = int(year_set[0])
    year2 = int(year_set[1])
#print(year1, year2)
# 输入数据int是正整数
try:
    num = input('Input a strictly positive integer: ')
    if int(num) <= 0:
        raise ValueError
except (ValueError):
    sys.exit()
except (TypeError):
    sys.exit()
#print(num)
num = int(num)

#导入森林文件,1960年对应4号元素 = year - 1956
frst_temp = os.sep.join(['.', 'Areas', 'Forest', 'API_AG.LND.FRST.ZS_DS2_en_csv_v2_2125884.csv'])
frst_reader = csv.reader(open(frst_temp))
temp_frst = 0
frst_different_set = {}
for item in frst_reader:
    if temp_frst < 5:
        temp_frst += 1
    else:
        if item[year1 - 1956] != '' and item[year2 - 1956] != '':
            country = item[0]
            small_year = float(item[year1 - 1956])
            big_year = float(item[year2 - 1956])
            frst_difference = big_year - small_year
            frst_different_set.update({country: frst_difference})
#print(frst_different_set)
#导入农业文件
agri_temp = os.sep.join(['.', 'Areas', 'Agricultural Land', 'API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2056230.csv'])
agri_reader = csv.reader(open(agri_temp))
temp_agri = 0
agri_different_set = {}
for item in agri_reader:
    if temp_agri < 5:
        temp_agri += 1
    else:
        if item[year1 - 1956] != '' and item[year2 - 1956] != '':
            country = item[0]
            small_year = float(item[year1 - 1956])
            big_year = float(item[year2 - 1956])
            agri_difference = big_year - small_year
            agri_different_set.update({country: agri_difference})
#print(agri_different_set)

#得到商差值字典
res = {}
for i in frst_different_set.keys():
    if i in agri_different_set:
        if float(frst_different_set[i]) > 0 and float(agri_different_set[i]) > 0:
            a = float(agri_different_set[i]) / float(frst_different_set[i])
            #a = f'{a: .2f}'
            res.update({i: a})
#print(res)


#降序排列res
res = sorted(res.items(), key = lambda value: (value[1], value[0]), reverse=True)
#print(res)
country_print_list = []
num_print_list = []
for i in range(len(res)):
    if i < num:
        a = res[i]
        country_print_list.append(a[0])
        num_print_list.append(a[1])
#print(country_print_list)
#print(num_print_list)
if res == []:
    print('I do not have data for any country for at least one of those years.')
else:
    print(f'Here are the top {num} countries or categories where, between {year1} and {year2},')
    print('  the ratios of agricultural land area and forest area')
    print('  (over total land) have both strictly increased,')
    print('  listed from the countries where the ratio of increases')
    print('  is largest, to those where it is smallest:')
    for i in range(len(country_print_list)):
        print(f'{country_print_list[i]} ('f'{num_print_list[i]:.2f}'')')
'''temp = 0
for key, value in res.items():
    temp += 1
    if temp > num:
        break
    print("{}:{}".format(key, value))'''