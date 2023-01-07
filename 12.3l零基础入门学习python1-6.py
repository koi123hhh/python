#1.字符串中+/*的用法一个拼接一个复制
a="let's go."
print(a)
aa='let\'s go.'
print(aa)
#如果想打印出\,但是结尾处不能有\
aaa='ni\\nhao'
print(aaa)
aaaa=r'nihao\niahao'
print(aaaa)
#如果结尾处有\加双\\,加空格，使用字符串的拼接
aaaaa='nihao\\'
print(aaaaa)
#长字符串的运用可能会使用一堆的\用双三引号
b="""
面朝大海,
春暖花开。
"""
print(b)
#小插曲创建一个小游戏
# import random
# c=random.randint(1,10)
# for i in range(3):
#     d = int(input('请输入一个整数：'))
#     if c==d:
#         print('猜对了，你好棒。')
#         break
#     else:
#         if d<c:
#             print('有点小了，再试试。')
#         else:
#             print('有点大了，再试试。')
# print('游戏结束。')
#常见的数据类型int float bool 复数
cc='nihao'
print(type(cc))
ccc=2
print(isinstance(ccc,str))#Flace
#常用操作符加减乘除，余数，地板除（直接删除后面的小数部分）
#优先级问题幂函数，一级操作符正负号，乘除加减，判断操作符，逻辑操作符。
###特殊的一类操作符，三级操作符
x=1
y=2
a=x if x<y else y#三级操作符
print(a)
#列表的增删改除
e=[1,2,3,4]
e.append(5)
print(e)
#指在末尾添加一个元素
e.extend([4,5,6])
print(e)
#添加好几个
e.pop(1)
print(e)
#默认删除最后一个，加上的是索引值
#插入元素
e.insert(1,3)#索引，插入值
print(e)
#查
print(e[3])
#删除元素
e.remove(4)
print(e)
#
e.pop()

#函数的调用，也可以调用次数
def myfunc(name,times):
    for i in range(times):
        print('I love {}'.format(name))
print(myfunc('heqimeng',5))

#收集参数
def myfunc(*args):
    print('有{}个参数'.format(len(args)))
    print('第二个参数是：{}'.format(args[1]))
myfunc('小鲫鱼','有','一个小媳妇')
#元组具有打包和解包的功能
#将函数打包成字典的模式
def aaa(**kwargs):
    print(kwargs)
aaa(a=1,b=2,c=3)
#{'a': 1, 'b': 2, 'c': 3}
#* **混合使用
def bbb(a,*b,**c):
    print(a,b,c)
bbb(1,2,3,4,c=5,d=6)
#1 (2, 3, 4) {'c': 5, 'd': 6}
#函数* **的解包
args=(1,2,3,4)
def ccc(a,b,c,d):
    print(a,b,c,d)
ccc(*args)#1 2 3 4
kwargs={'a':1,'b':2,'c':3,'d':4}
ccc(**kwargs)#1 2 3 4字典只打印值
#全局变量在局部变量中也可以访问得到，但局部变量不能在全局变量中访问到
def ddd():
    yy=50
    print(yy)
ddd()
#print(yy)尝试在全局变量中去访问局部变量，不可以
zz=30
def zzz():
    print(zz)
zzz()#30这一步是在局部变量中访问全局变量可以访问到
print(zz)#30
#但是在局部变量中不可以改变全局变量的值除了局部局部变量就没有效果了
gg=520
def ggg():
    gg=250
    print(gg)
ggg()#250
print(gg)#520
#如果一定要在局部变量中去修改全局变量的值用global,但是不建议使用
#函数的嵌套
def funa():
    x=520
    def funb():
        x=880
        print('在funb中x=',x)

funa()#在funa中不能直接出来funb，必须在funa中调用一下funb
#打印不出来
def funa():
    x = 520
    def funb():
        x = 880
        print('在funb中x=', x)
    funb()
    print('在funa中，x=',x)
