#菱形的制作
n=int(input())
#&与的意思，|或，！非
while n%2==0:
    print('必须输入奇数')
for i in range(1,n//2+2):
    print(' '*(n-i),end='')
    print('*'*(2*i-1))
for i in range(n//2,0,-1):
    print(' '*(n-i),end='')
    print('*'*(2*i-1))
#输出指定范围内的偶数
for i in range(1,10):
    if i%2==0:
        print(i)
#输出99乘法表
for i in range(1,10):
     for j in range(1,i+1):
         if i!=j:
            print(j,'*',i,'=',i*j,end=' ')
         else:
            print(j,'*',i,'=',i*j)
print('')
#石头剪刀布游戏
import random






































































