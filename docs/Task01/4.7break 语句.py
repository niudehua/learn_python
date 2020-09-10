# break语句可以跳出当前所在层的循环。

import random

secret = random.randint(1, 10)  # [1,10]之间的随机数

while True:
    temp = input("猜一猜小姐姐想的是哪个数字？")
    guess = int(temp)
    if guess > secret:
        print("大了，大了")
    else:
        if guess == secret:
            print("你太了解小姐姐的心思了！")
            print("哼，猜对也没有奖励！")
            break
        else:
            print("小了，小了")
print("游戏结束，不玩儿啦！")
