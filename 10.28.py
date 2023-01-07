#函数的返回值return
#用于帮助处理我们处理完的函数值，也i可以不用return进行返回则默认返回None
#return返回是借助元组形式进行返回
def aaa():
    print('nihao')
r=aaa()
print(r)#None
def bbb(a,b):
    return(a*b)
#s=bbb(1,2)#2
s=bbb('1',2)
print(s,type(s))#11 <class 'str'>
#return将后边的函数进行调用注意自符串和数字对于*的不同意义tuple元组的英文标识
#配合元组的解包
def ccc(a,b,c):
    return a+100,b+200,c+300
r=ccc(100,200,300)
print(r)

x,y,z=r#配合解包使用
print(x)
print(y)
print(z)

# input('请输入你的名字：')
# if input('zhaotong'):
#     print('3')
# else:
#     print('1')
#请输入你的名字：zhoaotng/'zhaotong'
# 你好
# 1
#应该是数据类型不同input以str的形式输出但是还是不太懂
print('猜猜余沐林 的年龄：')
a=3
b= int(input())
print(type(a))
print(type(b))
if a>=b:
     print('恭喜你猜对了，这货心理年龄也就这个数了')
else:
   print('你太高估了奥')