funa()
#在funb中x= 880
#在funa中，x= 520
def funa():
    x = 520
    def funb():
        nonlocal x#python只会劝你从良，不会阻止你犯罪，要想从内部改变外部函数的x，必须加上nonlocal
        x = 880
        print('在funb中x=', x)
    funb()
    print('在funa中，x=',x)
funa()
#在funb中x= 880
#在funa中，x= 880

#LEGB
# 内置函数的调用
def eee(a):
    def fff(c):
        return c**a
    return fff
aa=eee(3)
bb=eee(4)
print(aa(2))#8
print(bb(2))#16
#函数的记忆功能
def hhh():
    x=0
    y=0
    def iii(x1,x2):
        nonlocal x,y
        x+=x1
        y+=x2
        print(f'现在x的值是{x}，现在y的值是{y}')
    return iii
hh=hhh()
hh(1,2)#这个时候已经叠加上去了
print(hh(1,2))#到这里又叠加上去一遍拥有了记忆功能
#现在x的值是1，现在y的值是2
#现在x的值是2，现在y的值是4

#函数调用函数将函数作为参数传递给另一个函数
def myfuns():
    print('正在调用函数myfuns...')
def report(fun):#形参，先定义一个函数名
    print('我要开始调用程序了。。')
    fun()#在函数里面调用函数
    print('调用完程序，结束。')
report(myfuns)
# 我要开始调用程序了。。
# 正在调用函数myfuns...
# 调用完程序，结束。
#检测程序运行时间
import time
def timemaster(func):
    print('开始运行程序...')
    start=time.time()
    func()
    stop=time.time()
    print('程序运行结束...')
    print(f'一共消耗了{(start-stop):.3f}秒')
timemaster(myfuns)
# 开始运行程序...
# 正在调用函数myfuns...
# 程序运行结束...
# 一共消耗了0.000秒
#装饰器
# @timemaster
# def myfun():
#     time.sleep(2)
#     print('...')
# myfun()
#一行流lamnda的使用
def uuu(x):
    return x*x
print(uuu(3))#9
#一行流
uuu1=lambda y:y*y
print(uuu1(3))#9
#lambda 因为不是一个函数所以应用更广泛一点
uy=[lambda y:y*y,2,3]
print(uy[0](6))#36
#打印一到十内的参数
b=list(filter(lambda x:x%2,range(11)))#返回其中的False
print(b)#[1, 3, 5, 7, 9]
#生成器的概念
# #以 list 容器为例，在使用该容器迭代一组数据时，必须事先将所有数据存储到容器中，才能开始迭代；而生成器却不同，它可以实现在迭代的同时生成元素。
# 也就是说，对于可以用某种算法推算得到的多个数据，生成器并不会一次性生成它们，而是什么时候需要，才什么时候生成。
#
# 不仅如此，生成器的创建方式也比迭代器简单很多，大体分为以下 2 步：
# 定义一个以 yield 关键字标识返回值的函数；
# 调用刚刚创建的函数，即可创建一个生成器。
#相比迭代器，生成器最明显的优势就是节省内存空间，即它不会一次性生成所有的数据，而是什么时候需要，什么时候生成。
def numa():
    print('开始执行')
    for i in range(5):
        yield i#将return用yield进行代替返回值
        print('继续执行')
num=numa()
#因为生成器是一遍一遍调用的，圣魔时候用神魔时间取，所以生成器不会连续返回值需要和内置函数next()或for循环配合使用
print(next(num))#开始执行
                # 0#出现这样的情况就是因为yield的影响
print(num.__next__())#继续向下执行，把继续执行打印出来打印到1时又因为yield停止运行

for i in num:
     print(i)
