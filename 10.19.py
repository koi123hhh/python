#1.成员检测与标识号检测
#in和 not in后面可以是字符串，元组，列表,字典
#in 如果存在返回ture不存在返回false
print('4' in'1234')##注意后面是字符串的时候前面要是字符串
print(4 in(1,2,3,4))
print(4 in[1,2,3,4])
print('mingzi'in{'mingzi':'heqimeng'})#True字典只能返回键，不能返回值
print('4' not in'1234') #not in和in的用法一样但结果相反
#2.判断那相等于否
#is  is not
#数字 元组 字符串 都是不可变的数据类型， 只要形式上相同就相同
#列表 字典 集合不同 可变的数据类型
a=1
b=1
print(a is b)
aa='111'
bb='111'
print(aa is bb)
#but
aaa=[1,2,3,4,]
bbb=[1,2,3,4,]
print(aaa is bbb)#False
#python的条件语句
#1.if  elif（可以有无数个或0个）  else#注意事项空格冒号
#print(input('请输入你的成绩：'))#99此时该数字是以字符串的形式存在的
#a=int(input('请输入你的成绩：'))
#if a >= 90:
#    print('youxiou')
#elif a >= 80:
#    print('lianghao')
#elif a >= 60:
#   print('jige')
#else:
#    print('bijige')
#2.for循环1
#for不使用下标的方式对列表中的每一个元素进行访问in的后面可以是元组，列表，字典（键），字符串，集合
#遍历数字for >>>in>>range(范围）
for i in[1,2,3]:
    print(i)
for k in range(1,10):#取左不取右10取不到
    print(k)
#for循环2
#对字典的循环直接打印只返回字典中的键，如果都返回用items（）
ff={
    '名字':'贺琪萌',
    '技能':'python'
}
print(ff.items())#dict_items([('名字', '贺琪萌'), ('技能', 'python')])
print(ff)#{'名字': '贺琪萌', '技能': 'python'}
#for j in ff:
 #   print(j)#名字 技能只返回了键
for j in ff.items():
 print(j)#('名字', '贺琪萌') ('技能', 'python')
 #range函数的步长
 #range（0，1）表示从0到一
 #range（0，6，2）最后的2是步长
 print(range(0,6,2))#range(0, 6, 2)如果想要看到步长需要用到for循环语句
 for g in range(0,7,2):
     print(g)#0246
 #for循环语句拿到元组内部的东西if  isinstance()
 #isinstance()判断数据类型
 bbbb=(1,2,3,[10,20,30],[40,50,60])
 for i in bbbb:
    # print(i)
     if isinstance(i,list):
         for d in i :
           print(d)#提取列表中的元素注意事项最后的print中的要在f的后面要凸显出层次

#if为判断语句while为循环语句while可以单独使用也i可以配合else一起使用
ccc=0
while ccc<6:
    print('我爱你')
    ccc+=1
else:
    print('我腻了，不爱你了哈哈')
#break和continue可以跳过for和while循环
#continue用于跳过当前循环中的语句，继续执行剩余的元素
v='python'
for ii in v:

    print(ii)
    break #p
    #break和continue住一起摆放位置放前放后不一样
for gg in v:
    print('我爱你')#打印了6个我爱你
    continue
    print(gg)#跳过了python的打印
#在while循环中的运用
vvv=0
while vvv<6:
  print('我是贺琪萌')
  vvv += 1
  break #只打印一个我是贺琪萌被被迫停止#如果这个地方写continue的话会打印6个我是贺琪萌
#break和continue的区别break结束语句循环被打破了被迫停止
#continue是跳过剩余的语句剩余语句不起作用，但是不影响前面的循环
#如果加上if
ss=0
while ss<6:
    ss+=1
    if ss==3:
     continue
    print(ss)#12(break)跳出循环#12456(continue)跳过ss=3中的语句
nn=0
#while nn<6:
    #if nn==3:
     #continue
    #print(nn)
    #nn+=1#break和continue(012)#之所以只打印了012是因为在nn==3时nn+=1在continue后面被隔断无法继续运行如果nn+=i放在if前面打印01245
ggg=0
while ggg<6:
    ggg+=1
    if ggg == 3:
        continue
    print(ggg)#12456
#pass#想不起来写啥了放一会有为了防止报错放一个pass













