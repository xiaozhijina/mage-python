#!/usr/bin/python

#2017-12-11 21:04:00
#第一天 ：打出52张纸牌
'''
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
'''
####################################
## 第一周作业
##用户管理
'''
如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dcit中数据，若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在;
如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印;
如果用户输入list，则打印所有用户信息;
打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
如果用户输入exit，则打印退出程序，并退出 ;

user_dict = {'xiao':(18,123),'xiaozhijian':(26,'17060******5')}
while True:
    opt = input("please input your operation:")
    if opt == "delete":
        user = input('please input user name:')
        try:
            user_dict.pop(user)
        except KeyError as e:
            print('{} user has not exist!'.format(user))
    elif opt == "update":
        u_age = input('please input ”user:age:tel”,with ":" separate.')
        u_info = u_age.split(':')
        u_name = u_info[0]
        u_data = (u_info[1],u_info[2])
        if u_name in user_dict.keys():
            user_dict[u_name] = u_data
        else:
            print('{} user has not exist!'.format(u_name))

    elif opt == "find":
        user = input('please input user name:')
        try:
            print('user name is {}:'.format(user))
            print('{} info is {}:'.format(user,user_dict[user]))
        except KeyError as e:
            print('{} user has not exist!'.format(user))
    elif opt == 'list':
        for u,d in user_dict.items():
            print("user name is:{}".format(u))
            print('user info is:{}'.format(d))
    elif opt == "exit":
        break
    else:
        break
####################################
## 第二周作业

在用户管理功能中添加密码信息:
增、改添加用户密码输入
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序）后将结果输入

def PasswordMange(username):

    user_list = {'xiao':''}
    password = input('please input user password:').strip()
    if username in user_list.keys():
        if user_list[username].strip() != password:
            for i in range(2):
                if i <= 1:
                    p = input("please input password again:").strip()
                    if user_list[username].strip() == p:
                        print("password is good")
                        break
                    else:
                        print("password is mistake,one mone agin!")
                else:
                    exit()
        else:
            print("{} user password is  correct".format(username))
            print("whether  are you set password again!!,now password is: {}".format('*'*len(user_list[username])))
            c = input("please input yes or no:(y/n)").lower()
            if c == "y":
                pw = input("please input new password: ")
                user_list[username] = pw
    else:
        print("{} user don't exist".format(username))
        user_list[username] = ''
        exit()

while True:
    username = input('please input username:')
    PasswordMange(username)
    opt = input("please input your operation:")
    user_dict = {'xiao':(18,123),'xiaozhijian':(26,'17060******5')}
    if opt == "delete":
        user = input('please input user name:')
        try:
            user_dict.pop(user)
        except KeyError as e:
            print('{} user has not exist!'.format(user))
    elif opt == "update":
        u_age = input('please input ”user:age:tel”,with ":" separate.')
        u_info = u_age.split(':')
        u_name = u_info[0]
        u_data = (u_info[1],u_info[2])
        if u_name in user_dict.keys():
            user_dict[u_name] = u_data
        else:
            print('{} user has not exist!'.format(u_name))

    elif opt == "find":
        user = input('please input user name:')
        try:
            print('user name is {}:'.format(user))
            print('{} info is {}:'.format(user,user_dict[user]))
        except KeyError as e:
            print('{} user has not exist!'.format(user))
    elif opt == 'list':
        for u,d in user_dict.items():
            print("user name is:{}".format(u))
            print('user info is:{}'.format(d))
    elif opt == "exit":
        break
    else:
        break
#################################
'''''
###第五周作业
'''
1。实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间；
'''
import datetime
import time

def timeit(fn):
    def _timeit(*args,**kwargs):
        start = datetime.datetime.now()
        print('begin time is {}'.format(start))
        wrapped = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('function run time is {}'.format(delta))
        return wrapped
    return _timeit

@timeit
def fib(nums):
    pre = 0
    cur = 1
    time.sleep(3)
    for i in range(nums):
        pre,cur = cur,pre + cur
        print(cur,end=' ')
    print()

fib(6)
'''
2.实现一个缓存的装饰器：cache装饰器，缓存斐波那契数运行的结果，
先检测要运行的斐波那契数是否在缓存里面，如果在直接返回结果，
否则计算并发结果存在缓存里面，再返回结果。
'''