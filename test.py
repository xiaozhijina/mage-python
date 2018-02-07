#coding:utf8

'''
for i in range(10):
    if not i % 2 ==0 :
        continue
    print(i)
for j in range(10,-1,-2):
    print(j)

count = 0
for i in range(1,1001):
    if i % 7 == 0:
        print(i)
        count += 1
        if count >= 20:
            break
    val = input('>>>')
val = int(val)
print(val)
if val >= 1000: # 􀜑􀔡
if val>=10000:
num = 5
else:
num = 4
else:
if val>=100:
num = 3
elif val >= 10:
num = 2
else:
num = 1
print(num)
pre = 0
for i in range(num,0,-1):
cur = val//(10**(i-1))
print(cur - pre*10)
pre = cur # 􀬐􀟄􀡚􀟄􀒿􀑕􀞾􀗱􀤙􀞐􀚔􀛸􀔭􀍾􀗲􀟧􀮬􀡌􀞩􀑒􀐅􀑹􀓱􀐗􀑹􀛸􀔭􂪢􀍾
            '''
'''
data = input('please input five digit:')
#if a.isdigit():
#    data=int(a)
print(len(data))
for i in data:
    print(i)
if int(data) >=100000:
        print('number is too big')
else:
        if int(data) >= 1000:
            if int(data) >=10000:
                print('five number')
                print('万位:'  + data[0])
                print('qianwei:' + data[1])
                print('baiwei:' + data[2])
                print('shiwei:' + data[3])
                print('gewei:' + data[4])
            else:
                print('four number')
        else:
            if int(data) >= 100:
                print(3)
            elif int(data) >= 10:
                print(2)
            else:
                print(1)
'''
'''
num = int(input('<<<<<<'))
for i in range(num):
    print(' * '*num)

sum = 0
for j in range(100)::
    if not j % 2 == 0:
       sum = sum + j
print(sum)
count = 0
for i in range(1,6):
    count += i**2
print(count)

num = int(input('<<<<<<'))

if num//1 == num and num // num == 1 and num % 2 != 0:
    print('zishu')
else:
    print('feizishu')
num = int(input('<<<<<<'))
while True:
    for i in range(1,num):
        if i == 1 or i == num - 1:
            print('*\t' * (num - 1) )
        else:
            print('*' + '\t'*(num - 2) +  '*')
    if i == num - 1:
        break
x = 1
sum = 0
for i in range(1,6):
    x *= i
    sum += x
print(sum)

num = int(input('input one number:'))

for j in range(2,num):
    if num % j == 0:
        print('is not prime')
        break
else:
    print('is prime')
'''
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) , 'x' , str(i) , '=' , str(i*j) ,end='\t')
    print()
'''
'''
for i in range(1,8):
    if i % 2 != 0:
        print('*' * i)
for j in range(5,0,-1):
    if j % 2 !=0:
        print('*' * j)
'''
'''
for n  in range(1,101):
    k = 1
    if n >= 2:
        print(1)
    else:
        k = 1/5^-2[((1+5^-2)/2)^n - ((1-5^-2)/2)^n]
        print(k)
count = 0
sum = 0
while True:
    a = input('>>>>')
    if a == 'quit':
        break
    count += 1
    sum += int(a)
    print('avg:',sum/count)
for i in range(1,10):
    for j in range(1,10):
        if j < i:
            print(' '* 11,end=' ')
        else:
#            print(str(i) , 'x' , str(j) , '=' , str(i*j) ,end='\t')
            print('{0} * {1} = {2}'.format(i,j,i*j),end='\t')
    print()

for i in range(-3,4):
    if i < 0:
        prespace = -i
    else:
        prespace = i
    print(' '*prespace + '*'*(7-prespace*2))

for j in range(-3,4):
    if j < 0:
        prespace = -j
        print(' '*prespace + '*'*(4-prespace))
    elif j == 0:
        print('*'*7)
    else:
        prespace = j
        print(' '*3 + '*'*(4-prespace))
print(0,end=' ')
print(1,end=' ')
a = 0
b = 1
while True:
    c = a + b
    if c > 100:
        break
    a = b
    b = c
    print(c,end=' ')

