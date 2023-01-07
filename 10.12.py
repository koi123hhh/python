#字符串的用法
#split分割字符
#1，分割点2，分割次数
#strip去除字符串首尾空格
s1='  a111ab111ac111  '
print(s1.split('a'),3)
print(s1.strip())
print(s1.replace(' ',''))#replace代替字符
#传统字符串输出方法%
#%s;任意字符
#%d;整数
#%f;浮点型
s2='wo%sni'%('ai')
s3='wojinnian%d'%(100)
s4='wozai%f'%(99.9)
print(s2,s3,s4)
#F,f
name='heqimeng'
age='16'
s5='我的名字是{},我今年{}岁'.format(name,age)
s6=F'我的名字是{name},我今年{age}岁'
print(s6)
#len()计算字符串长度
b='nqhurrnfrraoejg'
print(len(b))
#format:.2f 或 :.2%
c='今天句子的价格是{:.2f}'.format(3.1415927)

print(c)
e=3.1415927
f=5.1415927
print('jintiandeshouhuoshi{:.2%}'.format(e,f))
