#1.两数之和
# a=int(input('请输入一个数:'))
# b=int(input('请再输入一个数:'))
# c=a+b
# print(c)
# #当a和b的输出前面不加int时是错误的当输入2 和3时c的值是23因为input输出为字符串形式
# #当需要把整个式子打印出来时可以使用字符串的格式化操作
# numbers1=int(input('请输入第一个数:'))
# numbers2=int(input('请输入第二个数:'))
# sum=numbers1+numbers2
# print(f'{numbers1}+{numbers2}={sum}')
#2.数字的阶乘为了方便一次求解多个数的阶乘,可以调用函数
def jiecheng(number):
    result=1
    while number>0:
        result*=number
        number-=1
    return result
print('jiecheng6=',jiecheng(6))
print('jiecheng8=',jiecheng(8))
#3.计算圆的面积pi在math模块中
import math
p=math.pi
r=int(input('请输入半径的值:'))
s=pow(r,2)*p
print(s)
#使用函数来计算多次调用多次计算
def rounds(r):
    return round(pow(r,2)*math.pi,2)#结果保留两位小数可以用round(number,要保留的位数)
print(rounds(1))
print(rounds(2))
#3.求区间内的所有素数
def isprime(number):
    if number in (1,2):
        return True
    for j in range(2,number):
        if number%j==0:
            return False
    return True
def prime(begin,end):
    for number in range(begin,end+1):
        if isprime(number):
            print(f'{number}是一个素数')
prime(1,10)
#5.求n个数字的平方和
def sumofsquare(n):
    result=0
    for i in range(1,n+1):
        result += i*i
    return result
print(sumofsquare(3))
#6.计算列表中所有的数字和
list1=[1,2,3,4]
list2=[5,6,7,8]
def sumoflist(alist):
    sum=0
    for i in alist:#谨记列表不用加range
        sum+=i
    return sum
print(sumoflist(list1))
print(sumoflist(list2))
#最大公约数
import math
a,b= map(int, input().split())
c=math.gcd(a,b)
print(c)

for s in 'baseball':
    if  s=='b':
        break
    print(s)























































































