#del的牛逼用法
#可以直接删除一些东西x='fishc',y=[1,2,3]......
#也可以删除可变序列中特定的值
a=[1,2,3,4,5]
del a[1:4]
print(a)#[1, 5]
x=[1,2,3,4,5]
del x[::2]
print(x)#print(x)#[2,4]
#用切片的方法行不通
# y=[1,2,3,4,5]报错
# y[::2]=[]
# print(y)#Traceback (most recent call last):
#   File "D:\py.works\hqm2022.11\序列.py", line 12, in <module>
#     y[::2]=[]
# ValueError: attempt to assign sequence of size 0 to extended slice of size 3
#删除可变列表中的所有元素
y=[1,2,3,4,5]
del y[:]
print(y)#[]
#列表，原组，字符串相互转化list(),tuple(),str()
b=list('fishc')
print(b)
#max,min大写字母的编码值要小于小写字母的编码值
c='fishc'
cc=min(c)
print(cc)#c
ccc=[1,2,3,46,7,3]
print(max(ccc))#46
#如果输入的是一个空集合或空列表在使用最大值和最小值时会报错
s=[]
print(min(s,default='皮，啥都没有怎末来的最小值'))
print(min(1,2,3,4,5))#1
#求和函数
d=[1,2,3,4,5,6]
print(sum(d,start=100))#121只有start这一个参数指定起始运算的值
#sorted函数和reversed
#sort和revers这两个函数是伴随这列表使用的不能用在其他的数据类型里面
#sort和sorted在列表中的用法
e=[1,2,5,4,3]
#print(e.sort())#不返回值None sort是在函数e的基础上对e进行的变换
e.sort()
print(e)#[1, 2, 3, 4, 5]
#从大到小排列
e.sort(reverse=True)
print(e)#[5, 4, 3, 2, 1]
ee=[1,2,4,5,7,6,3]
print(sorted(ee))#[1, 2, 3, 4, 5, 6, 7]
print(sorted(ee,reverse=True))#[7, 6, 5, 4, 3, 2, 1]
eee=['krd','book','nihao','hudc','dffddd']
print(sorted(eee,key=len))#['krd', 'book', 'hudc', 'nihao', 'dffddd']
print(sorted((1,0,0,8,6)))#[0, 0, 1, 6, 8]sorted里面是一个序列



























































































































