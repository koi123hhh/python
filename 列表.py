#列表的增删改查
heros=['钢铁侠','黑寡妇']
#heros.append('绿巨人')

#弊端之只能增加一个元素发在列表的末尾
heros.extend(['鹰眼','灭霸','雷神'])#增加多个元素时，用列表套着
print(heros)

#insert插入
a=[1,2,3,5]
a.insert(3,4)#第一个是插入的位置，第二个是筛入的内容
print(a)
#remove移除pop索引clear清除

wang=['路飞','sulong','namei','nikeluobin','nihao','duxiaoyya']
wang[4]='gangteixia'
print(wang)
#更改多个元素的做法
wang[3:]=['bure','nihao','haihai']
print(wang)

#将数字从小到大进行排序
num=[1,2,8,4,5,9,10]
num.sort()
print(num)

#将元素从大到小进行拍列reverse将元素进行调转
num.reverse()
print(num)
#叠加列表的两种表达方法
aaa=[1,2,3]
bbb=[4,5,6]
ccc=aaa+bbb
print(ccc)
ddd=aaa*3
print(ddd)

#列表的镶嵌
eee=[[1,2,3],[4,5,6],[7,8,9]]
#两种访问模式
for i in eee:
    for g in i:
        print(g)#一个以分行
for z in eee:
    for v in z:
        print(v,end=' ')
    print()#进行换行处理
print(eee[0][0])#第一个列表是镶嵌列表中的第一个列表第二个是第一个列表中第一个元素
#创建一个二维列表
zzz=[0]*3
#print(zzz)#一维
#用循环的方法
for i in range(3):
    zzz[i]=[0]*3
print(zzz)#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]一个二维列表的创建
#一种错误的列表二维方法
fff=[[0]*3]*3
print(fff)#打印出来也是一个二维的东西但是列表是可变的，所以相同的列表储存在不同的位置而fff
#所对应的二维列表是一个东西当对其中一个小列表中的元素进行增删补差时牵一发而动全身
#用列表的推导式来创建一个二维列表
ss=[[0]*3 for i in range(3)]
print(ss)#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ss[1][1]=1
print(ss)#[[0, 0, 0], [0, 1, 0], [0, 0, 0]]


#列表的拷贝1.浅拷贝
x=[1,2,3]
y=x
x[1]=1
print(x)#[1, 1, 3][1, 1, 3]x,y的值都发生了改变，因为x，y是同一个列表
print(y)
z=x.copy()
x[2]=2
print(z)#113
print(x)#112
#这是两个列表，储存在两个地方，值一样，但是位置不一样
#2.深拷贝用于镶嵌了列表中
xx=[[1,2,3],[4,5,6],[7,8,9]]
yy=xx.copy()
xx[1][1]=0
print(xx)
print(yy)
#[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
#[[1, 2, 3], [4, 0, 6], [7, 8, 9]]这种浅拷贝只是拷贝了列表的最外层，列表内部的改变还是会影响两个变量的改变
#深拷贝引用copy模块中的deepcopy，copy模块中一共有两个函数一个是copy，一个是deepcopy，一深一浅
import copy
xxx=[[1,2,3],[4,5,6],[7,8,9]]
yyy=copy.copy(xxx)
xxx[1][1]=0
print(xxx)
print(yyy)
#[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
#[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
xxxx=[[1,2,3],[4,5,6],[7,8,9]]
yyyy=copy.deepcopy(xxxx)
xxxx[1][1]=0
print(xxxx)
print(yyyy)
#[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#列表推导式
#将列表中的每一个元素乘以原来的2倍1.循环是将你的老婆变得更聪明
oho=[1,2,3,4,5]
for i in range(len(oho)):
    oho[i]=oho[i]*2
print(oho)
#2.列表的推导式，是直接换了个老婆。
oo=[1,2,3,4,5]
oo=[i*2 for i in oo]
print(oo)#[2,4,6,8,10]
vv=[i for i in range(10)]
print(vv)
vvv=[i+i for i in range(5)]
print(vvv)#[0,2,4,6,8]
#当然列表的推导式也可以应用于字符串
vvvv=[i*2 for i in 'fishc']
print(vvvv)#['ff', 'ii', 'ss', 'hh', 'cc']
#打印字符串对应的unicode编码引用一个ord
zzz=[ord(i) for i in 'fishc']
print(zzz)#[102, 105, 115, 104, 99]
#索引元素
nnn=[[1,2,3],
     [4,5,6],
     [7,8,9]]
c2=[row[1] for row in nnn]
print(c2)#[2,5,8]
#第i行第i列元素的提取
c3=[nnn[i][i] for i in range(len(nnn))]
print(c3)
#列表的推导式同样可以有if语句的参与
#取0到9之间的参数
d1=[i for i in range(0,9,2)]
print(d1)
d2=[i for i in range(0,9)if i%2==0 ]
print(d2)
#[0, 2, 4, 6, 8]
#[0, 2, 4, 6, 8]
d3=['fishc','fii','nihao','heqimeng']
d4=[w for w in d3 if w[0]=='f']#先执行for循环再接着执行if语句最后打印要打印的值
#先取出d3的值放入w中判断w的第一个值是否为’f'最后打印出筛选出来的w值
print(d4)
#二维列表转化为一维列表运用列表推导式中的嵌套进行
d5=[[1,2,3],[4,5,6],[7,8,9]]
d6=[a2 for a3 in d5 for a2 in a3]
print(d6)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#等价于
d7=[]
for d8 in d5:
    for d9 in d8:
        d7.append(d9)
print(d7)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
d10=[x+y for x in'fishc'for y in 'FISHC']
print(d10)
#['fF', 'fI', 'fS', 'fH', 'fC', 'iF', 'iI', 'iS', 'iH', 'iC', 'sF', 'sI', 'sS', 'sH', 'sC', 'hF', 'hI', 'hS', 'hH', 'hC', 'cF', 'cI', 'cS', 'cH', 'cC']
#相当于循环的嵌套
#循环加镶嵌
d5=[[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0]
print(d5)
#[[0, 0], [0, 3], [0, 6], [0, 9], [2, 0], [2, 3], [2, 6], [2, 9], [4, 0], [4, 3], [4, 6], [4, 9], [6, 0], [6, 3], [6, 6], [6, 9], [8, 0], [8, 3], [8, 6], [8, 9]]
#用for in循环来实现的话
_=[]
for x in range(10):
    if x%2==0:
        for y in range(10):
            if y%3==0:
             print([x,y])






































