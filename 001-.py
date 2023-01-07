#1.求两数之和
def qiuhe(a,b):
    sum=a+b
    return sum
print(qiuhe(3,4))
#2.求数字的阶乘
def jiecheng(number):
    result=1
    while number>0:
        result*=number
        number-=1
    return result
print(jiecheng(6))
#3.计算圆的面积
import math
def yuanmianji(r):
    s=math.pi*pow(r,2)
    return s
print(round(yuanmianji(1),2))
#4.计算区间内所有的素数
def issushu(number):
    if number in(1,2):
        return True
    else:
        for i in range(2,number):
            if number%i==0:
                return False
    return True
def sushu(begin,end):
    for number in range(1,end+1):
        if issushu(number):
            print(f'{number}is prime')
print(sushu(1,6))
#5求前n个数字的平方和
def pingfanghe(n):
    result=0
    while n>0:
        result+=pow(n,2)
        n-=1
    return result
print(pingfanghe(3))
#6.计算列表数字的和
def liebiaohe(list):
    result=0
    for i in list:
        result+=i
    return result
list1=[1,2,3,4]
print(liebiaohe(list1))
#7.数字范围内所有的偶数
def oushu(n):
    result=[]
    for i in range(1,n+1):
        if i%2==0:
            result.append(i)
    return result
print(oushu(7))
#8.从列表中移除多个元素
def yichuduoge(list1,list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1
list1=[1,2,3,4,5,6]
list2=[1,2]
print(yichuduoge(list1,list2))
#列表推导式的使用
date=[i for i in list1 if i not in list2]
print(date)
#9对列表进行去重
#运用集合对其进行去重
a=[1,2,3,1,1,1]
b=set(a)
print(list(b))
#正常函数方法
def quchong(list):
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    return result
print(quchong(a))
#10.对简单列表进行排序sort,sorted,reverse=Ture从大到小进行排序
def paixu(list):
    listb=sorted(list,reverse=True)#这样写并没有改变原列表的顺序,只是又新建了一个列表
    return listb
list3=[2,1,4,3,5,7,6]
print(paixu(list3))
#11.python实现对学生成绩的排序lambda
students=[
    {'name':'小王','chengji':'99'},
    {'name':'小赵','chengji':'77'},
    {'name':'小李','chengji':'88'},
    {'name':'小芳','chengji':'66'}
]
paixu=sorted(students,key=lambda x:x['chengji'],reverse=True)
print(paixu)#key是键
#12.python读取成绩文件实现排序
def readfile():
    result=[]
    with open('./chengjiwenjian.txt') as fin:
        for line in fin:
            line=line[:-1]
            result.append(line.split(','))
    return result
def sortgrade(dates):
    return sorted(dates,
                  key=lambda x:int(x[2]),
                  reverse=True)
dates=readfile()
print(dates)
b=sortgrade(dates)
print(b)
















