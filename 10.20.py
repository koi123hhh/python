#显示数据类型type
a='123'
b=123
c=[1,2,3]
d={
    '名字':'贺琪萌'
}
e=(1,2,3)
print(type(a))#<class 'str'>-->表示字符串
print(type(b))#<class 'int'>
print(type(c))#<class 'list'>
print(type(d))#<class 'dict'>
print(type(e))#<class 'tuple'>
#python数字类型的强制转换1.str将其他数据类型转换为字符串类型
f='123'
sedffr=str(f)
print(sedffr,type(sedffr))#123 <class 'str'>
#数字类型的强制转换int() 转化为整型  float（）转化为浮点型
#注意类型1.只有数字之间可以相互转换2.字符串转化时里面必须是整数可正可负，小数会报错
#3.浮点型化整形时不遵循四舍五入原则直接去点小数点后面的元素
aa=12.33
s_a=int(aa)
print(s_a)#12
bb=12
s_b=float(bb)
print(s_b)#12.0
#数据类型强制转换为布尔值bool
#1.容器类型 列表，元组，集合，字符串，字典，和非容器类类型数字，布尔值
#容积为空False,里面有元素返回Ture
#数字类型转化为布尔值时除了0 0.0返回F外其余都返回T
dd=''
ddd=[]
s_d=bool(ddd)
print(s_d)
#数字类型强制转换List和tuple元组类型一样
#非容器类型无法转换
#元组，集合，字符串转化时其里面的每一个元素转化为列表中的元素
#字典转化只转化键
#集合转化时是无序的因为集合本身就是无序的
ee='12345678'
print(list(ee))#['1', '2', '3', '4', '5', '6', '7', '8']
ff={1,23,4,5,3,4,}#[1, 3, 4, 5, 23]
print(list(ff))
#数字类型的强制转换转化为集合set（）
#数字类型无法转换其他容器类型转化是都是无序的
#数字类型强植转换为字典dict()
#集合，字符串，非容器类型无法转化为字符串
#元组和列表转化为字符串时必须为二级容器且每个容器中必须有两个元素
aaa=[[1,0],['名字','贺琪萌']]
print(dict(aaa))#{1: 0, '名字': '贺琪萌'}
#isinstance函数返回布尔值用于判断函数的类型
#isinstance(对象，对象类型）
#如果对象类型正确或对象类型用元组表示只要元组中有对象对应的类型也返回Ture
aaaa=123
print(isinstance(aaaa,int))
print(isinstance(aaaa,(int,float,dict)))#两个都是Ture















