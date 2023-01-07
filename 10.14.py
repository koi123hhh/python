#extend一次添加多个元素
#a=[1,2,3,]
#a.extend([4,5,6,7,])
#print(a)
#append只能添加一个元素
#a.append([7,8,9,])
#print(a)#[1, 2, 3, 4, 5, 6, 7, [7, 8, 9]][7,8,9,]是一个元素
#还有一个相加的操做extend和加法
#区别；相加的话又新创建了一个变量要占用内存而extend是在原基础a上改变的函数不占用新的内存
#b=[30,40,50]
#c=a+b
#print(c)#[1, 2, 3, 4, 5, 6, 7, [7, 8, 9], 30, 40, 50]
#copy与赋值的区别
a=['helli','world','heqimeng','nihao']#如果不加，那就是一个字符串
b=a.copy()
del a[0]
print(b)
c=b
del b[0]
print(c)
#sort函数 列表内必须都是同类性，不能数字——字符混用会报错
e=['hello','world','nihao','wo']
e.sort()
print(e)
f=[1,2,3,4,5,1,1,1,2,]
f.sort()
print(f)
#count用于显示某个字符出现了多少次
g=f.count(1)
print(g)

