i=1
while i<=9:
    j=i

    if j<=9:
        print(i*j)
        j=j+1
    i=i+1

c=1
while c<=9:
    b=1
    while b<=c:
        print(b,'*',c,'=',b*c,end=' ')
        b=b+1
    print()
    c=c+1

#将FISHC这几个字符依次打印出来运用循环
# for d in 'FISHC':
#     print(d)
#
# e=0
# while e<=len('FISHC'):
#     print('FISHC'[e])
#     e=e+1

#陪for出生入死的好兄帝range
for f in range(10):
    print(f)


for g in range(1,9):
    print(g)

for h in range(1,9,2):
    print(h)

#利用for循环来计算10000以内的数字的和
sum=0
for j in range(10000):#但是这个结果是错的，range也是取前不取后
    sum+=j
print(sum)

#将1到10之间的素数打印出来
for k in range(2,10):
    for x in range(2,k):
        if k%x==0:
            print(k,'=',x,'*',k//x)
            break
    else:
        print(k,'这是一个素数。')#else只有当循环正常进行时才会执行



#列表的增删改查
heros=['钢铁侠','绿巨人']
print(heros.append('黑寡妇'))

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='')
    if i!=9:
        print()

















