# 1) 首先，在创建有 num 生成器的前提下，通过其调用 next() 内置函数，会使 Python 解释器开始执行 intNum() 生成器函数中的代码，因此会输出“开始执行”，程序会一直执行到yield i，而此时的 i==0，因此 Python 解释器输出“0”。由于受到 yield 的影响，程序会在此处暂停。
#
# 2) 然后，我们使用 num 生成器调用 __next__() 方法，该方法的作用和 next() 函数完全相同（事实上，next() 函数的底层执行的也是 __next__() 方法），它会是程序继续执行，即输出“继续执行”，程序又会执行到yield i，此时 i==1，因此输出“1”，然后程序暂停。
#
# 3) 最后，我们使用 for 循环遍历 num 生成器，之所以能这么做，是因为 for 循环底层会不断地调用 next() 函数，使暂停的程序继续执行，因此会输出后续的结果。

#生成器表达式 ：利用推导的方式获得生成器一次产出一个数据
t=(i*i for i in range(6))
print(next(t))#0
print(next(t))#1
print(next(t))#4
#递归：函数调用自身的过程
#1.函数调用函数
def num2():
    print('duiash')
def num3():
    num2()
    return num2
print(num3())
# duiash
# <function num2 at 0x000001C9DBD6C310>
#函数调用自身的行为非常危险，不加以控制就像一个无限循环一样，一直不停歇地进行下去
#天才和疯子的一线之隔可能就是一个条件语句
def uu1(i):
    if i>0:
        print('djkhud')
        i-=1
        uu1(i)#调用函数自身
uu1(7)
# djkhud
# djkhud
# djkhud
# djkhud
# djkhud
# djkhud
# djkhud
#求一个数的阶乘
#迭代
def uu2(n):
    result=n
    for i in range(1,n):
        result*=i
    return result
print(uu2(3))

#递归的方法--优雅的编程
def uu3(n):
    if n==1:
        return 1
    else:
        return n*uu3(n-1)
print(uu3(3))#6优雅

#名字太长了就叫兔子数列吧
#1.迭代
def uu4(n):
    a=1
    b=1
    c=1
    while n>2:
        c=a+b
        a=b
        b=c
        n-=1
    return c
print(uu4(12))#144
#2.递归
def uu5(n):
    if n==1 or n==2:
        return 1
    else:
        return uu5(n-1)+uu5(n-2)
print(uu5(12))#144

#汉诺塔函数：优雅的递归啊
def ii3(n,a,b,c):
    if n==1:
        print(a,'-',c)#终止条件
    else:
        ii3(n-1,a,c,b)#将第一根上的n-1个圆盘移动到第二根上
        print(a,'-',c)#将第一根上的第n个圆盘移动到第三根上
        ii3(n-1,b,a,c)#将第二根上的n-1个圆盘移动到的三根上
n=int(input('请输入汉诺塔的层数：'))
ii3(n,'x','y','z')

#函数文档：有点像注释但可以通过函数help对其进行访问，从而了解到函数的功能
#编写一个汇率转换的文档
def change(dollor,rate=6.32):
    '''
    功能：汇率的转化
    :param dollor:美元
    :param rate: 汇率，默认值是6.32
    :return: 返回人民币的值
    '''
    return dollor*rate
print()
print(change(20))
help(change)#访问函数文档
#打印内容
# 126.4
# Help on function change in module __main__:
#
# change(dollor, rate=6.32)
#     功能：汇率的转化
#     :param dollor:美元
#     :param rate: 汇率，默认值是6.32
#     :return: 返回人民币的值

#类型注释
def tt(s:str,n:int)->str:#类型注释：后面的str只是希望你把s用字符串进行表示，n用整数类型进行表示
    #：和->str在代码中不参与翻译因为其本身就是注释只是让人看的，机器不进行阅读
    return s*n
print(tt('hqm',3))
#hqmhqmhqm
#当然用户也i可以输入其他的类型
print(tt(5,5))#25
#内省
#高阶函数
#异常捕获异常
try:
    1/0
except:
    print('出错了')#出错了
#try except 捕获异常当异常出现时程序执行except后面的代码，若无异常则不管后面
try:
    1/0
except:
    print('chucuole')
finally:
    print('chumeiekytfgh')

#




















































