# range([start,] stop[, step=1])
# 这个BIF（Built-in functions）有三个参数，其中用中括号括起来的两个表示这两个参数是可选的。
# step=1 表示第三个参数的默认值是1。
# range 这个BIF的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列，该序列包含start的值但不包含stop的值。


""" 例子 """
for i in range(2, 9):  # 不包含9
    print(i)

# 2
# 3
# 4
# 5
# 6
# 7
# 8
""" 例子 """
print()
for i in range(1, 10, 2):
    print(i)

# 1
# 3
# 5
# 7
# 9