a = 1
b = 1
index = 2
while True:
    c = a + b
    a = b
    b = c
    index += 1
    if index == 101:
        break
print('{0},{1}'.format(index,c))

import _datetime
start = _datetime.datetime.now()
for x in range(2,10000):
    for i in range(2,int(x ** 0.5)+1):
        if x % i == 0:
            break
    else:
        print(x)
end = _datetime.datetime.now()
print(end - start)

peach = 1
for i in range(9):
    peach = 2*(peach+1)
print

num_list = []
for i in range(3):
    num = int(input(">>>>"))
    num_list.append(num)
print(max(num_list))
print(sorted(num_list))

num_list = [
    [1,9,8,5,6,7,4,3,2],
    [1,2,3,4,5,6,7,8,9]
]
nums = num_list[0]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    flag = False
    for j in range(length - i - 1):
        count += 1
        if  nums[j] < nums[j + 1]:
            tmp = nums[j]
            nums[j] =  nums[j + 1]
            nums[j + 1]  = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums,count_swap,count)
s1 = "I'm \ta super student."
print(s1.split())
print(s1.split('s'))
print(s1.split('super'))
print(s1.split('super '))
print(s1.split(' '))
print(s1.split(' ',maxsplit=2))
print(s1.split('\t',maxsplit=2))
print('dfajdk\r')
s2 = """I'm a super student.
#You're a super teacher."""
print(s2)
print(s2.splitlines())
print(s2.splitlines(True))
s3 = "I'm a super student."
print(s3.partition('s'))
print(s3.partition('stu'))

triangle = [[1]]
n = 6
for i in range(1 ,n):
    pre = triangle[i - 1]
    cur = [1]
    for j in range(0,i-1):
        cur.append(pre[j] + pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)
prime = [2,]
for i in range(3,100):
    for j in prime:
        if i % j == 0:
            break
    else:
        prime.append(i)
print(prime)
'''
################# 求素数的改进版  ###################
'''
import  math
prime = []
for i in range(2,100):
    for j in range(2,math.ceil(math.sqrt(i))):
        if i % j == 0:
            break
    else:
        prime.append(i)
print(prime)
primenumber = []
flag = False
for x in range(2,10000):
    for k in primenumber:
        if x % k == 0:
            flag = True
            break
        if k >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        primenumber.append(x)
print(primenumber)
'''
################  求杨辉三角前6行 #######################
############ 方法一 ####################
'''
triangle = [[1],[1,1]]
for i in range(2,6):
    pre = triangle[i-1]
    cur = [1]
    for j in range(0,i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)
'''
################# 方法二 ##################################
'''
triganle = []
for i in range(6):
    row = [1]
    triganle.append(row)
    if i == 0:
        continue
    for j in range(i-1):
        row.append(triganle[i-1][j] + triganle[i-1][j+1])
    row.append(1)
print(triganle)
'''
################# 方法三 #################################
'''
n = 6
oldline = []
newline = [1]
length = 0
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1] + oldline[j])
    print(newline)
'''
############  方法四  ############################
'''
triganle = []
n = 6
for i in range(n):
    row = [1]   #开始的1
    for k in range(i):  ##中间填0，尾部填1
        row.append(1) if k == i-1 else row.append(0)
    triganle.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1):  ###n =3才能进来
        val = triganle[i -1 ][j - 1] + triganle[i -1 ][j]
        row[j] = val
        if j != i - j:   ###奇数个数的中点跳过
            row[-j-1] = val
print(triganle)
'''
####################　方法四-变形 #####################
'''
triangle = []
n = 6
for i in range(n):
    row = [1]*(i+1)
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1): # n=3才能进来􀨈􀬒􀟛
        val = triangle[i - 1][j-1] + triangle[i - 1][j]
        row[j] = val
        if i != 2j:   #奇数个数的中点跳过?􀞃􀐗􀞃􀤙􀐘􀢵􀫩􀬋
            row[-j-1] = val
print(triangle)
'''
################## 冒泡法 #####################################
'''
num_list = [
    [111,92,8,15,63,7,44,31,20],
    [1,2,3,4,5,6,7,8,9]
]
nums  = num_list[0]
print(nums)
length = len(nums)
count = 0
count_swap = 0
for i in range(length):
    flag = False
    for j in range(length - i -1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums,count,count_swap)
