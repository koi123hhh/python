a=sum(range(3,1000,3))
b=sum(range(7,1000,7))
c=sum(range(21,1000,21))
print(a+b-c)

# a=[i for i in range(3,1001,3)]
# b=[j for j in range(7,1001,7)]
# c=[d for d in range(21,1001,2)]
# #将abc全部的数值打印出来

a=0
for n in range(1,1001):
    if n%3==0 or n%7==0:
        a=a+n
    print(a)












