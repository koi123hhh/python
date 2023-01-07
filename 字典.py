#6种字典创建的方法
#1。
a={'xingming':'heqimeng','jineng':'python'}#大通用
print(a['xingming'])
b=dict(吕布='口口布',关羽='关西西',刘备='刘贝贝')
print(b['刘备'])
c=dict([('liubu','enenn')])
#字典的增删改除增
d=dict.fromkeys('fish',250)
print(d)
#改
d.update({'i':80,'c':90})#使用update可以一次修改多个键值对
print(d)
d['f']=90
print(d)
#如果原来有则覆盖进去，如果没有则添加进去
#{'f': 250, 'i': 250, 's': 250, 'h': 250}
#{'f': 90, 'i': 250, 's': 250, 'h': 250}
d['g']=500
print(d)
#{'f': 90, 'i': 250, 's': 250, 'h': 250, 'g': 500}
#删
d.pop('s')
print(d)
#{'f': 90, 'i': 250, 'h': 250, 'g': 500}
#如果删除的是字典中不存在的数则会抛出异常
#popitem删除字典中最后一个键值对删除
d.popitem()
print(d)
#如果删除字典中全部的键值对使用clear







































