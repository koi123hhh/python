#字典的操作方法
#clear函数清楚字典中的元素
#copy函数创建副本改变原字典中的元素对副本无影响
a={
    '名字':'贺琪萌',
    '年龄':'17'
}
a.clear()
print(a)
b={
    'mingzi':'heqimeng',
    'nianling':'17'
}
del b['mingzi']
s1=b.copy()
#
print(s1)
#2.fromkeys用于创建新的字典
#第一个序数对应着键，第二个序数对应的是每个键的值
c={}
d=c.fromkeys(('mingzi','nianling'),(18))#{'mingzi': 18, 'nianling': 18}
e=c.fromkeys(('mingzi','nianling'),(1,2))#{'mingzi': (1, 2), 'nianling': (1, 2)}
print(d)
print(e)
#3.pop函数从字典中移除指定值但有返回值返回字典中的键对应的值
f={
    'mingzi':'heqimeng',
    'nianling':17
}
s4=f.pop('mingzi')
print(f)#{'nianling': 17}
print(s4)#heqimeng
#4.popitem函数
#删除字典中的最后一项并且以元组的形式返回该项的键和值
g={
    'mingzii':'muzhou',
    'nianling':17
}
r=g.popitem()
print(g)#{'mingzii': 'muzhou'}
print(r)#('nianling', 17)
#5.setdefault官方说法设置键的默认值通俗点讲添加字典中的元素

g1={
    'mingzii':'muzhou',
    'nianling':17
}
g1.setdefault('jineng','python')
print(g1)
#若是字典中已经有相同的键则忽略该操作
g1.setdefault('mingzii','xiaoming')#{'mingzii': 'muzhou', 'nianling': 17, 'jineng': 'python'}
print(g1)
#补充一点如是字典中有两个键相同则采取覆盖原则只打印最后一个
g2={
    'mingzi':'heqimeng',
    'mingzi':'xiaoming'
}
print(g2)#{'mingzi': 'xiaoming'}
#5.字典的更新update
#如果键相等，则更改
#如果不相等则添加
k1={
    'mingzi':'heqimeng'
}
k2={
    'mingzi':'muzhou'
}
k3={
    'nianling':17
}
k1.update(k2)
print(k1)#{'mingzi': 'muzhou'}
k1.update(k3)
print(k1)#{'mingzi': 'muzhou', 'nianling': 17}