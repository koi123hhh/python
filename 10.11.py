#慕州老师字符串讲解19
#切片
#[开始:结束]
name="xiaoxiannv"
#print(name[0:3])
#切片[开始：结束：步长]
#print(name[::-1])#倒置
#字符串的拼接
#a='woshiheqimeng'
#b='woshiliuhanyue'
#c='wojintianhenkaixin'
#d=a+b+c#直接写字母不加引号
#print(d)
#字符串的格式化format
a='大家好，我是{},今年{}岁'.format('heqimeng' ,'16')
#print(a)
#寻找字符串
#find找数
#count数数
a='pythonheqimengooo'
print(a.find('o',6,18))
print(a.count('o'))
#找不到返回-1
#字符串的替换
b=a.replace('o','TT',2)#数字代表替换几个

print(b)
#upper小写换成大写
#lower大写转小写