#函数参数顺序
def aaa(a,name='heqimeng',*args,**kwargs):
    print(a)
    print(name)
    print(args)#(100, 200, 300)
    print(kwargs)#{'b': 300, 'c': 400, 'd': 500}
aaa(100,'liuhanyue',100,200,300,b=300,c=400,d=500)
#通常情况下该函数常配合for in进行使用
def bbb(*args):

    for i in (args):
        print(i)#遍历所有的值
bbb(100,200,300)

#def ccc(**kwargs):
    # for f in kwargs:
    #     print(kwargs)
#ccc(x=100,y=200)
#{'x': 100, 'y': 200}
#分别取键值
def ddd(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
ddd(x=200,y=300)

# x
# 200
# y
# 300
