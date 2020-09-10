# `for`循环是迭代循环，在Python中相当于一个通用的序列迭代器，可以遍历任何有序序列，如`str、list、tuple`等，也可以遍历任何可迭代对象，如`dict.
# 每次循环，迭代变量被设置为可迭代对象的当前元素，提供给代码块使用。

for i in 'ILoveLSGO':
    print(i, end=' ')  # 不换行输出

# I L o v e L S G O
""" 例子 """
print()
member = ['张三', '李四', '刘德华', '刘六', '周润发']
for each in member:
    print(each, end=' ')

# 张三
# 李四
# 刘德华
# 刘六
# 周润发
""" 例子 """
print()
for i in range(len(member)):
    print(member[i], end=' ')

# 张三
# 李四
# 刘德华
# 刘六
# 周润发
""" 例子 """
print()
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key, value in dic.items():
    print(key, value, sep=':', end=' ')

# a:1 b:2 c:3 d:4Î
""" 例子 """
print()
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key in dic.keys():
    print(key, end=' ')

# a b c d
""" 例子 """
print()
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for value in dic.values():
    print(value, end=' ')

# 1 2 3 4
