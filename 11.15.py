#精确计算浮点数之间的运算。
#引用decimal函数

import decimal
a=decimal.Decimal('0.1')
b=decimal.Decimal('0.2')
print(a+b)

#提取复数的实部和虚部
x=2+2j
print(x.real)#实部
print(x.imag)#虚部

#复数的模，负数的绝对值
c=-250
print(abs(c))
#int（）
#float()
#complex 转化为复数
d=complex(2+2j)
print(d)
#pow(2.3)==2**3可以加入第三个参数，进行取余运算
e=pow(2,3,5)
print(e)#3
#布尔类型的运用来个文字游戏
if bool(250):
    print('250 is ture')
else:
    print('250 is false')#250 is ture

# first_name=input()
# last_name=input()
# full_name=first_name+' '+last_name
# print(full_name)
#if else 的结构语句
a,b=3,5
print(a) if a<b else print(b)

#当然可以写成一个语句
small=a if a<b else b
print(small)

score=66
f=('D' if 0<=score<60 else
   'C' if 60<=score<80 else
   'B' if 80<=score<90 else
   'A' if 90<=score<100else
   '请输入0-100之间的数值：')
print(f)
#恋爱小循环
love='yes'
while love=='yes':
    love=input('今天你还爱我吗？')

i=1
sum=0
while i<=100000:
    sum=sum+i
    i=i+1
print(sum)
while True:
    answer=input('主人，我能退出循环了吗？')
    if answer=='可以':
        break
day=1
while day<=7:
    answer2=input('今天你有好好学习吗？')
    if answer2 !='有':
        break
    day=day+1
else:
    print('恭喜你，已经完成了7天的学习。')


