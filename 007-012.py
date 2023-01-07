#列举数字范围内所有的偶数
def qiuou(begin,end):
    result=[]
    for i in range(begin,end+1):
        if i%2==0:
            result.append(i)
    return result
print(qiuou(1,10))
#也可以运用列表推导式的方法更加简单
date=[item for item in range(1,11)if item%2==0]
print(date)
#8.移除列表中多个元素
def yichu(list1,list2):
    for i in list2:
        list1.remove(i)#从列表中移除多个元素用remove移除一个用pop()
    return list1
lista=[3,5,7,9,11,13]
listb=[7,11]
print(yichu(lista,listb))
#列表推导式的运用
date1=[item for item in lista if item not in listb]
print(date1)
#9.对列表中的元素进行去重
def quchong(list1):
    result=[]
    for i in list1:
        if i not in result:
            result.append(i)
    return result

listc=[1,1,2,3,4,1,]
print(quchong(listc))
#借用集合的去重性
print(list(set(listc)))#只需要一行代码即可
#对简单列表进行排序升序降序的运用
#正序的排列
listaa=[10,20,30,15,25,5]
#listaa.sort(reverse=Ture)
#print(listaa)该方法比较简单,但是改变了原列表
listbb=sorted(listaa,reverse=True)#该种方法未改变listaa这个原列表
print(listbb)
#sort/sorted都有一个默认值reverse=Flase
#11.实现学生成绩的排序
students=[
    {'sno':101,'sname':'小王','sgrade':88},
    {'sno':102,'sname':'小赵','sgrade':99},
    {'sno':103,'sname':'小钱','sgrade':77},
    {'sno':104,'sname':'小孙','sgrade':66},
]
chengjipaixu=sorted(students,key=lambda x:x['sgrade'],reverse=True)
print(chengjipaixu)#lambda的应用后面加一个参数:参数对应表达式和def的作用一样但后面只能加一个表达式,而def可以定义较为复杂函数
#12读取成绩文件排序数据
def readfile():
    result=[]
    with open('../Python实践/chengjiwenjian.txt') as fin:#打开文件的便捷方法,只有在with中才能打开文件
        for line in fin:
            line=line[:-1]
            result.append(line.split(','))
    return result
def sortgrade(datas):
    return sorted(datas,
                  key=lambda x:int(x[2]),
                  reverse=True)
def writefile(datas):
    with open('./成绩文件输出','w') as fout:
        for data in datas:
            fout.write(','.join(data)+'\n')
datas=readfile()
datas=sortgrade(datas)
writefile(datas)