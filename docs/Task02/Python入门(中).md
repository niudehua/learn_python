---


<h1>Python入门(中)</h1>

1. [简介](#简介)

2. [列表](#列表)<br>
   [1. 列表的定义](#1.列表的定义)<br>
   [2. 列表的创建](#2.列表的创建)<br>
   [3. 向列表中添加元素](#3.向列表中添加元素)<br>
   [4. 删除列表中的元素](#删除列表中的元素)<br>
   [5. 获取列表中的元素](#获取列表中的元素)<br>
   [6. 列表的常用操作符](#列表的常用操作符)<br>
   [7. 列表的其它方法](#列表的其它方法)<br>    

3. [元组](#元组)<br>
   [1. 创建和访问一个元组](#1.-创建和访问一个元组)<br>
   [2. 更新和删除一个元组](#2.-更新和删除一个元组)<br>
   [3. 元组相关的操作符](#3.-元组相关的操作符)<br>
   [4. 内置方法](#4.-内置方法)<br>
   [5. 解压元组](#5.-解压元组)<br>
   
4. [字符串](#字符串)<br>
   [1. 字符串的定义](#1.-字符串的定义)<br>
   [2. 字符串的切片与拼接](#2.-字符串的切片与拼接)<br>
   [3. 字符串的常用内置方法](#3.-字符串的常用内置方法)<br>
   [4. 字符串格式化](#4.-字符串格式化)<br>
   
5. [字典](#字典)<br>
   [1. 可变类型与不可变类型](#1.-可变类型与不可变类型)<br>
   [2. 字典的定义](#2.-字典的定义)<br>
   [3. 创建和访问字典](#3.-创建和访问字典)<br>
   [4. 字典的内置方法](#4.-字典的内置方法)<br>
   
6. [集合](#集合)<br>
   [1. 集合的创建](#1.-集合的创建)<br>
   [2. 访问集合中的值](#2.-访问集合中的值)<br>
   [3. 集合的内置方法](#3.-集合的内置方法)<br>
   [4. 集合的转换](#4.-集合的转换)<br>
   [5. 不可变集合](#5.-不可变集合)<br>
   
7. [序列](#序列)<br>
   [1. 针对序列的内置函数](#1.-针对序列的内置函数)<br>


## 简介

Python 是一种通用编程语言，其在科学计算和机器学习领域具有广泛的应用。如果我们打算利用 Python 来执行机器学习，那么对 Python 有一些基本的了解就是至关重要的。本 Python 入门系列体验就是为这样的初学者精心准备的。

**本实验包括以下内容**

1. 列表
    - 列表的定义
    - 列表的创建
    - 向列表中添加元素
    - 删除列表中的元素
    - 获取列表中的元素
    - 列表的常用操作符
    - 列表的其他方法
2. 元组
    - 创建和访问一个元组
    - 更新和删除一个元组
    - 元组相关的操作符
    - 内置方法
    - 解压元组
3. 字符串
    - 字符串的定义
    - 字符串的切片与拼接
    - 字符串的常用内置方法
    - 字符串格式化
4. 字典
    - 可变类型与不可变类型
    - 字典的定义
    - 创建和访问字典
    - 字典的内置方法
5. 集合
    - 集合的创建
    - 访问集合中的值
    - 集合的内置方法
    - 集合的转换
    - 不可变集合
6. 序列
    - 针对序列的内置函数

## 列表

简单数据类型
- 整型`<class 'int'>`
- 浮点型`<class 'float'>`
- 布尔型`<class 'bool'>`

容器数据类型
- 列表`<class 'list'>`
- 元组`<class 'tuple'>`
- 字典`<class 'dict'>`
- 集合`<class 'set'>`
- 字符串`<class 'str'>`

### 1. 列表的定义

列表是有序集合，没有固定大小，能够保存任意数量任意类型的 Python 对象，语法为 `[元素1, 元素2, ..., 元素n]`。

- 关键点是「中括号 []」和「逗号 ,」
- 中括号 把所有元素绑在一起
- 逗号 将每个元素一一分开



### 2. 列表的创建

- 创建一个普通列表

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(x, type(x))
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] <class 'list'>

x = [2, 3, 4, 5, 6, 7]
print(x, type(x))
# [2, 3, 4, 5, 6, 7] <class 'list'>
```

- 利用`range()`创建列表

【例子】 

```python
x = list(range(10))
print(x, type(x))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

x = list(range(1, 11, 2))
print(x, type(x))
# [1, 3, 5, 7, 9] <class 'list'>

x = list(range(10, 1, -2))
print(x, type(x))
# [10, 8, 6, 4, 2] <class 'list'>
```

- 利用推导式创建列表

【例子】 

```python
x = [0] * 5
print(x, type(x))
# [0, 0, 0, 0, 0] <class 'list'>

x = [0 for i in range(5)]
print(x, type(x))
# [0, 0, 0, 0, 0] <class 'list'>

x = [i for i in range(10)]
print(x, type(x))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

x = [i for i in range(1, 10, 2)]
print(x, type(x))
# [1, 3, 5, 7, 9] <class 'list'>

x = [i for i in range(10, 1, -2)]
print(x, type(x))
# [10, 8, 6, 4, 2] <class 'list'>

x = [i ** 2 for i in range(1, 10)]
print(x, type(x))
# [1, 4, 9, 16, 25, 36, 49, 64, 81] <class 'list'>

x = [i for i in range(100) if (i % 2) != 0 and (i % 3) == 0]
print(x, type(x))

# [3, 9, 15, 21, 27, 33, 39,
```

注意：

由于list的元素可以是任何对象，因此列表中所保存的是对象的指针。即使保存一个简单的`[1,2,3]`，也有3个指针和3个整数对象。

`x = [a] * 4`操作中，只是创建4个指向list的引用，所以一旦`a`改变，`x`中4个`a`也会随之改变。

【例子】

```python
x = [[0] * 3] * 4
print(x, type(x))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] <class 'list'>

x[0][0] = 1
print(x, type(x))
# [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]] <class 'list'>

a = [0] * 3
x = [a] * 4
print(x, type(x))
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]] <class 'list'>

x[0][0] = 1
print(x, type(x))
# [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]] <class 'list'>
```

- 创建一个混合列表

【例子】 

```python
mix = [1, 'lsgo', 3.14, [1, 2, 3]]
print(mix, type(mix))  
# [1, 'lsgo', 3.14, [1, 2, 3]] <class 'list'>
```

- 创建一个空列表

【例子】 

```python
empty = []
print(empty, type(empty))  # [] <class 'list'>
```

列表不像元组，列表内容可更改 (mutable)，因此附加 (`append`, `extend`)、插入 (`insert`)、删除 (`remove`, `pop`) 这些操作都可以用在它身上。


### 3. 向列表中添加元素

- `list.append(obj)` 在列表末尾添加新的对象，只接受一个参数，参数可以是任何数据类型，被追加的元素在 list 中保持着原结构类型。

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.append('Thursday')
print(x)  
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Thursday']

print(len(x))  # 6
```

此元素如果是一个 list，那么这个 list 将作为一个整体进行追加，注意`append()`和`extend()`的区别。

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.append(['Thursday', 'Sunday'])
print(x)  
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ['Thursday', 'Sunday']]

print(len(x))  # 6
```

- `list.extend(seq)` 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.extend(['Thursday', 'Sunday'])
print(x)  
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Thursday', 'Sunday']

print(len(x))  # 7
```

严格来说 `append` 是追加，把一个东西整体添加在列表后，而 `extend` 是扩展，把一个东西里的所有元素添加在列表后。

- `list.insert(index, obj)` 在编号 `index` 位置插入 `obj`。

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.insert(2, 'Sunday')
print(x)
# ['Monday', 'Tuesday', 'Sunday', 'Wednesday', 'Thursday', 'Friday']

print(len(x))  # 6
```

### 4. 删除列表中的元素
- `list.remove(obj)` 移除列表中某个值的第一个匹配项

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x.remove('Monday')
print(x)  # ['Tuesday', 'Wednesday', 'Thursday', 'Friday']
```

- `list.pop([index=-1])` 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y = x.pop()
print(y)  # Friday

y = x.pop(0)
print(y)  # Monday

y = x.pop(-2)
print(y)  # Wednesday
print(x)  # ['Tuesday', 'Thursday']
```

`remove` 和 `pop` 都可以删除元素，前者是指定具体要删除的元素，后者是指定一个索引。

- `del var1[, var2 ……]` 删除单个或多个对象。

【例子】

如果知道要删除的元素在列表中的位置，可使用`del`语句。

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
del x[0:2]
print(x)  # ['Wednesday', 'Thursday', 'Friday']
```

如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用`del`语句；如果你要在删除元素后还能继续使用它，就使用方法`pop()`。


### 5. 获取列表中的元素

- 通过元素的索引值，从列表获取单个元素，注意，列表索引值是从0开始的。
- 通过将索引指定为-1，可让Python返回最后一个列表元素，索引 -2 返回倒数第二个列表元素，以此类推。

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', ['Thursday', 'Friday']]
print(x[0], type(x[0]))  # Monday <class 'str'>
print(x[-1], type(x[-1]))  # ['Thursday', 'Friday'] <class 'list'>
print(x[-2], type(x[-2]))  # Wednesday <class 'str'>
```

切片的通用写法是 `start : stop : step`

- 情况 1 - "start :" 
- 以 `step` 为 1 (默认) 从编号 `start` 往列表尾部切片。

【例子】

```python
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(x[3:])  # ['Thursday', 'Friday']
print(x[-3:])  # ['Wednesday', 'Thursday', 'Friday']
```

- 情况 2 - ": stop"
- 以 `step` 为 1 (默认) 从列表头部往编号 `stop` 切片。

【例子】

```python
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[:3])  # ['Monday', 'Tuesday', 'Wednesday']
print(week[:-3])  # ['Monday', 'Tuesday']
```

- 情况 3 - "start : stop"
- 以 `step` 为 1 (默认) 从编号 `start` 往编号 `stop` 切片。

【例子】

```python
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[1:3])  # ['Tuesday', 'Wednesday']
print(week[-3:-1])  # ['Wednesday', 'Thursday']
```

- 情况 4 - "start : stop : step"
- 以具体的 `step` 从编号 `start` 往编号 `stop` 切片。注意最后把 `step` 设为 -1，相当于将列表反向排列。

【例子】

```python
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[1:4:2])  # ['Tuesday', 'Thursday']
print(week[:4:2])  # ['Monday', 'Wednesday']
print(week[1::2])  # ['Tuesday', 'Thursday']
print(week[::-1])  
# ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
```

- 情况 5 - " : "
- 复制列表中的所有元素（浅拷贝）。

【例子】

```python
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(week[:])  
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```

【例子】浅拷贝与深拷贝

```python
list1 = [123, 456, 789, 213]
list2 = list1
list3 = list1[:]

print(list2)  # [123, 456, 789, 213]
print(list3)  # [123, 456, 789, 213]
list1.sort()
print(list2)  # [123, 213, 456, 789] 
print(list3)  # [123, 456, 789, 213]

list1 = [[123, 456], [789, 213]]
list2 = list1
list3 = list1[:]
print(list2)  # [[123, 456], [789, 213]]
print(list3)  # [[123, 456], [789, 213]]
list1[0][0] = 111
print(list2)  # [[111, 456], [789, 213]]
print(list3)  # [[111, 456], [789, 213]]
```

### 6. 列表的常用操作符

- 等号操作符：`==`
- 连接操作符 `+`
- 重复操作符 `*`
- 成员关系操作符 `in`、`not in`

「等号 ==」，只有成员、成员位置都相同时才返回True。

列表拼接有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。

【例子】

```python
list1 = [123, 456]
list2 = [456, 123]
list3 = [123, 456]

print(list1 == list2)  # False
print(list1 == list3)  # True

list4 = list1 + list2  # extend()
print(list4)  # [123, 456, 456, 123]

list5 = list3 * 3
print(list5)  # [123, 456, 123, 456, 123, 456]

list3 *= 3
print(list3)  # [123, 456, 123, 456, 123, 456]

print(123 in list3)  # True
print(456 not in list3)  # False
```

前面三种方法（`append`, `extend`, `insert`）可对列表增加元素，它们没有返回值，是直接修改了原数据对象。
而将两个list相加，需要创建新的 list 对象，从而需要消耗额外的内存，特别是当 list 较大时，尽量不要使用 “+” 来添加list。

### 7. 列表的其它方法

`list.count(obj)` 统计某个元素在列表中出现的次数

【例子】

```python
list1 = [123, 456] * 3
print(list1)  # [123, 456, 123, 456, 123, 456]
num = list1.count(123)
print(num)  # 3
```

`list.index(x[, start[, end]])` 从列表中找出某个值第一个匹配项的索引位置

【例子】

```python
list1 = [123, 456] * 5
print(list1.index(123))  # 0
print(list1.index(123, 1))  # 2
print(list1.index(123, 3, 7))  # 4
```

`list.reverse()` 反向列表中元素

【例子】

```python
x = [123, 456, 789]
x.reverse()
print(x)  # [789, 456, 123]
```

`list.sort(key=None, reverse=False)` 对原列表进行排序。

- `key` -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- `reverse` -- 排序规则，`reverse = True` 降序， `reverse = False` 升序（默认）。
- 该方法没有返回值，但是会对列表的对象进行排序。

【例子】

```python
x = [123, 456, 789, 213]
x.sort()
print(x)
# [123, 213, 456, 789]

x.sort(reverse=True)
print(x)
# [789, 456, 213, 123]


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


x = [(2, 2), (3, 4), (4, 1), (1, 3)]
x.sort(key=takeSecond)
print(x)
# [(4, 1), (2, 2), (1, 3), (3, 4)]

x.sort(key=lambda a: a[0])
print(x)
# [(1, 3), (2, 2), (3, 4), (4, 1)]
```

## 元组

### 1. 元组的定义

「元组」定义语法为：`(元素1, 元素2, ..., 元素n)`

- 小括号把所有元素绑在一起
- 逗号将每个元素一一分开

### 2. 创建和访问一个元组

- Python 的元组与列表类似，不同之处在于tuple被创建后就不能对其进行修改，类似字符串。
- 元组使用小括号，列表使用方括号。
- 元组与列表类似，也用整数来对它进行索引 (indexing) 和切片 (slicing)。

【例子】

```python
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
```

- 创建元组可以用小括号 ()，也可以什么都不用，为了可读性，建议还是用 ()。
- 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用。

【例子】

```python
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
```

【例子】

```python
print(8 * (8))  # 64
print(8 * (8,))  # (8, 8, 8, 8, 8, 8, 8, 8)
```

【例子】创建二维元组。

```python
x = (1, 10.31, 'python'), ('data', 11)
print(x)
# ((1, 10.31, 'python'), ('data', 11))

print(x[0])
# (1, 10.31, 'python')
print(x[0][0], x[0][1], x[0][2])
# 1 10.31 python

print(x[0][0:2])
# (1, 10.31)
```

### 3. 更新和删除一个元组

【例子】

```python
week = ('Monday', 'Tuesday', 'Thursday', 'Friday')
week = week[:2] + ('Wednesday',) + week[2:]
print(week)  # ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
```

【例子】元组有不可更改 (immutable) 的性质，因此不能直接给元组的元素赋值，但是只要元组中的元素可更改 (mutable)，那么我们可以直接更改其元素，注意这跟赋值其元素不同。

```python
t1 = (1, 2, 3, [4, 5, 6])
print(t1)  # (1, 2, 3, [4, 5, 6])

t1[3][0] = 9
print(t1)  # (1, 2, 3, [9, 5, 6])
```

### 4. 元组相关的操作符

- 等号操作符：`==`
- 连接操作符 `+`
- 重复操作符 `*`
- 成员关系操作符 `in`、`not in`

「等号 ==」，只有成员、成员位置都相同时才返回True。

元组拼接有两种方式，用「加号 +」和「乘号 *」，前者首尾拼接，后者复制拼接。

【例子】

```python
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
```

### 5. 内置方法

元组大小和内容都不可更改，因此只有 `count` 和 `index` 两种方法。

【例子】

```python
t = (1, 10.31, 'python')
print(t.count('python'))  # 1
print(t.index(10.31))  # 1
```

- `count('python')` 是记录在元组 `t` 中该元素出现几次，显然是 1 次
- `index(10.31)` 是找到该元素在元组 `t` 的索引，显然是 1

### 6. 解压元组

【例子】解压（unpack）一维元组（有几个元素左边括号定义几个变量）

```python
t = (1, 10.31, 'python')
(a, b, c) = t
print(a, b, c)
# 1 10.31 python
```

【例子】解压二维元组（按照元组里的元组结构来定义变量）

```python
t = (1, 10.31, ('OK', 'python'))
(a, b, (c, d)) = t
print(a, b, c, d)
# 1 10.31 OK python
```

【例子】如果你只想要元组其中几个元素，用通配符「*」，英文叫 wildcard，在计算机语言中代表一个或多个元素。下例就是把多个元素丢给了 `rest` 变量。

```python
t = 1, 2, 3, 4, 5
a, b, *rest, c = t
print(a, b, c)  # 1 2 5
print(rest)  # [3, 4]
```

【例子】如果你根本不在乎 rest 变量，那么就用通配符「*」加上下划线「_」。

```python
t = 1, 2, 3, 4, 5
a, b, *_ = t
print(a, b)  # 1 2
```

## 字符串

### 1. 字符串的定义
- Python 中字符串被定义为引号之间的字符集合。
- Python 支持使用成对的 单引号 或 双引号。

【例子】

```python
t1 = 'i love Python!'
print(t1, type(t1))
# i love Python! <class 'str'>

t2 = "I love Python!"
print(t2, type(t2))
# I love Python! <class 'str'>

print(5 + 8)  # 13
print('5' + '8')  # 58
```

- Python 的常用转义字符


| 转义字符 | 描述            |
| :------: | --------------- |
|   `\\`   | 反斜杠符号      |
|   `\'`   | 单引号          |
|   `\"`   | 双引号          |
|   `\n`   | 换行            |
|   `\t`   | 横向制表符(TAB) |
|   `\r`   | 回车            |

【例子】如果字符串中需要出现单引号或双引号，可以使用转义符号`\`对字符串中的符号进行转义。

```python
print('let\'s go')  # let's go
print("let's go")  # let's go
print('C:\\now')  # C:\now
print("C:\\Program Files\\Intel\\Wifi\\Help")
# C:\Program Files\Intel\Wifi\Help
```

【例子】原始字符串只需要在字符串前边加一个英文字母 r 即可。

```python
print(r'C:\Program Files\Intel\Wifi\Help')  
# C:\Program Files\Intel\Wifi\Help
```

【例子】三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。

```python
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)
# 这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB (    )。
# 也可以使用换行符 [
#  ]。
```

### 2. 字符串的切片与拼接

- 类似于元组具有不可修改性
- 从 0 开始 (和 Java 一样)
- 切片通常写成 `start:end` 这种形式，包括「`start` 索引」对应的元素，不包括「`end`索引」对应的元素。
- 索引值可正可负，正索引从 0 开始，从左往右；负索引从 -1 开始，从右往左。使用负数索引时，会从最后一个元素开始计数。最后一个元素的位置编号是 -1。

【例子】

```python
str1 = 'I Love LsgoGroup'
print(str1[:6])  # I Love
print(str1[5])  # e
print(str1[:6] + " 插入的字符串 " + str1[6:])  
# I Love 插入的字符串  LsgoGroup

s = 'Python'
print(s)  # Python
print(s[2:4])  # th
print(s[-5:-2])  # yth
print(s[2])  # t
print(s[-1])  # n
```

### 3. 字符串的常用内置方法



- `capitalize()` 将字符串的第一个字符转换为大写。

【例子】

```python
str2 = 'xiaoxie'
print(str2.capitalize())  # Xiaoxie
```

- `lower()` 转换字符串中所有大写字符为小写。
- `upper()` 转换字符串中的小写字母为大写。
- `swapcase()` 将字符串中大写转换为小写，小写转换为大写。

【例子】

```python
str2 = "DAXIExiaoxie"
print(str2.lower())  # daxiexiaoxie
print(str2.upper())  # DAXIEXIAOXIE
print(str2.swapcase())  # daxieXIAOXIE
```

- `count(str, beg= 0,end=len(string))` 返回`str`在 string 里面出现的次数，如果`beg`或者`end`指定则返回指定范围内`str`出现的次数。

【例子】

```python
str2 = "DAXIExiaoxie"
print(str2.count('xi'))  # 2
```

- `endswith(suffix, beg=0, end=len(string))` 检查字符串是否以指定子字符串 `suffix` 结束，如果是，返回 True，否则返回 False。如果 `beg` 和 `end` 指定值，则在指定范围内检查。
- `startswith(substr, beg=0,end=len(string))` 检查字符串是否以指定子字符串 `substr` 开头，如果是，返回 True，否则返回 False。如果 `beg` 和 `end` 指定值，则在指定范围内检查。

【例子】

```python
str2 = "DAXIExiaoxie"
print(str2.endswith('ie'))  # True
print(str2.endswith('xi'))  # False
print(str2.startswith('Da'))  # False
print(str2.startswith('DA'))  # True
```

- `find(str, beg=0, end=len(string))` 检测 `str` 是否包含在字符串中，如果指定范围 `beg` 和 `end`，则检查是否包含在指定范围内，如果包含，返回开始的索引值，否则返回 -1。
- `rfind(str, beg=0,end=len(string))` 类似于 `find()` 函数，不过是从右边开始查找。

【例子】

```python
str2 = "DAXIExiaoxie"
print(str2.find('xi'))  # 5
print(str2.find('ix'))  # -1
print(str2.rfind('xi'))  # 9
```

- `isnumeric()` 如果字符串中只包含数字字符，则返回 True，否则返回 False。

【例子】

```python
str3 = '12345'
print(str3.isnumeric())  # True
str3 += 'a'
print(str3.isnumeric())  # False
```

- `ljust(width[, fillchar])`返回一个原字符串左对齐，并使用`fillchar`（默认空格）填充至长度`width`的新字符串。
- `rjust(width[, fillchar])`返回一个原字符串右对齐，并使用`fillchar`（默认空格）填充至长度`width`的新字符串。

【例子】

```python
str4 = '1101'
print(str4.ljust(8, '0'))  # 11010000
print(str4.rjust(8, '0'))  # 00001101
```

- `lstrip([chars])` 截掉字符串左边的空格或指定字符。
- `rstrip([chars])` 删除字符串末尾的空格或指定字符。
- `strip([chars])` 在字符串上执行`lstrip()`和`rstrip()`。

【例子】

```python
str5 = ' I Love LsgoGroup '
print(str5.lstrip())  # 'I Love LsgoGroup '
print(str5.lstrip().strip('I'))  # ' Love LsgoGroup '
print(str5.rstrip())  # ' I Love LsgoGroup'
print(str5.strip())  # 'I Love LsgoGroup'
print(str5.strip().strip('p'))  # 'I Love LsgoGrou'
```

- `partition(sub)` 找到子字符串sub，把字符串分为一个三元组`(pre_sub,sub,fol_sub)`，如果字符串中不包含sub则返回`('原字符串','','')`。
- `rpartition(sub)`类似于`partition()`方法，不过是从右边开始查找。

【例子】

```python
str5 = ' I Love LsgoGroup '
print(str5.strip().partition('o'))  # ('I L', 'o', 've LsgoGroup')
print(str5.strip().partition('m'))  # ('I Love LsgoGroup', '', '')
print(str5.strip().rpartition('o'))  # ('I Love LsgoGr', 'o', 'up')
```

- `replace(old, new [, max])` 把 将字符串中的`old`替换成`new`，如果`max`指定，则替换不超过`max`次。

【例子】

```python
str5 = ' I Love LsgoGroup '
print(str5.strip().replace('I', 'We'))  # We Love LsgoGroup
```

- `split(str="", num)` 不带参数默认是以空格为分隔符切片字符串，如果`num`参数有设置，则仅分隔`num`个子字符串，返回切片后的子字符串拼接的列表。

【例子】

```python
str5 = ' I Love LsgoGroup '
print(str5.strip().split())  # ['I', 'Love', 'LsgoGroup']
print(str5.strip().split('o'))  # ['I L', 've Lsg', 'Gr', 'up']
```

【例子】

```python
u = "www.baidu.com.cn"
# 使用默认分隔符
print(u.split())  # ['www.baidu.com.cn']

# 以"."为分隔符
print((u.split('.')))  # ['www', 'baidu', 'com', 'cn']

# 分割0次
print((u.split(".", 0)))  # ['www.baidu.com.cn']

# 分割一次
print((u.split(".", 1)))  # ['www', 'baidu.com.cn']

# 分割两次
print(u.split(".", 2))  # ['www', 'baidu', 'com.cn']

# 分割两次，并取序列为1的项
print((u.split(".", 2)[1]))  # baidu

# 分割两次，并把分割后的三个部分保存到三个变量
u1, u2, u3 = u.split(".", 2)
print(u1)  # www
print(u2)  # baidu
print(u3)  # com.cn
```

【例子】去掉换行符

```python
c = '''say
hello
baby'''

print(c)
# say
# hello
# baby

print(c.split('\n'))  # ['say', 'hello', 'baby']
```

【例子】

```python
string = "hello boy<[www.baidu.com]>byebye"
print(string.split('[')[1].split(']')[0])  # www.baidu.com
print(string.split('[')[1].split(']')[0].split('.'))  # ['www', 'baidu', 'com']
```

- `splitlines([keepends])` 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数`keepends`为 False，不包含换行符，如果为 True，则保留换行符。

【例子】

```python
str6 = 'I \n Love \n LsgoGroup'
print(str6.splitlines())  # ['I ', ' Love ', ' LsgoGroup']
print(str6.splitlines(True))  # ['I \n', ' Love \n', ' LsgoGroup']
```

- `maketrans(intab, outtab)` 创建字符映射的转换表，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
- `translate(table, deletechars="")` 根据参数`table`给出的表，转换字符串的字符，要过滤掉的字符放到`deletechars`参数中。

【例子】

```python
str7 = 'this is string example....wow!!!'
intab = 'aeiou'
outtab = '12345'
trantab = str7.maketrans(intab, outtab)
print(trantab)  # {97: 49, 111: 52, 117: 53, 101: 50, 105: 51}
print(str7.translate(trantab))  # th3s 3s str3ng 2x1mpl2....w4w!!!
```

### 4. 字符串格式化

- `format` 格式化函数

【例子】

```python
str8 = "{0} Love {1}".format('I', 'Lsgogroup')  # 位置参数
print(str8)  # I Love Lsgogroup

str8 = "{a} Love {b}".format(a='I', b='Lsgogroup')  # 关键字参数
print(str8)  # I Love Lsgogroup

str8 = "{0} Love {b}".format('I', b='Lsgogroup')  # 位置参数要在关键字参数之前
print(str8)  # I Love Lsgogroup

str8 = '{0:.2f}{1}'.format(27.658, 'GB')  # 保留小数点后两位
print(str8)  # 27.66GB
```

- Python 字符串格式化符号


| 符   号 | 描述                                 |
| :-----: | :----------------------------------- |
|   %c    | 格式化字符及其ASCII码                |
|   %s    | 格式化字符串，用str()方法处理对象    |
|   %r    | 格式化字符串，用rper()方法处理对象   |
|   %d    | 格式化整数                           |
|   %o    | 格式化无符号八进制数                 |
|   %x    | 格式化无符号十六进制数               |
|   %X    | 格式化无符号十六进制数（大写）       |
|   %f    | 格式化浮点数字，可指定小数点后的精度 |
|   %e    | 用科学计数法格式化浮点数             |
|   %E    | 作用同%e，用科学计数法格式化浮点数   |
|   %g    | 根据值的大小决定使用%f或%e           |
|   %G    | 作用同%g，根据值的大小决定使用%f或%E |

【例子】

```python
print('%c' % 97)  # a
print('%c %c %c' % (97, 98, 99))  # a b c
print('%d + %d = %d' % (4, 5, 9))  # 4 + 5 = 9
print("我叫 %s 今年 %d 岁!" % ('小明', 10))  # 我叫 小明 今年 10 岁!
print('%o' % 10)  # 12
print('%x' % 10)  # a
print('%X' % 10)  # A
print('%f' % 27.658)  # 27.658000
print('%e' % 27.658)  # 2.765800e+01
print('%E' % 27.658)  # 2.765800E+01
print('%g' % 27.658)  # 27.658
text = "I am %d years old." % 22
print("I said: %s." % text)  # I said: I am 22 years old..
print("I said: %r." % text)  # I said: 'I am 22 years old.'
```

- 格式化操作符辅助指令

| 符号  | 功能                                                         |
| :---: | :----------------------------------------------------------- |
| `m.n` | m 是显示的最小总宽度,n 是小数点后的位数（如果可用的话）      |
|  `-`  | 用作左对齐                                                   |
|  `+`  | 在正数前面显示加号( + )                                      |
|  `#`  | 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X') |
|  `0`  | 显示的数字前面填充'0'而不是默认的空格                        |

【例子】

```python
print('%5.1f' % 27.658)  # ' 27.7'
print('%.2e' % 27.658)  # 2.77e+01
print('%10d' % 10)  # '        10'
print('%-10d' % 10)  # '10        '
print('%+d' % 10)  # +10
print('%#o' % 10)  # 0o12
print('%#x' % 108)  # 0x6c
print('%010d' % 5)  # 0000000005
```

## 字典

### 1. 可变类型与不可变类型

- 序列是以连续的整数为索引，与此不同的是，字典以"关键字"为索引，关键字可以是任意不可变类型，通常用字符串或数值。
- 字典是 Python 唯一的一个 <u>映射类型</u>，字符串、元组、列表属于<u>序列类型</u>。

那么如何快速判断一个数据类型 `X` 是不是可变类型的呢？两种方法：
- 麻烦方法：用 `id(X)` 函数，对 X 进行某种操作，比较操作前后的 `id`，如果不一样，则 `X` 不可变，如果一样，则 `X` 可变。
- 便捷方法：用 `hash(X)`，只要不报错，证明 `X` 可被哈希，即不可变，反过来不可被哈希，即可变。

【例子】

```python
i = 1
print(id(i))  # 140732167000896
i = i + 2
print(id(i))  # 140732167000960

l = [1, 2]
print(id(l))  # 4300825160
l.append('Python')
print(id(l))  # 4300825160
```

- 整数 `i` 在加 1 之后的 `id` 和之前不一样，因此加完之后的这个 `i` (虽然名字没变)，但不是加之前的那个 `i` 了，因此整数是不可变类型。
- 列表 `l` 在附加 `'Python'` 之后的 `id` 和之前一样，因此列表是可变类型。

【例子】

```python
print(hash('Name'))  # 7047218704141848153

print(hash((1, 2, 'Python')))  # 1704535747474881831

print(hash([1, 2, 'Python']))
# TypeError: unhashable type: 'list'

```

```
print(hash({1, 2, 3}))
# TypeError: unhashable type: 'set'
```

- 数值、字符和元组 都能被哈希，因此它们是不可变类型。
- 列表、集合、字典不能被哈希，因此它是可变类型。




### 2. 字典的定义

字典 是无序的 键:值（`key:value`）对集合，键必须是互不相同的（在同一个字典之内）。

- `dict` 内部存放的顺序和 `key` 放入的顺序是没有关系的。
- `dict` 查找和插入的速度极快，不会随着 `key` 的增加而增加，但是需要占用大量的内存。


字典 定义语法为 `{元素1, 元素2, ..., 元素n}`

- 其中每一个元素是一个「键值对」-- 键:值 (`key:value`)
- 关键点是「大括号 {}」,「逗号 ,」和「冒号 :」
- 大括号 -- 把所有元素绑在一起
- 逗号 -- 将每个键值对分开
- 冒号 -- 将键和值分开


### 3. 创建和访问字典

【例子】

```python
brand = ['李宁', '耐克', '阿迪达斯']
slogan = ['一切皆有可能', 'Just do it', 'Impossible is nothing']
print('耐克的口号是:', slogan[brand.index('耐克')])  
# 耐克的口号是: Just do it

dic = {'李宁': '一切皆有可能', '耐克': 'Just do it', '阿迪达斯': 'Impossible is nothing'}
print('耐克的口号是:', dic['耐克'])  
# 耐克的口号是: Just do it
```

【例子】通过字符串或数值作为`key`来创建字典。

```python
dic1 = {1: 'one', 2: 'two', 3: 'three'}
print(dic1)  # {1: 'one', 2: 'two', 3: 'three'}
print(dic1[1])  # one
print(dic1[4])  # KeyError: 4
```

```python
dic2 = {'rice': 35, 'wheat': 101, 'corn': 67}
print(dic2)  # {'wheat': 101, 'corn': 67, 'rice': 35}
print(dic2['rice'])  # 35
```

注意：如果我们取的键在字典中不存在，会直接报错`KeyError`。

【例子】通过元组作为`key`来创建字典，但一般不这样使用。

```python
dic = {(1, 2, 3): "Tom", "Age": 12, 3: [3, 5, 7]}
print(dic)  # {(1, 2, 3): 'Tom', 'Age': 12, 3: [3, 5, 7]}
print(type(dic))  # <class 'dict'>
```

通过构造函数`dict`来创建字典。

- `dict()` 创建一个空的字典。

【例子】通过`key`直接把数据放入字典中，但一个`key`只能对应一个`value`，多次对一个`key`放入 `value`，后面的值会把前面的值冲掉。

```python
dic = dict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3

print(dic)
# {'a': 1, 'b': 2, 'c': 3}

dic['a'] = 11
print(dic)
# {'a': 11, 'b': 2, 'c': 3}

dic['d'] = 4
print(dic)
# {'a': 11, 'b': 2, 'c': 3, 'd': 4}
```

- `dict(mapping)` new dictionary initialized from a mapping object's (key, value) pairs

【例子】

```python
dic1 = dict([('apple', 4139), ('peach', 4127), ('cherry', 4098)])
print(dic1)  # {'cherry': 4098, 'apple': 4139, 'peach': 4127}

dic2 = dict((('apple', 4139), ('peach', 4127), ('cherry', 4098)))
print(dic2)  # {'peach': 4127, 'cherry': 4098, 'apple': 4139}
```

- `dict(**kwargs)` -> new dictionary initialized with the name=value pairs in the keyword argument list.  For example:  dict(one=1, two=2)

【例子】这种情况下，键只能为字符串类型，并且创建的时候字符串不能加引号，加上就会直接报语法错误。

```python
dic = dict(name='Tom', age=10)
print(dic)  # {'name': 'Tom', 'age': 10}
print(type(dic))  # <class 'dict'>
```

### 4. 字典的内置方法

- `dict.fromkeys(seq[, value])` 用于创建一个新字典，以序列 `seq` 中元素做字典的键，`value` 为字典所有键对应的初始值。

【例子】

```python
seq = ('name', 'age', 'sex')
dic1 = dict.fromkeys(seq)
print(dic1)
# {'name': None, 'age': None, 'sex': None}

dic2 = dict.fromkeys(seq, 10)
print(dic2)
# {'name': 10, 'age': 10, 'sex': 10}

dic3 = dict.fromkeys(seq, ('小马', '8', '男'))
print(dic3)
# {'name': ('小马', '8', '男'), 'age': ('小马', '8', '男'), 'sex': ('小马', '8', '男')}
```

- `dict.keys()`返回一个可迭代对象，可以使用 `list()` 来转换为列表，列表为字典中的所有键。

【例子】

```python
dic = {'Name': 'lsgogroup', 'Age': 7}
print(dic.keys())  # dict_keys(['Name', 'Age'])
lst = list(dic.keys())  # 转换为列表
print(lst)  # ['Name', 'Age']
```

- `dict.values()`返回一个迭代器，可以使用 `list()` 来转换为列表，列表为字典中的所有值。

【例子】

```python
dic = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print(dic.values())
# dict_values(['female', 7, 'Zara'])

print(list(dic.values()))
# [7, 'female', 'Zara']
```

- `dict.items()`以列表返回可遍历的 (键, 值) 元组数组。

【例子】

```python
dic = {'Name': 'Lsgogroup', 'Age': 7}
print(dic.items())
# dict_items([('Name', 'Lsgogroup'), ('Age', 7)])

print(tuple(dic.items()))
# (('Name', 'Lsgogroup'), ('Age', 7))

print(list(dic.items()))
# [('Name', 'Lsgogroup'), ('Age', 7)]
```

- `dict.get(key, default=None)` 返回指定键的值，如果值不在字典中返回默认值。

【例子】

```python
dic = {'Name': 'Lsgogroup', 'Age': 27}
print("Age 值为 : %s" % dic.get('Age'))  # Age 值为 : 27
print("Sex 值为 : %s" % dic.get('Sex', "NA"))  # Sex 值为 : NA
print(dic)  # {'Name': 'Lsgogroup', 'Age': 27}
```

- `dict.setdefault(key, default=None)`和`get()`方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

【例子】

```python
dic = {'Name': 'Lsgogroup', 'Age': 7}
print("Age 键的值为 : %s" % dic.setdefault('Age', None))  # Age 键的值为 : 7
print("Sex 键的值为 : %s" % dic.setdefault('Sex', None))  # Sex 键的值为 : None
print(dic)  
# {'Age': 7, 'Name': 'Lsgogroup', 'Sex': None}
```

- `key in dict` `in` 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回`true`，否则返回`false`。而`not in`操作符刚好相反，如果键在字典 dict 里返回`false`，否则返回`true`。

【例子】

```python
dic = {'Name': 'Lsgogroup', 'Age': 7}

# in 检测键 Age 是否存在
if 'Age' in dic:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dic:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in 检测键 Age 是否存在
if 'Age' not in dic:
    print("键 Age 不存在")
else:
    print("键 Age 存在")

# 键 Age 存在
# 键 Sex 不存在
# 键 Age 存在
```

- `dict.pop(key[,default])`删除字典给定键 `key` 所对应的值，返回值为被删除的值。`key` 值必须给出。若`key`不存在，则返回 `default` 值。
- `del dict[key]` 删除字典给定键 `key` 所对应的值。

【例子】

```python
dic1 = {1: "a", 2: [1, 2]}
print(dic1.pop(1), dic1)  # a {2: [1, 2]}

# 设置默认值，必须添加，否则报错
print(dic1.pop(3, "nokey"), dic1)  # nokey {2: [1, 2]}

del dic1[2]
print(dic1)  # {}
```

- `dict.popitem()`随机返回并删除字典中的一对键和值，如果字典已经为空，却调用了此方法，就报出KeyError异常。

【例子】

```python
dic1 = {1: "a", 2: [1, 2]}
print(dic1.popitem())  # {2: [1, 2]}
print(dic1)  # (1, 'a')
```

- `dict.clear()`用于删除字典内所有元素。

【例子】

```python
dic = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dic))  # 字典长度 : 2
dic.clear()
print("字典删除后长度 : %d" % len(dic))  
# 字典删除后长度 : 0
```

- `dict.copy()`返回一个字典的浅复制。

【例子】

```python
dic1 = {'Name': 'Lsgogroup', 'Age': 7, 'Class': 'First'}
dic2 = dic1.copy()
print("dic2")  
# {'Age': 7, 'Name': 'Lsgogroup', 'Class': 'First'}
```

【例子】直接赋值和 copy 的区别

```python
dic1 = {'user': 'lsgogroup', 'num': [1, 2, 3]}

# 引用对象
dic2 = dic1  
# 浅拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dic3 = dic1.copy()  

print(id(dic1))  # 148635574728
print(id(dic2))  # 148635574728
print(id(dic3))  # 148635574344

# 修改 data 数据
dic1['user'] = 'root'
dic1['num'].remove(1)

# 输出结果
print(dic1)  # {'user': 'root', 'num': [2, 3]}
print(dic2)  # {'user': 'root', 'num': [2, 3]}
print(dic3)  # {'user': 'runoob', 'num': [2, 3]}
```

- `dict.update(dict2)`把字典参数 `dict2` 的 `key:value`对 更新到字典 `dict` 里。

【例子】

```python
dic = {'Name': 'Lsgogroup', 'Age': 7}
dic2 = {'Sex': 'female', 'Age': 8}
dic.update(dic2)
print(dic)  
# {'Sex': 'female', 'Age': 8, 'Name': 'Lsgogroup'}
```

## 集合

Python 中`set`与`dict`类似，也是一组`key`的集合，但不存储`value`。由于`key`不能重复，所以，在`set`中，没有重复的`key`。

注意，`key`为不可变类型，即可哈希的值。

【例子】

```python
num = {}
print(type(num))  # <class 'dict'>
num = {1, 2, 3, 4}
print(type(num))  # <class 'set'>
```

### 1. 集合的创建

- 先创建对象再加入元素。
- 在创建空集合的时候只能使用`s = set()`，因为`s = {}`创建的是空字典。

【例子】

```python
basket = set()
basket.add('apple')
basket.add('banana')
print(basket)  # {'banana', 'apple'}
```

- 直接把一堆元素用花括号括起来`{元素1, 元素2, ..., 元素n}`。
- 重复元素在`set`中会被自动被过滤。

【例子】

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'banana', 'apple', 'pear', 'orange'}
```

- 使用`set(value)`工厂函数，把列表或元组转换成集合。

【例子】

```python
a = set('abracadabra')
print(a)  
# {'r', 'b', 'd', 'c', 'a'}

b = set(("Google", "Lsgogroup", "Taobao", "Taobao"))
print(b)  
# {'Taobao', 'Lsgogroup', 'Google'}

c = set(["Google", "Lsgogroup", "Taobao", "Google"])
print(c)  
# {'Taobao', 'Lsgogroup', 'Google'}
```

【例子】去掉列表中重复的元素

```python
lst = [0, 1, 2, 3, 4, 5, 5, 3, 1]

temp = []
for item in lst:
    if item not in temp:
        temp.append(item)

print(temp)  # [0, 1, 2, 3, 4, 5]

a = set(lst)
print(list(a))  # [0, 1, 2, 3, 4, 5]
```

从结果发现集合的两个特点：无序 (unordered) 和唯一 (unique)。

由于 `set` 存储的是无序集合，所以我们不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值，但是可以判断一个元素是否在集合中。




### 2. 访问集合中的值

- 可以使用`len()`內建函数得到集合的大小。

【例子】

```python
s = set(['Google', 'Baidu', 'Taobao'])
print(len(s))  # 3
```

- 可以使用`for`把集合中的数据一个个读取出来。

【例子】

```python
s = set(['Google', 'Baidu', 'Taobao'])
for item in s:
    print(item)
    
# Baidu
# Google
# Taobao
```

- 可以通过`in`或`not in`判断一个元素是否在集合中已经存在

【例子】

```python
s = set(['Google', 'Baidu', 'Taobao'])
print('Taobao' in s)  # True
print('Facebook' not in s)  # True
```

### 3. 集合的内置方法

- `set.add(elmnt)`用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。

【例子】

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  
# {'orange', 'cherry', 'banana', 'apple'}

fruits.add("apple")
print(fruits)  
# {'orange', 'cherry', 'banana', 'apple'}
```

- `set.update(set)`用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。

【例子】

```python
x = {"apple", "banana", "cherry"}
y = {"google", "baidu", "apple"}
x.update(y)
print(x)
# {'cherry', 'banana', 'apple', 'google', 'baidu'}

y.update(["lsgo", "dreamtech"])
print(y)
# {'lsgo', 'baidu', 'dreamtech', 'apple', 'google'}
```

- `set.remove(item)` 用于移除集合中的指定元素。如果元素不存在，则会发生错误。

【例子】

```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}
```

- `set.discard(value)` 用于移除指定的集合元素。`remove()` 方法在移除一个不存在的元素时会发生错误，而 `discard()` 方法不会。

【例子】

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # {'apple', 'cherry'}
```

- `set.pop()` 用于随机移除一个元素。

【例子】

```python
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(fruits)  # {'cherry', 'apple'}
print(x)  # banana
```

由于 set 是无序和无重复元素的集合，所以两个或多个 set 可以做数学意义上的集合操作。
- `set.intersection(set1, set2)` 返回两个集合的交集。
- `set1 & set2` 返回两个集合的交集。
- `set.intersection_update(set1, set2)` 交集，在原始的集合上移除不重叠的元素。

【例子】

```python
a = set('abracadabra')
b = set('alacazam')
print(a)  # {'r', 'a', 'c', 'b', 'd'}
print(b)  # {'c', 'a', 'l', 'm', 'z'}

c = a.intersection(b)
print(c)  # {'a', 'c'}
print(a & b)  # {'c', 'a'}
print(a)  # {'a', 'r', 'c', 'b', 'd'}

a.intersection_update(b)
print(a)  # {'a', 'c'}
```

- `set.union(set1, set2)` 返回两个集合的并集。
- `set1 | set2` 返回两个集合的并集。

【例子】

```python
a = set('abracadabra')
b = set('alacazam')
print(a)  # {'r', 'a', 'c', 'b', 'd'}
print(b)  # {'c', 'a', 'l', 'm', 'z'}

print(a | b)  
# {'l', 'd', 'm', 'b', 'a', 'r', 'z', 'c'}

c = a.union(b)
print(c)  
# {'c', 'a', 'd', 'm', 'r', 'b', 'z', 'l'}
```

- `set.difference(set)` 返回集合的差集。
- `set1 - set2` 返回集合的差集。
- `set.difference_update(set)` 集合的差集，直接在原来的集合中移除元素，没有返回值。

【例子】

```python
a = set('abracadabra')
b = set('alacazam')
print(a)  # {'r', 'a', 'c', 'b', 'd'}
print(b)  # {'c', 'a', 'l', 'm', 'z'}

c = a.difference(b)
print(c)  # {'b', 'd', 'r'}
print(a - b)  # {'d', 'b', 'r'}

print(a)  # {'r', 'd', 'c', 'a', 'b'}
a.difference_update(b)
print(a)  # {'d', 'r', 'b'}
```

- `set.symmetric_difference(set)`返回集合的异或。
- `set1 ^ set2` 返回集合的异或。
- `set.symmetric_difference_update(set)`移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。

【例子】

```python
a = set('abracadabra')
b = set('alacazam')
print(a)  # {'r', 'a', 'c', 'b', 'd'}
print(b)  # {'c', 'a', 'l', 'm', 'z'}

c = a.symmetric_difference(b)
print(c)  # {'m', 'r', 'l', 'b', 'z', 'd'}
print(a ^ b)  # {'m', 'r', 'l', 'b', 'z', 'd'}

print(a)  # {'r', 'd', 'c', 'a', 'b'}
a.symmetric_difference_update(b)
print(a)  # {'r', 'b', 'm', 'l', 'z', 'd'}
```

- `set.issubset(set)`判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。
- `set1 <= set2` 判断集合是不是被其他集合包含，如果是则返回 True，否则返回 False。

【例子】

```python
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)  # True
print(x <= y)  # True

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)  # False
print(x <= y)  # False
```

- `set.issuperset(set)`用于判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。
- `set1 >= set2` 判断集合是不是包含其他集合，如果是则返回 True，否则返回 False。

【例子】

```python
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)  # True
print(x >= y)  # True

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)  # False
print(x >= y)  # False
```

- `set.isdisjoint(set)` 用于判断两个集合是不是不相交，如果是返回 True，否则返回 False。

【例子】

```python
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z)  # False

x = {"f", "e", "d", "m", "g"}
y = {"a", "b", "c"}
z = x.isdisjoint(y)
print(z)  # True
```

### 4. 集合的转换

【例子】

```python
se = set(range(4))
li = list(se)
tu = tuple(se)

print(se, type(se))  # {0, 1, 2, 3} <class 'set'>
print(li, type(li))  # [0, 1, 2, 3] <class 'list'>
print(tu, type(tu))  # (0, 1, 2, 3) <class 'tuple'>
```

### 5. 不可变集合

Python 提供了不能改变元素的集合的实现版本，即不能增加或删除元素，类型名叫`frozenset`。需要注意的是`frozenset`仍然可以进行集合操作，只是不能用带有`update`的方法。

- `frozenset([iterable])` 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

【例子】

```python
a = frozenset(range(10))  # 生成一个新的不可变集合
print(a)  
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

b = frozenset('lsgogroup')
print(b)  
# frozenset({'g', 's', 'p', 'r', 'u', 'o', 'l'})
```

## 序列

在 Python 中，序列类型包括字符串、列表、元组、集合和字典，这些序列支持一些通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。

### 1. 针对序列的内置函数

- `list(sub)` 把一个可迭代对象转换为列表。

【例子】

```python
a = list()
print(a)  # []

b = 'I Love LsgoGroup'
b = list(b)
print(b)  
# ['I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p']

c = (1, 1, 2, 3, 5, 8)
c = list(c)
print(c)  # [1, 1, 2, 3, 5, 8]
```

- `tuple(sub)` 把一个可迭代对象转换为元组。

【例子】

```python
a = tuple()
print(a)  # ()

b = 'I Love LsgoGroup'
b = tuple(b)
print(b)  
# ('I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p')

c = [1, 1, 2, 3, 5, 8]
c = tuple(c)
print(c)  # (1, 1, 2, 3, 5, 8)
```

- `str(obj)` 把obj对象转换为字符串

【例子】

```python
a = 123
a = str(a)
print(a)  # 123
```

- `len(s)` 返回对象（字符、列表、元组等）长度或元素个数。
    - `s` -- 对象。

【例子】

```python
a = list()
print(len(a))  # 0

b = ('I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p')
print(len(b))  # 16

c = 'I Love LsgoGroup'
print(len(c))  # 16
```

- `max(sub)`返回序列或者参数集合中的最大值

【例子】

```python
print(max(1, 2, 3, 4, 5))  # 5
print(max([-8, 99, 3, 7, 83]))  # 99
print(max('IloveLsgoGroup'))  # v
```

- `min(sub)`返回序列或参数集合中的最小值

【例子】

```py
print(min(1, 2, 3, 4, 5))  # 1
print(min([-8, 99, 3, 7, 83]))  # -8
print(min('IloveLsgoGroup'))  # G
```

- `sum(iterable[, start=0])` 返回序列`iterable`与可选参数`start`的总和。

【例子】

```python
print(sum([1, 3, 5, 7, 9]))  # 25
print(sum([1, 3, 5, 7, 9], 10))  # 35
print(sum((1, 3, 5, 7, 9)))  # 25
print(sum((1, 3, 5, 7, 9), 20))  # 45
```

- `sorted(iterable, key=None, reverse=False) ` 对所有可迭代的对象进行排序操作。
    - `iterable` -- 可迭代对象。
    - `key` -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    - `reverse` -- 排序规则，`reverse = True` 降序 ， `reverse = False` 升序（默认）。
    - 返回重新排序的列表。

【例子】

```python
x = [-8, 99, 3, 7, 83]
print(sorted(x))  # [-8, 3, 7, 83, 99]
print(sorted(x, reverse=True))  # [99, 83, 7, 3, -8]

t = ({"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"})
x = sorted(t, key=lambda a: a["age"])
print(x)
# [{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]
```

- `reversed(seq)` 函数返回一个反转的迭代器。
    - `seq` -- 要转换的序列，可以是 tuple, string, list 或 range。

【例子】

```python
s = 'lsgogroup'
x = reversed(s)
print(type(x))  # <class 'reversed'>
print(x)  # <reversed object at 0x000002507E8EC2C8>
print(list(x))
# ['p', 'u', 'o', 'r', 'g', 'o', 'g', 's', 'l']

t = ('l', 's', 'g', 'o', 'g', 'r', 'o', 'u', 'p')
print(list(reversed(t)))
# ['p', 'u', 'o', 'r', 'g', 'o', 'g', 's', 'l']

r = range(5, 9)
print(list(reversed(r)))
# [8, 7, 6, 5]

x = [-8, 99, 3, 7, 83]
print(list(reversed(x)))
# [83, 7, 3, 99, -8]
```

- `enumerate(sequence, [start=0])`

【例子】用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
a = list(enumerate(seasons))
print(a)  
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

b = list(enumerate(seasons, 1))
print(b)  
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

for i, element in a:
    print('{0},{1}'.format(i, element))
# 0,Spring
# 1,Summer
# 2,Fall
# 3,Winter
```

- `zip(iter1 [,iter2 [...]])`
    - 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
    - 我们可以使用 `list()` 转换来输出列表。
    - 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 `*` 号操作符，可以将元组解压为列表。

【例子】

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]

zipped = zip(a, b)
print(zipped)  # <zip object at 0x000000C5D89EDD88>
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]
zipped = zip(a, c)
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]

a1, a2 = zip(*zip(a, b))
print(list(a1))  # [1, 2, 3]
print(list(a2))  # [4, 5, 6]
```

