# `while`语句最基本的形式包括一个位于顶部的布尔表达式，一个或多个属于`while`代码块的缩进语句。
# `while`循环的代码块会一直循环执行，直到布尔表达式的值为布尔假。
# 如果布尔表达式不带有`<、>、==、！=、in、not in`等运算符，仅仅给出数值之类的条件，也是可以的。当`while`后写入一个非零整数时，视为真值，执行循环体；写入`0`时，视为假值，不执行循环体。也可以写入`str、list`或任何序列，长度非零则视为真值，执行循环体；否则视为假值，不执行循环体。
count = 0
while count < 3:
    temp = input("猜一猜小姐姐想的是哪个数字？")
    guess = int(temp)
    if guess > 8:
        print("大了，大了")
    else:
        if guess == 8:
            print("你太了解小姐姐的心思了！")
            print("哼，猜对也没有奖励！")
            count = 3
        else:
            print("小了，小了")
    count = count + 1
print("游戏结束，不玩儿啦！")

# 【例子】布尔表达式返回0，循环终止。
string = 'abcd'
while string:
    print(string)
    # 截取string长度
    string = string[1:]

# abcd
# bcd
# cd
# d
