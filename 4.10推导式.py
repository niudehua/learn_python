"""
列表:[1, 2, 3, 4, 5, 6]
元祖:(1, 2, 3, 4, 5, 6)
字典:{1: 1, 2: 2, 3: 3, 4: 4}
集合:{1, 2, 3, 4, 5, 6}
"""
# 列表推导式
# [ expr for value in collection [if condition] ]
""" 例子 """
x = [-4, -2, 0, 2, 4]
y = [a * 2 for a in x]
print(y)
# [-8, -4, 0, 4, 8]

""" 例子 """
print()
x = [i ** 2 for i in range(1, 10)]
print(x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

""" 例子 """
print()
x = [(i, i ** 2) for i in range(6)]
print(x)
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

""" 例子 """
print()
x = [i for i in range(100) if (i % 2) != 0 and (i % 3) == 0]
print(x)
# [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]

""" 例子 """
print()
a = [(i, j) for i in range(0, 3) for j in range(0, 3)]
print(a)
""" 
a = []
for i in range(0, 3):
    for j in range(0, 3):
        a.append((i, j))
print(a)
"""
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

""" 例子 """
print()
x = [[i, j] for i in range(0, 3) for j in range(0, 3)]
print(x)
# [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
x[0][0] = 10
x[0][1] = 99
print(x)
# [[10, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

""" 例子 """
print()
# a = [(i, j) for i in range(0, 3) if i < 1 for j in range(0, 3) if j > 1]
# print(a)
# """
a = []
for i in range(0, 3):
    if i < 1:
        for j in range(0, 3):
            if j > 1:
                a.append((i, j))
print(a)
# """
# [(0, 2)]


# 元组推导式
# ( expr for value in collection [if condition] )
""" 例子 """
print()
a = (x for x in range(10))
print(a)
# <generator object <genexpr> at 0x0000025BE511CC48>
print(tuple(a))

# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 字典推导式
# { key_expr: value_expr for value in collection [if condition] }
""" 例子 """
print()
b = {i: i % 2 == 0 for i in range(10) if i % 3 == 0}
print(b)
"""
b = {}
for i in range(10):
    if i % 3 == 0:
        b.update({i: i % 2 == 0})
print(b)
"""
# {0: True, 3: False, 6: True, 9: False}

# 集合推导式
# { expr for value in collection [if condition] }
""" 例子 """
print()
c = {i for i in [1, 2, 3, 4, 5, 5, 6, 4, 3, 2, 1]}
print(c)
# {1, 2, 3, 4, 5, 6}

# 其它
"""
next(iterator[, default]) 迭代器
Return the next item from the iterator.
If default is given and the iterator is exhausted, it is returned instead of raising Stop Iteration.
"""
print()
e = (i for i in range(10))
print(e)
# <generator object <genexpr> at 0x0000007A0B8D01B0>
print(next(e))  # 0
print(next(e))  # 1
for each in e:
    print(each, end=' ')
print()
# 2 3 4 5 6 7 8 9

""" 例子 """
print()
s = sum([i for i in range(101)])
print(s)  # 5050
s = sum((i for i in range(101)))
print(s)  # 5050
