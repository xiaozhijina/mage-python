#!/usr/bin/python

#2017-12-11 21:04:00
#第一天 ：打出52张纸牌

###  test 1 ############

dict = {}
nums = []

for i in range(1,14):
    if i == 1:
        nums.append('A')
    elif i == 11:
        nums.append('J')
    elif i == 12:
        nums.append('Q')
    elif i == 13:
        nums.append('K')
    else:
        nums.append(i)

dict['黑桃'] = nums
dict['红桃'] = nums
dict['方片'] = nums
dict['梅花'] = nums

for j,k in dict.items():
    print('花色:{} is {}'.format(j,k))

############ test 2 #################
dict1 = {x:'{}'.format(x) for x in range(2,11)}
dict2 = {1:'A',11:'J',12:'Q',13:'K'}
s1 = dict1.copy()
s1.update(dict2)
types = ['红桃','方块','黑桃','梅花']
cards = [(i,k) for i in types for j,k in s1.items()]
for card in cards:
    print(card)
######################################
#第二天： 快速统计字符串每个元素出现的次数： 如"abcevaefegsgdghfdefavbdr"， “a”:x,"b":y
### 方法一###########
strings = "abcevaefegsgdghfdefavbdr"

for i in set(strings):
    print('{}:{}'.format(i,strings.count(i)),end=' ')
print()
##########方法二 #####################
from collections import Counter
print(Counter(strings))
####################方法三 ####################
dict = {}

for i in strings:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
# 第三天： 快速统计字符串每个元素出现的次数： 如"abcevaefegsgdghfdefavbdr"， “a”:x,"b":y，并降序排序，找出前三名。
############ 方法一 ##################
strings = "abcevaefegsgdghfdefavbdr"
dict = {}

for i in strings:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
vob = sorted(dict.items(),key=lambda x:x[-1],reverse=True)
for i in range(3):
    print(vob[i])
############## 方法二 ###########################
strings = "abcevaefegsgdghfdefavbdr"
from collections import Counter
print(Counter(strings).most_common(3))  
