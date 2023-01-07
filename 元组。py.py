1.#元组的表达
a=(1,2,3,4)
aa=1,2,3,4
print(a,aa)#(1, 2, 3, 4) (1, 2, 3, 4)
#元组是不可变得，所以元组内的东西不可以改变
#元组同样可以进行切片操作
print(a[3:])
#元组的查count找index
aaa=(1,2,3,4,3)
print(aaa.count(3))
print(aaa.index(3))#查的是第一个3的下标
#元组的一个嵌套
a1=(1,2,3)
a2=(4,5,6)
a3=a1,a2
print(a3)#((1, 2, 3), (4, 5, 6))元组的嵌套
for i in a1:
    print(i)
#循环的嵌套
for i in a3:
    for g in i:
        print(g)#依次打印123456
#列表推导式同样可以运用到元组里面去
b=(1,2,3,4,5,6)
c=[w*2 for w in b]
print(c)#[2, 4, 6, 8, 10, 12]

#拓展问题
x=(520)
print(x,type(x))#520 <class 'int'>
y=(520,)
print(y,type(y))#(520,) <class 'tuple'>
#元组的解包和打包
d=(123,'fishc',[123])
a,b,c=d
print(a, b,c)#123 fishc [123]
e=(1,2,3,4,5,5)
e,f,*g=e
print(e,f,g)#1 2 [3, 4, 5, 5]

x='我爱python'
ee=x.startswith('我')
print(ee)#Ture
eee=x.endswith('python')
print(eee)#Ture
#后面也可以加上开始值和结束值进行判断
eeee=x.startswith('爱',1)
print(eeee)#Ture
##特殊的用法：可以输入多个进行匹配
x='他爱python'
if x.startswith(('你','我','他')):#以元组的形式进行判断
    print('总有人喜欢python')

#判断字符串istitle首字母是否大写，isupper是否全为大写，islower是否全为小写，isalpha是否全为字母有空格的也不算全为字母
xx='I Love python'
f=xx.istitle()
ff=xx.isalpha()
fff=xx.isupper()
ffff=xx.upper().isupper()#从左到右依次进行判断
print(f,ff,fff,ffff)#False False False True
#值得注意的一点字符串中也i有不可打印的值转义字符不进行打印isprintable()是否可打印
#判断是否是保留标识符
import keyword
fffff=keyword.iskeyword('if')
print(fffff)#Ture


#去除空白的操作
t='      左侧不留空白'.lstrip()
tt='右侧不留空白    '.rstrip()
ttt='   zuoyoucedoubuliukongbai    '.strip()
print(t)
print(tt)
print(ttt)

#strip默认删除的是空白也可以删除指定的字符
tttt='www.ilovepython.com'
y=tttt.strip('w.com')
yy=tttt.lstrip('w.com')
yyy=tttt.rstrip('w.com')
print(y,yy,yyy)#ilovepython ilovepython.com www.ilovepython

#removeprefix 删除指定前缀 removesuffix 删除指定后缀
yyyy=tttt.removeprefix('www.')
print(yyyy)#ilovepython.com

#partition分隔符rpartition lpatition
rrr='www.iloceyou.com'.partition('.')
print(rrr)#('www', '.', 'iloceyou.com')

rr='苟日新 日日新 又日新'.split()
print(rr)#['苟日新', '日日新', '又日新']默认分割字符是空格以列表的形式进行返回分成三段
ww='苟日新，日日新，又日新'.split('，')
print(ww)#['苟日新', '日日新', '又日新']
www='苟日新，日日新，又日新'.split('，',1)
print(www)#['苟日新', '日日新，又日新']后面的一表示只切割一次
#2.字符串的拼接join
qq='.'.join(['www','python','com'])
print(qq)#www.python.com#字符串的拼接可以用列表的形式表示，也可以用字符串的形式表示
#当然字符串的拼接以可以使用+来进行拼接，但是当拼接的数量非常多时，join的运算效率要比+快得多
qqq=''.join(['fishc','fishc'])
print(qqq)

#格式化字符串
year=2010
o='yucgonfzuoshichenvliyu{}nian.'.format(year)
oo='2的平方是{},2+1是{},3的立方是{}'.format(2*2,2+1,3*3*3)
print(o)
print(oo)
ooo='nidemingzishi{1}{0}'.format('xioajiayu','piaoliang')
print(ooo)
#如果用默认参数值的话不用考虑其位置
oooo='我叫{name},我爱{fav}'.format(name='小甲鱼',fav='漂亮小姐姐')
print(oooo)
#字符串千位分隔符和加减和空格
g='{:+}{:-}'.format(520,-250)
print(g)
gg='{:,}'.format(12335465)
print(gg)#12,335,465
#精度类型不允许运用在整数上
ggg='{:.2f}'.format(3.142)
print(ggg)#3.14.2f是保留小数点后两位数
gggg='{:.2g}'.format(3.142)
print(gggg)#小数点前后一共保留两位小数








































