'''
#############################
'''
nums = []
for i in range(5):
    num = int(input(">>>>>>"))
    nums.append(num)
print(nums)
print(len(nums))
for j in range(5):
    flag = False
    for k in range(5 - j -1):
 #       print(nums[k])
        if nums[k] > nums[k+1]:
            tmp = nums[k]
            nums[k] = nums[k+1]
            nums[k+1] = tmp
            flag = True
    if not flag:
        break
print(nums)
'''''
#################################################
############ 打印数字的位数 #########################
'''
num = input('>>>>>>>>').strip().lstrip('0')
if not num.isdigit:
    print('please input number:')
else:
    print('have many digits {}'.format(len(num)))
#    for i in range(len(num)):
#            print("{}'s count {}".format(num[i],num.count(num[i])))
##### 数字出现的个数。
    count = [0]*10

    for j in range(10):
        count[j] = num.count(str(j))
        if count[j]:
            print(j,count[j])
######## 倒叙打印1
for k in range(len(num),0,-1):
    print(num[k-1],end=' ')
print()
######## 倒序打印 2
for i in reversed(num):
    print(i,end=' ')
print()
'''
###############################################
'''
n = 11
m = 4
triganle = []
for i in range(n):
    row = [1]
    triganle.append(row)
    if i == 0:
        continue
    for j in range(i - 1):
        row.append(triganle[i-1][j]+triganle[i-1][j+1])
    row.append(1)
print(triganle)
print(triganle[n-1][m-1])
'''
######### 矩阵倒置 ############
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
for i in range(len(tm)):
    for j in range(len(matrix)):
        tm[i][j] = matrix[j][i]
print(matrix)
print(tm)
'''
'''
matrix = [[1,2],[3,4],[5,6],[7,8]]
tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
for i in range(len(tm)):
    for j in range(len(matrix)):
        tm[i][j] = matrix[j][i]
print(tm)
##############################################
import random
s1 = set()
s2 = set()
for _ in range(10):
    a = random.randrange(10,21)
    b = random.randrange(10,21)
    s1.add(a)
    s2.add(b)
print('s1 is {},s2 is {}'.format(s1,s2))
print('s1 and s2 Common figures is {}'.format(s1.union(s2)))
print('not repetition number is {},this is {}'.format(len(s1 ^ s2),s1 ^ s2))
print('repetition number is {}'.format(s1 & s2))
'''
#################### 简单选择排序 #########################
'''
nums  = [3,1,6,2,8,4,9,22]
length = len(nums)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if nums[maxindex] < nums[j]:
            maxindex = j

    if i != maxindex:
        nums[maxindex],nums[i] = nums[i],nums[maxindex]
print(nums)
'''

