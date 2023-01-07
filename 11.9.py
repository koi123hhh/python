#天天向上
#1.天天向上/下0.001
import math
dayup=math.pow((1+0.01),365)
daydown=math.pow((1-0.01),365)
print('向上：{:.3f},向下：{:.3f}'.format(dayup,daydown))
#2.天天向上/下0.005
import math
dayup=math.pow((1+0.05),365)
daydown=math.pow((1-0.05),365)
print('向上:{:.2f},向下:{:.2f}'.format(dayup,daydown))
#3.周末休息
dayup,dayfactor=1.0,0.01
for i in range(365):
    if i%7 in[6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print('向上五天向下两天的力量：{:.2f}'.format(dayup))






#pk版
def dayUp(dayfactor):
    dayup=1.0
    for i in range(356):
        if i%356 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+dayfactor)
    return dayup
dayfactor=0.01
while(dayUp(dayfactor)<37.78):
    dayfactor+=0.001
print('每天努力的参数是:{:.3f}'.format(dayfactor))


s,idx='hjajdfl' ,0
while idx<len(s):
    print('循环进行中:' +s[idx])
    idx+=1
else:
    print('循环结束')


#break和continue的区别和联系
for s in 'python':
    if s=='t':
        continue
    print(s,end='')#end不换行
else:
    print('正常退出')#pyhon正常退出


for aaa in 'python':
    if aaa=='t':
        break
    print(aaa,end='')#py
else:
    print('正常结束')


from random import random
from math import sqrt

s=1000000
n=0

for i in range(int(s)):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1:
        n=n+1
pi=4*(n/s)
print('pi的值是:{}'.format(pi))







