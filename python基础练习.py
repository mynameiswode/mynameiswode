import time

# 1 # 给a,b,c,d 四个变量分别赋值1,2,3,4
# a = 1
# b = 2
# c = 3
# d = 4
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)

# 2 #交换ab a=2,b=1
# temp = 0
# temp = a
# a = b
# b = temp

a, b = b, a  # 交换ab
print(a, b)
# 3 #存放学生信息的列表,list[姓名,年龄,性别]
list1 = ['Eddie', 20, 'male']
# name = list1[0]
# age = list1[1]
# gender = list1[2]
# print('name:', name)
# print('age:', age)
# print('gender:', gender)

name, age, gender = list1
print('name:', name)
print('age:', age)
print('gender:', gender)

# 4 # x,x>10,y=x,x<10 y=-x
x = 9
# if x > 10:
#     y = x
# else:
#     y = -x

y = x if x > 10 else -x
print('y:', y)

# 5 # 80-90 B
score = 89
if score >= 80 and score < 90:
    level = 'B'
print('level:', level)
if 80 <= score <= 90:
    level = 'B'
print('level:', level)

# 6 #等级在ABC当中,就是及格
# if level == 'A' or level == 'B' or level == 'C':
#     print('passed')
# else:
#     print('failed!')

if level in ('A', 'B', 'C'):
    print('passed')
else:
    print('failed')

# any([exp1,exp2,exp3])
if any([level == 'A', level == 'B', level == 'C']):
    print('any passed')
else:
    print('failed!')

math = 90
english = 89
computer = 70
# if math >= 60 and english >= 60 and computer >= 60:
#     print('passed!')
if all([math >= 60, english >= 60, computer >= 60]):
    print('all passed!')

# 7 # 判断字典,列表,字符串为空
li, dic, str1 = [1, 2, 3], {}, ''
# if len(li):
#     print('list is not empty')
# if len(dic):
#     print('dict is not empty')
# if len(str1):
#     print('string is not empty')

# None,空列表,空字典,空元组,空字符串,False,其他 True

if li:
    print('list is not empty')
if dic:
    print('dict is not empty')
if str1:
    print('string is not empty')
# 8 # 同时遍历列表的元素及其下标
list2 = ['Eddie', 'Due', 'Sean', 'Abby']
for i in range(len(list2)):
    print(i, ':', list2[i])

for i, name in enumerate(list2):
    print(i, ':', name)

# 9 #显示循环进度
i, n = 0, 100
for i in range(n):
    print('\r', i + 1, end='%')
    time.sleep(0.01)

print()
print('# 10 # 匿名函数 lambda')
# 10 # 匿名函数 lambda
list3 = [1, 23, 5, 6, 'qq', 'yuuui', 9]


def isNum(x):
    return isinstance(x, int)  # true,x is not int,false


# filter()function: (_T) -> Any, iterable: Iterable[_T]
# new_list = list(filter(isNum, list3))
# print(sum(new_list))

new_list = list(filter(lambda x: isinstance(x, int), list3))
print(sum(new_list))


# 模拟题目答案

def waitTime(args):
####################################
    args.sort()  #排序从小到大
    l=len(args) #长度
    result=0
    for i in range(l):
        result+= args[i]*(l-i)
####################################
    return result

t=[5,10,8,7]
print(waitTime(t))