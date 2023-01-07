#13.统计学生成绩最高分,最低分和平均分
'''
def computescore():
    scores=[]
    with open('../Python实践/chengjiwenjian.txt') as fin:
        for line in fin:
            line=line[:-1]
            fields=line.split(',')
            scores.append(int(fields[-1]))
    maxscore=max(scores)
    minscore=min(scores)
    avgscore=sum(scores)/len(scores)
    return maxscore,minscore,avgscore
maxscore,minscore,avgscore=computescore()
print(f'maxscore={maxscore},minscore={minscore},avgscore={avgscore}')
'''
#14.统计英文文章每个单词的出现次数
wordcount={}
with open('./yingwenwenchang.txt','rb') as fin:
    for line in fin:
        line=line[:-1]
        words=line.split( )
        for word in words:
            if word not in wordcount:
                wordcount[word]=0
            wordcount[word]+=1

print(
    sorted(
        wordcount.items(),
        key=lambda x:x[1],
        reverse=True
    )[:10]
)
#15.python统计文剪下的数字大小
import os
print(os.path.getsize('yingwenwenchang.txt'))
#计算目录下所有文件的大小
sumsize=0
for file in os.listdir('.'):
    if os.path.isfile(file):
        sumsize+=os.path.getsize(file)
print(sumsize/1024)
#16.按照文件的后缀名来整理文件

for s in 'baseball':
    if s=='b':
        break
print(s,end='')

print(pow(3,0.5)*pow(3,0.5)==3)
print('a'<'b'<'c')

s=1
while s<=1:
    print(s)
    s+=1


for i in range(1,8):
    if i%4==0:
        break
    else:
        print(i,end=',')