############# 练习--打印纸牌 ###########################
'''
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
###################################################
dict1 = {x:'{}'.format(x) for x in range(2,11)}
dict2 = {1:'A',11:'J',12:'Q',13:'K'}
s1 = dict1.copy()
s1.update(dict2)
types = ['红桃','方块','黑桃','梅花']
cards = [(i,k) for i in types for j,k in s1.items()]
for card in cards:
    print(card)
'''
##########  二元选择排序  #######################
'''
nums = [2,7,1,56,21,5,3,12]
length = len(nums)

for i in range(length // 2):
    maxindex = i
    minindex = -i - 1

    for j in range(i + 1,length - i):
        if nums[maxindex] < nums[j]:
            maxindex = j
        if nums[minindex] > nums[-j - 1]:
            minindex = -j - 1

     ########### 排除当元素全部相同的情况
    if nums[maxindex] == nums[minindex]:
        break

    if i != maxindex:
        nums[maxindex],nums[i] = nums[i],nums[maxindex]
        ## 如果最小值被交换过，要更新索引
        if i == minindex or i == length + minindex:
            minindex = maxindex

    if  -i - 1 != minindex:
        nums[minindex],nums[-i - 1] = nums[-i - 1],nums[minindex]

print(nums)
'''
#############################################################
'''
from collections import defaultdict
d1 = {}
d2 = defaultdict(list)
for k  in  'abcde':
    for v in range(5):
        if k not in d1.keys():
            d1[k] = []
        d1[k].append(v)
print(d1)
for k in 'mnopq':
    for v in range(3):
        d2[k].append(v)
print(d2)
########################################################
from collections import OrderedDict
import  random
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d)
keys = list(d.keys())
random.shuffle(keys)
print(keys)
od = OrderedDict()
for key in keys:
    od[key] = d[key]
print(od)
print(od.keys())
'''
################ 字典练习 ##########################
'''
from collections import Counter,defaultdict
a = input('>>>>')
print(Counter(a))
b = {}
for i in a:
    if i not in b.keys():
        b[i] = 1
    else:
        b[i] += 1
print(b)
'''
#############################################
'''
import  random
num_list = []
dict = {}
for i in range(100):
    num_list.append(random.randrange(-1000,1000))
for j in set(num_list):
    dict[j] = num_list.count(j)
#    print('{}:{}'.format(j,num_list.count(j)))
dt = sorted(dict.items(),key=lambda x:x[0],reverse=True)   ### dict.items()是一个个元组，lambda x:x[0]每个元组以第一个元素进行排序。
for i in range(3):
    print(dt[i])
############ 字符串重复统计 ####################
strings = 'abcdefghijklmnopqrstuvwxyz'
'''
'''
s = [i+j for i in strings for j in strings]
#print(s)
str_list = []
dict = {}
random.shuffle(s)
print(len(s))
for j in s:
    if j not in dict.keys():
        dict[j] = 1
    else:
        dict[j] += 1

dt = sorted(dict.items(),key=lambda x:x[0],reverse=True)
print(dt)
'''
'''
import random
words = []
for _ in range(100):
    #words.append(random.choice(strings) + random.choice(strings))
    #words.append(''.join(random.sample(strings,2))) ##随机采样
    words.append(''.join(random.choice(strings) for _ in range(2)))  ###生成器
d = {}
for x in words:
    d[x] = d.get(x,0) + 1
d1 = sorted(d.items(),reverse=True)
print(d1)
'''
############################################
'''
1、如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，
若用户数据不存在，则提示不存在;
2、如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dcit中数据，
若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在;
3、如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印;
4、如果用户输入list，则打印所有用户信息;
 打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
5、如果用户输入exit，则打印退出程序，并退出 ;
'''
'''
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
'''
###############################################
## 第二周作业
'''
在用户管理功能中添加密码信息:
增、改添加用户密码输入
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序）后将结果输入
'''
'''
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
'''
####################   函数   ####################################
# 练习：编写一个函数，接受一个参数n，n为正整数，左右两种打印方式，要求数字必须对齐。
'''
###方法一 ###################
def show(n):
    tail = " ".join([str(i) for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n+1):
        print("{:>{}}".format(" ".join([str(j) for j in range(i,0,-1)]),width))
show(5)
'''
#############方法二############
'''
def show(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if i < j :
                print(" "*len(str(j)),end= ' ')
            else:
                print(j,end=' ')
        print()
show(15)
'''
########### 下三角 #################
'''
def showtail(n):
    tail = " ".join([str(i) for i in range(n,0,-1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i,tail[i+1:])
showtail(10)
'''
########## 插入排序 ##############
'''
m_list = [1,9,8,5,6,7,4,3,2]
nums = [0] + m_list
#sentry ,*origin = nums
length = len(nums)

for i in range(2,length):
    nums[0] = nums[i]  ########设置哨兵位
    j = i -1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -= 1   #### 插入点索引
        nums[j+1] = nums[0]  ####将哨兵位插入
print(nums[1:])
'''
############### 第一月测试题 ###############
##第一题###################
''''
import random

lst = []
s = list({5,10,3,8,6,10,9,15,24,30,27,48,24})
for i in range(10):
    a = random.choice(s)
    if a % 3 == 0 and a %4 != 0:
        lst.append(a)
print(lst)
print(sum(lst))

########  第三题########
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

tm = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
for i in range(len(tm)):
    for j in range(len(matrix)):
        tm[i][j] = matrix[j][i]
print(tm)

########### 第四题 ##################
import datetime

dt = datetime.datetime.now().timestamp()
a =   ['{}_{}_{}'.format(str(dt)[:10],''.join(str(random.randint(0,9)) for _ in range(3)),
                         ''.join(chr(random.randint(97,122)) for j in range(8)))]
print(a)
################ 第五题 ################
lst = [29,30,37,12,1,5,55,15,75,79,75,64,26,25,29,985,15,26,24,78,26,28,29,31,35,38,39,37,79,74,78,75,78,74,25,18,75,79]
print(set(lst))
k = []
for i in lst:
    if i not in k:
        k.append(i)
print(sorted(k))

############### 第六题 #####################
nums = [375,3.5,6,20,9,-20,68]
length = len(nums)

for i in range(length):
    flag = False
    for j in range(length - i - 1):
        if nums[j] > nums[j +1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            flag = True
    if not flag:
        break
print(nums)
########## 第七题 ##########################
nums1 = [375,3.5,6,20,9,-20,68]
length = len(nums1)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if nums1[maxindex] > nums1[j]:
            maxindex = j
    if i != maxindex:
        nums1[maxindex],nums1[i] = nums1[i],nums1[maxindex]
print(nums1)
#### 第八题 #########################
'''
############# 递归##########
'''
import datetime
start = datetime.datetime.now()
pre = 0
cur = 1 # No1
print(pre, cur, end=' ')
def fib(n, pre=0,cur=1): # recursion
    pre, cur = cur, pre + cur
    print(cur, end=' ')
    if n == 2:
        return
    fib(n-1, pre, cur)
fib(35)
delta = (datetime.datetime.now() - start).total_seconds()
print()
print(delta)
'''
'''
import datetime
start = datetime.datetime.now()
pre = 0
cur = 1 # No1
print(pre, cur, end=' ')
n = 35
for i in range(n-1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
delta = (datetime.datetime.now() -start).total_seconds()
print()
print(delta)

n = 35
start = datetime.datetime.now()
def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)
for i in range(n):
    print(fib(i), end=' ')
delta = (datetime.datetime.now() -start).total_seconds()
print()
print(delta)
x = 1
sum = 0
n = 5
for i in range(1,n):
    x *= i
#    sum = sum + x
print(x)

def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)
print(fac(4))

lst = []
for i in '1234'[::-1]:
    lst.append(i)
print(lst)


peach = 1
for i in range(9):
    peach = 2*(peach+1)
print(peach)

def peach(days=1):
    if days == 10:
        return 1
    return (peach(days+1)+1)*2
print(peach())

def peach1(day=9,sum=1):
    sum = (sum + 1) * 2
    day  -= 1
    if day == 0:
        return sum
    return peach1(day,sum)
print(peach1())
'''
'''

source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def flatmap(src):
    def _flatmap(src,dest=None,prefix=''):
        for k,v in src.items():
            key = prefix + k
            if isinstance(v,(list,tuple,set,dict)):
                _flatmap(v,dest,key + '.')
            else:
                dest[key] = v
    dest = {}
    _flatmap(src,dest)
    return dest

print(flatmap(source))
'''
######### 高阶函数 #########
########## 自定义sort函数 #######################
'''
nums = [3,2,8,4,9,7,5,11]

def sorted(nums,key=lambda a,b : a > b):
    ret = []
    for x in nums:
        for i,y in enumerate(ret):
#            flag = x > y if reverse else x < y
            if key(y,x):
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret
print(sorted(nums))
'''
###### 装饰器函数 #####################
'''
def logger(fn):
    def _logger(*args,**kwargs):
        print('begin')
        ret = fn(*args,**kwargs)
        print('end')
        return ret
    return  _logger

@logger  #add = logger(add)
def add(x,y):
    return  x + y

print(add(3,4))
'''
###################
'''
import datetime
import time
import functools

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__name__
        return dst
    return _copy

def decorate(duration,func=lambda name,duration:print('{} took {}s'.format(name,duration))):
    def _decorate(fn):
#        @copy_properties(fn)
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            'I am wrapper'
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta =(datetime.datetime.now() - start).total_seconds()
#            print('so slow') if delta > duration else print('so fast')
            if delta > duration:
                func(fn.__name__,duration)
            return  ret
#        return wrapper
        return functools.update_wrapper(wrapper,fn)
    return _decorate

@decorate(4)
def add1(x,y):
    """This is a funcction for add"""
    time.sleep(2)
    return x * y
#print("name={}, doc={}".format(add1.__name__, add1.__doc__))
print(add1(3,4),add1.__name__,add1.__wrapped__,add1.__dict__,sep='\n')
'''
'''
def logger(duration):
    def _logger(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            print('begin')
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print(delta)
            if delta > duration:
                print('so slow')
            return  ret
        return wrapper
    return _logger

@logger(3)
def add(x,y):
    """
    This is add function

    :x int
    :y int
    :return int
    """
    time.sleep(3)
    return x + y

print(add(2,5),add.__name__,add.__doc__,sep='\n')
'''
##### 冒泡法、选择排序、插入排序 ##################
'''
nums = [0,3,5,1,7,6,8,2,9]
length = len(nums)

for i in range(2,length):
    nums[0] = nums[i]
    j = i - 1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j + 1] = nums[j]
            j -= 1
    nums[j + 1] = nums[0]
print(nums[1:])

for i in range(length):
    flag = False
    for j in range(length - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j],nums[j + 1] = nums[j + 1],nums[j]
            flag = True
    if not flag:
        break
print(nums)

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        if nums[maxindex] < nums[j]:
            maxindex = j

    if i != maxindex:
        nums[maxindex],nums[i] = nums[i],nums[maxindex]

print(nums)
'''
############### 参数注解与inspect模块应用 ###########
'''
import inspect
import functools

def check(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        # 实参检查
        sig = inspect.signature(fn)
        params = sig.parameters
        # 位置参数处理
        param_list = list(params.keys())
        print(param_list)
        for i,v in enumerate(args):
            k = param_list[i]
            if isinstance(v,params[k].annotation):
                print(v,'is',params[k].annotation)
            else:
                print('{} {} {}'.format(v,'is not',params[k].annotation))

        # 关键字参数处理
        for k,v in kwargs.items():
            if isinstance(v,params[k].annotation):
                print(v,'is',params[k].annotation)
            else:
                print('{} {} {}'.format(v,'is not',params[k].annotation))

        ret = fn(*args,**kwargs)
        return ret
    return wrapper

@check
def add(x:int,y:int = 7,*args) -> int:
    return x + y

print(add(4,5))
'''
################# cache 装饰器#######################
# 缓冲buff 、缓存cache
'''
from functools import wraps
import time
import inspect
import datetime

def m_cache(duration):
    def _cache(fn):
        local_cache = {}
        @wraps(fn)
        def wrapper(*args,**kwargs):
    #        print(args,kwargs)
            #判断local_cache 有没有过期的key,过期就清除
            def clear_expire(cache):
                expire_keys = []
                for k, (_, timestamp) in cache.items():
                    if datetime.datetime.now().timestamp() - timestamp > duration:
                        expire_keys.append(k)
                for k in expire_keys:
                    cache.pop(k)

            clear_expire(local_cache)

            def make_key():
                key_dict = {}   #排序用sorted
                sig = inspect.signature(fn)
                params = sig.parameters #有序字典
                param_list = list(params.keys())
                # 位置参数
                for i,v in enumerate(args):
        #            print(i,v)
                    k = param_list[i]
                    key_dict[k] = v
                #关键字参数
                #for k,v in kwargs.items():   等于下面的update
                #   key_dict[k] = v
                key_dict.update(kwargs)
                #缺省值处理
                for k in params.keys():
                    if k not in key_dict.keys():
                        key_dict[k] = params[k].default

                return tuple(sorted(key_dict.items()))

            ##生成key
            key = make_key()
            ## 判断key是否在local缓存中，如果在则输出缓存值，不在就存入缓存字典中
            if key not in local_cache.keys():
                ret = fn(*args,**kwargs)
                local_cache[key] = (ret,datetime.datetime.now().timestamp())

            return  local_cache[key]
        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('run time is {}'.format(delta))
        return ret
    return wrapper

@logger
@m_cache(5)
def add(x,y=5):
    time.sleep(3)
    ret = x + y
    print(ret)
    return ret

add(4)
add(4,5)
add(x=4,y=5)

time.sleep(6)

add(4)
add(4,5)
add(x=4,y=5)
'''
#### 命令分发器#############
'''
from functools import partial

def command_dispatcher():
    command = {}
    #注册函数
    def register(name,*args,**kwargs):
        def _register(fn):
            func = partial(fn,*args,**kwargs)
            command[name] = func
            return func
        return _register
    #缺省函数
    def default_func():
        print("Unkown command")
    #调度器
    def dispatcher():
        while True:
            cmd = input(">>>>")
            if cmd.strip() == "":
                return
            command.get(cmd,default_func)()

    return register,dispatcher

register,dispatcher = command_dispatcher()

#自定义函数
@register('mag',x=100,y=200,z=300)
def foo1(x,y,z):
    print('magedu',x,y,z)

@register('py',300,b=400)
def foo2(a,b=100):
    print('python',a,b)

#调度循环
dispatcher()

### 求2个字符串的最长公共子串
s1 = "abcdefg"
s2 = "defabcdoabcdeftw"
s3 = "1234a"

def findit(str1,str2):
    length = len(str1)

    for sublen in range(length,0,-1):
        for start in range(0,length - sublen + 1):
            substr = str1[start:start + sublen]
            if str2.find(substr) > -1:
                print("substrlen={}".format(sublen))
                return substr

print(findit(s1,s2))
'''''
## 堆排序 ############              疑难点
'''
import math

def print_tree(array):
    """
            前空格     元素间
    1         7         0
    2         3         7
    3         1         3
    4         0         1
    """
    index = 1
    depth = math.ceil(math.log2(len(array)))  #因为补0了,不然应该是math.ceil(math.log2(len(array)+1))
    sep = "  "
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1),end='')
        line = array[index:index + offset]
        for j,x in enumerate(line):
            print("{:>{}}".format(x,len(sep)),end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval,end='')

            index += offset
            print()
#Heap Sort
#为了和编码对应，增加一个无用的0在首位
origin = [0,30,20,80,40,50,10,60,70,90]
total = len(origin) - 1  ##初始待排序元素个数，即n
print(origin)
print_tree(origin)
print("="*50)
def heap_adjust(n,i,array:list):
    while 2 * i <= n:
        #孩子结点判断 2为左孩子，2i+1为右孩子
        lchile_index = 2 * i
        max_child_index = lchile_index #n = 2i
        if n > lchile_index and array[lchile_index + 1] > array[lchile_index]: #n>2i说明还有右孩子
            max_child_index = lchile_index #n =2i+1

        #和子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i],array[max_child_index] = array[max_child_index],array[i]
            i = max_child_index #被交换后，需要判断是否还需要调整
        else:
            break

# 构建大顶堆，大根堆
def max_heap(total,array:list):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
    return array

print_tree(max_heap(total,origin))
print('=='*50)

#排序
def sort(total,array:list):
    while total > 1:
        array[1],array[total] = array[total],array[1] #堆顶和最后一个结点交换
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:
            break
        heap_adjust(total,1,array)
    return array

print_tree(sort(total,origin))
print(origin)
'''
### 对一个文件，进行单词统计，不区分大小写，并显示单词重复最多的10个单词 ##############    疑难"""
"""
def wordcount(file='sample.txt'):
    chars = '''~!@#$$&*()_+{}[]|\\/"'=,:-<>'''
    charset = set(chars)
    with open(file,'r+',encoding="utf8") as f:
        word_count = {}
        for line in f:
            words = line.split()

#            for k,v in zip(words,(1,)*len(words)):
            for k in words:
                k = k.strip(chars)
                if len(k) < 1:
                    continue
                k = k.lower()
                start = 0
                for i,c in enumerate(k):
                    if c in charset:
                        if start == i:
                            start = i + 1
                            continue
                        key = k[start:i]
                        word_count[k] = word_count.get(k,0) + 1
                        start = i + 1
                else:
                    key = k[start:]
                    word_count[k] = word_count.get(k,0) + 1

    lst = sorted(word_count.items(),key=lambda x:x[1],reverse=True)
    for i in range(10):
        print("word is {} ,number is {}".format(lst[i][0],lst[i][1]))
       # if i < len(lst):
       #     print(str(lst[i:]).strip("'()").replace("'",""))

    return lst
wordcount()
"""









