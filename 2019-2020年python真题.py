'''
2019-2020年python真题

20,小明某天被分配到一个任务,有一个输入的序列,首先输入的整数个数n,然后输入了n个整数.
小明要输出为n个整数中负数的个数,和所有非负整数的平均值,结果保留一位小数.请你来帮助
小明解决这个问题.
输入:
	--整数个数n,然后用空格隔开的n个整数组成的字符串
输出:
	--负数的个数和非负整数的平均值
举例:
	--输入:5 1 2 3 4 5 输出:0 3.0

# 完成计算统计函数,系统会自动调用
def count(args):
	return result1,result2

'''


'''
21,给定一个整数N,判断N是否为素数.
输入:
	--正整数N
输出:
	--判定结果

举例:
	--输入:100 输出:False

# 完成素数判断函数,系统会自动调用
def prime(n):
	return result

'''


'''
22,小明被布置了一个任务,要求在O(1)时间检测整数n是否能写成m个2相乘的样子,
请你帮他实现
输入:
	--正整数N
输出:
	--判断结果True或者False
举例:
	--输入:2 输出:True

# 完成judge函数,系统会自动调用
def judge(n):
	return result

'''

# 21,完成计算统计函数,系统会自动调用
def count(args):

    a=args.split(' ')  #空格转list函数
    numbers = list(map(int, a))
    result1=0
    b=[]   
    for i in range(1,numbers[0]+1):
        if numbers[i]<0 : #筛选非负数，负数判断为真，负数个数加一，跳过下面else步骤
            result1=result1+1
        else :
            b.append(numbers[i])    #非负数，加入列表 b    
    sum=0
    for i in range(len(b)):
        sum=sum+b[i]  #非负数累加
    if sum==0:
        result2=0.0  #保留一位小数
    else :
        result2=round(float(sum/len(b)),1)  #所有非负整数的平均值,结果保留一位小数

    return result1,result2

# 验证21
print('21题:      输出:',count('5 1 2 3 4 5'))


# 22,完成素数判断函数，系统会自动调用
def prime(n):

    result= True
    if n < 2: 
        result = False
    for i in range(2,int(n**0.5)+1):  #缩小遍历范围 n的开方即可完成
        if n % i == 0:    #是否能整除
            result= False

    return result


print('22题:n=100 素数判断:',prime(100))

# 23,完成judge函数,系统会自动调用
def judge(n):

	if n < 1 :
		result = False
	elif (n & (n-1)) == 0: # 4 & (4-1) :100 & 11 =000
		result = True   #n为 2的m次方 二进制 写成10...0  m个0 在后面 那么n-1 二进制为 1....1 m个1组成 位运算与 & 的结果为0
	else:
		result = False

	return result

print('23题:n=2   判断结果:',judge(2))
