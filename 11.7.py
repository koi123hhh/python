#计算圆的周长和面积
r=eval(input('请输入半径'))#进字符串进行函数调用
S=3.1415*r*r
C=2*3.1415*r
print(S,C)
# #计算绝对值
# a=eval(input('请输入数字：'))
# if a<0:
#    a=-a
# print(a)
#累加求和
# R=eval(input('输入数字'))
# i,s=0,0
# while i<=R:
#      s=s+i
#      i=i+1
# print(s)#注意缩进符的运用print靠边写，这是和while一阶的。
#if语句
P=eval(input('请输入PM2.5的值：'))
if P>=75:
     print('空气污染警告')
if 35<=P<75:
     print('空气质量良，适合外出')
if P<35:
     print('空气质量优，适合外出旅游')

if 'PYTHON'>'python':
     print('ture')
else:
     print('fasle')
a='PYTHON'
b='python'
print('ture' if a>b else'false')#if else的紧凑结构
p=eval(input('请输入pm2.5的值：'))
print('空气{}污染'.format('存在'if p>=75 else'不存在'))

#pmi指标
weight,height=eval(input('你的身高（米）和体重（千克）是[请用，隔开]:'))
bmi=weight/pow(height,2)
print('BMI的数值为{:.2f}'.format(bmi))
who,dom='',''
if bmi<18.5:
     who,dom='偏瘦','偏瘦'
elif 18.5<=bmi<=25:
     who,dom='正常','正常'
else:
     who,dom='偏胖','偏胖'
print('你的国际bmi为{0},你的国内bmi为{1}'.format(who,dom))





