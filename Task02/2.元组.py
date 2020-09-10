"""
1.元组的定义
"""
# 「元组」定义语法为：(元素1, 元素2, ..., 元素n)
#
# 小括号把所有元素绑在一起
# 逗号将每个元素一一分开

""" 
2.创建和访问一个元组
"""
# Python 的元组与列表类似，不同之处在于tuple被创建后就不能对其进行修改，类似字符串。
# 元组使用小括号，列表使用方括号。
# 元组与列表类似，也用整数来对它进行索引 (indexing) 和切片 (slicing)。
""" 例子 """
t1 = (1, 10.31, 'python')
t2 = 1, 10.31, 'python'
print(t1, type(t1))
# (1, 10.31, 'python') <class 'tuple'>

print(t2, type(t2))
# (1, 10.31, 'python') <class 'tuple'>

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[1])  # 2
print(tuple1[5:])  # (6, 7, 8)
print(tuple1[:5])  # (1, 2, 3, 4, 5)
tuple2 = tuple1[:]
print(tuple2)  # (1, 2, 3, 4, 5, 6, 7, 8)

# 创建元组可以用小括号()，也可以什么都不用，为了可读性，建议还是用()。
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用。
""" 例子 """
print()
x = (1)
print(type(x))  # <class 'int'>
x = 2, 3, 4, 5
print(type(x))  # <class 'tuple'>
x = []
print(type(x))  # <class 'list'>
x = ()
print(type(x))  # <class 'tuple'>
x = (1,)
print(type(x))  # <class 'tuple'>

""" 例子 """
print()
print(8 * (8))  # 64
print(8 * (8,))  # (8, 8, 8, 8, 8, 8, 8, 8)

""" 例子 创建二维元组。 """
print()
x = (1, 10.31, 'python'), ('data', 11)
print(x)
# ((1, 10.31, 'python'), ('data', 11))

print(x[0])
# (1, 10.31, 'python')
print(x[0][0], x[0][1], x[0][2])
# 1 10.31 python

print(x[0][0:2])
# (1, 10.31)

"""
3.更新和删除一个元组
"""
""" 例子 """
print()
week = ('Monday', 'Tuesday', 'Thursday', 'Friday')
week = week[:2] + ('Wednesday',) + week[2:]
print(week)  # ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

""" 例子 元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值，但是只要元组中的元素可更改 (mutable)，那么我们可以直接更改其元素，注意这跟赋值其元素不同。"""
print()
t1 = (1, 2, 3, [4, 5, 6])
print(t1)  # (1, 2, 3, [4, 5, 6])

t1[3][0] = 9
print(t1)  # (1, 2, 3, [9, 5, 6])

"""
4.元组相关的操作符
"""
# 等号操作符：==
# 连接操作符 +
# 重复操作符 *
# 成员关系操作符 in、not in
#
# 「等号 ==」，只有成员、成员位置都相同时才返回True。
#
# 元组拼接有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。
""" 例子 """
print()
t1 = (123, 456)
t2 = (456, 123)
t3 = (123, 456)

print(t1 == t2)  # False
print(t1 == t3)  # True

t4 = t1 + t2
print(t4)  # (123, 456, 456, 123)

t5 = t3 * 3
print(t5)  # (123, 456, 123, 456, 123, 456)

t3 *= 3
print(t3)  # (123, 456, 123, 456, 123, 456)

print(123 in t3)  # True
print(456 not in t3)  # False

"""
5.内置方法
"""
# 元组大小和内容都不可更改，因此只有 count 和 index 两种方法。
""" 例子 """
print()
t = (1, 10.31, 'python')
print(t.count('python'))  # 1
print(t.index(10.31))  # 1
# count('python') 是记录在元组 t 中该元素出现几次，显然是 1 次
# index(10.31) 是找到该元素在元组 t 的索引，显然是 1


"""
6.解压元组
"""
""" 例子 解压（unpack）一维元组（有几个元素左边括号定义几个变量）"""
print()
t = (1, 10.31, 'python')
(a, b, c) = t
print(a, b, c)
# 1 10.31 python

""" 例子 解压二维元组（按照元组里的元组结构来定义变量） """
print()
t = (1, 10.31, ('OK', 'python'))
(a, b, (c, d)) = t
print(a, b, c, d)
# 1 10.31 OK python

""" 例子  如果你只想要元组其中几个元素，用通配符「*」，英文叫 wildcard，在计算机语言中代表一个或多个元素。下例就是把多个元素丢给了 rest 变量。 """
print()
t = 1, 2, 3, 4, 5
a, b, *rest, c = t
print(a, b, c)  # 1 2 5
print(rest)  # [3, 4]

""" 例子 如果你根本不在乎 rest 变量，那么就用通配符「*」加上下划线「_」。 """
print()
t = 1, 2, 3, 4, 5
a, b, *_ = t
print(a, b)  # 1 2
print(_)
