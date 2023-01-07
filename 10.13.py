#列表
#定义，下标，列表取值
#List1=[1,2,3,'woaini',[1,2,3,]]
#print(List1[4][1])
List1=[1,2,3,4,5,6,7]
print(len(List1))
List1[2]=99
print(List1)
#列表的加法和乘法操作
List2=[1,2,3,]
List3=[4,5,6,]
print(List2+List3)
print(List2*5)

s5='woaini'*5
print(s5)
#列表的切片取值
List4=[10,20,30,40,50]#[10, 20, 30, 40]
print(List4[0:4])
#逆向取值
print(List4[-3:-1])
#要想取50的话
print(List4[-3:])
#整个都取
print(List4[:])
#加一个步长
print(List4[1:5:2])#小2是步长跨两步
#负数跨步子
print(List4[-5:-1:2])
#反向
print(List4[::-1])#[50, 40, 30, 20, 10]
#list和字符串操作一样
#列表的操作方法
#1.del关键字 删除
a=[1,2,3,]
del a[2]#shangchu
print(a)
#2.append用于向列表末尾添加元素
#print(a.append(4))#None#不能这样写
a.append(4)#先变a再进行打印
print(a)
#3.insert像列表中插入元素
List5=[1,2,3,4,5,]
#List5.insert(2,[4,5,6],)
#print(List5)
#4.clear函数用于将列表清空的操作
List5.clear()
print(List5)
#5.remove移除 只会移除匹配到的第一个
b=[1,1,2,3,4,5]
b.remove(1)
print(b)
#6.pop删除指定的下标
b.pop(3)
print(b)#打印更改后的列表
print(b.pop(3))#打印要移除的字符串
#7.index匹配第一次找的是坐标
c=['hello','world','hello','nihao']
r=c.index('hello')
print(r,1,3)
#疑问运行出来为什莫不是2
#运行结果0 1 3不懂
#8reverse逆向排列
#c.reverse()
#print(c)
print(c[::-1])
#9
