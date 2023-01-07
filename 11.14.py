'''编写一个游戏代码'''

temp=input('猜一下贺琪萌心里想的数是几：')
guess=int(temp)
if guess==8:
    print('猜对了，你真是我肚子里的蛔虫！')
    print('欧，猜对了也没奖励。')
else:
    print('猜错了，我想的是8')
print('游戏结束，不玩了。')

#当然这个游戏太低级 当用户猜错时，程序应该给出提示
aaa=input('猜一下贺琪萌心里想的数是几：')
guess=int(aaa)
if guess==8:
    print('猜对了，你真是我肚子里的蛔虫！')
    print('欧，猜对了也没奖励。')
else:
    if guess<8:
        print('小了，，，')
    else:
        print('大了，，，')
print('游戏结束，不玩了。')

#当然现代人更想玩点花的，至少应该多提供几次几次机会给用户
#此时循环上场
counts=3
while counts>0:
    bbb = input('猜一下贺琪萌心里想的数是几：')
    guess = int(bbb)
    if guess == 8:
        print('猜对了，你真是我肚子里的蛔虫！')
        print('欧，猜对了也没奖励。')
        break
    else:
        if guess < 8:
            print('小了，，，')
        else:
            print('大了，，，')
        counts-=1
print('游戏结束，不玩了。')

#甲方爸爸当然不满意了，就一个数字猜来猜去，一个人猜出来告诉其他人这个游戏就没意思了
#每次执行程序时，答案应该是随机的。
#random的使用调用随机数
import random #将random函数导入进来
ccc=3
ddd=random.randint(1,10)
while counts>0:
    bbb = input('猜一下贺琪萌心里想的数是几：')
    guess = int(bbb)
    if guess == ddd:
        print('猜对了，你真是我肚子里的蛔虫！')
        print('欧，猜对了也没奖励。')
        break
    else:
        if guess < ddd:
            print('小了，，，')
        else:
            print('大了，，，')
        counts-=1
print('游戏结束，不玩了。')

















































































































































