------

<h1>Python入门(上)</h1>

1. [简介](#简介)

2. [变量、运算符与数据类型](#变量、运算符与数据类型)<br>
   [1. 注释](#1.注释)<br>
   [2. 运算符](#2.运算符)<br>
   [3. 变量和赋值](#3.-变量和赋值)<br>
   [4. 数据类型与转换](#4.-数据类型与转换)<br>
   [5. print()函数](#5.-print()-函数)<br>

3. [位运算](#位运算)<br>
   [1. 原码、反码和补码](#1.-原码、反码和补码)<br>
   [2. 按位运算](#2.-按位运算)<br>
   [3. 利用位运算实现快速计算](#3.-利用位运算实现快速计算)<br>
   [4. 利用位运算实现整数集合](#4.-利用位运算实现整数集合)<br>
   
4. [条件语句](#条件语句)<br>
   [1. if 语句](#1.-if-语句)<br>
   [2. if - else 语句](#2.-if---else-语句)<br>
   [3. if - elif - else 语句](#3.-if---elif---else-语句)<br>
   [4. assert 关键词](#4.-assert-关键词)<br>
   
5. [循环语句](#循环语句)<br>
   [1. while 循环](#1.-while-循环)<br>
   [2. while - else 循环](#2.-while---else-循环)<br>
   [3. for 循环](#3.-for-循环)<br>
   [4. for - else 循环](#4.-for---else-循环)<br>
   [5. range() 函数](#5.-range()-函数)<br>
   [6. enumerate()函数](#6.-enumerate()函数)<br>
   [7. break 语句](#7.-break-语句)<br>
   [8. continue 语句](#8.-continue-语句)<br>
   [9. pass 语句](#9.-pass-语句)<br>
   [10. 推导式](#10.-推导式)<br>
   
6. [异常处理](#异常处理)<br>
   [1. Python 标准异常总结](#1.-Python-标准异常总结)<br>
   [2. Python 标准警告总结](#2.-Python标准警告总结)<br>
   [3. try - except 语句](#3.-try---except-语句)<br>
   [4. try - except - finally 语句](#4.-try---except---finally-语句)<br>
   [5. try - except - else 语句](#5.-try---except---else-语句)<br>
   [6. raise语句](#6.-raise语句)<br>


## 简介

Python 是一种通用编程语言，其在科学计算和机器学习领域具有广泛的应用。如果我们打算利用 Python 来执行机器学习，那么对 Python 有一些基本的了解就是至关重要的。本 Python 入门系列体验就是为这样的初学者精心准备的。

本实验包括以下内容：
- 变量、运算符与数据类型
    - 注释
    - 运算符
    - 变量和赋值
    - 数据类型与转换
    - print() 函数
- 位运算
    - 原码、反码和补码
    - 按位非操作 ~
    - 按位与操作 &
    - 按位或操作 |
    - 按位异或操作 ^
    - 按位左移操作 <<
    - 按位右移操作 >>
    - 利用位运算实现快速计算
    - 利用位运算实现整数集合
- 条件语句
    - if 语句
    - if - else 语句
    - if - elif - else 语句
    - assert 关键词
- 循环语句
    - while 循环
    - while - else 循环
    - for 循环
    - for - else 循环
    - range() 函数
    - enumerate()函数
    - break 语句
    - continue 语句
    - pass 语句
    - 推导式
- 异常处理
    - Python 标准异常总结
    - Python 标准警告总结
    - try - except 语句
    - try - except - finally 语句
    - try - except - else 语句
    - raise语句

## 变量、运算符与数据类型

### 1.注释

- 在Python中，# 表示单行注释，作用于整行

【例子】单行注释
```python
# 单行注释
print("单行注释")
```

- ''' ''' 或者 """ """ 表示区间注释，在三引号之间的所有内容被注释

【例子】 多行注释
```python
'''
单引号多行注释
'''
print("多行注释")

"""
双引号多行注释
"""
print("双引号多行注释")
```

### 2.运算符
**算术运算符**

操作符 | 名称 | 示例
:---:|:---:|:---:
`+` | 加 | `1 + 1`
`-` | 减 | `2 - 1`
`*` | 乘 | `3 * 4`
`/` | 除 | `3 / 4`
`//`| 整除（地板除）| `3 // 4`
`%` | 取余| `3 % 4`
`**`| 幂 | `2 ** 3`

【例子】
```python
print(1 + 1)  # 2
print(2 - 1)  # 1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(3 // 4) # 0
print(3 % 4)  # 3
print(2**3)   # 8
```

**比较运算符**

操作符 | 名称 | 示例
:---:|:---:|:---:
`>` |大于| `2 > 1`
`>=`|大于等于| `2 >= 4`
`<` |小于| `1 < 2`
`<=`|小于等于| `5 <= 2`
`==`|等于| `3 == 4`
`!=`|不等于| `3 != 5`

【例子】
```python
print(2 > 1)   # True
print(2 >= 4)  # False
print(1 < 2)   # True
print(5 <= 2)  # False
print(3 == 4)  # False
print(3 != 5)  # True
```

**逻辑运算符**

操作符 | 名称 | 示例
:---:|:---:|:---:
`and`|与| `(3 > 2) and (3 < 5)`
`or` |或| `(1 > 3) or (9 < 2)`
`not`|非| `not (2 > 1)`

【例子】
```python
print((3 > 2) and (3 < 5))  # True
print((1 > 3) or (9 < 89))  # False
print(not (2 > 1))          # False
```

**位运算符**

操作符 | 名称 | 示例
:---:|:---:|:---:
`~` |按位取反|`~4`
`&` |按位与  |`4 & 5`
`|` |按位或  |`4 | 5`
`^` |按位异或|`4 ^ 5`
`<<`|左移    |`4 << 2`
`>>`|右移    |`4 >> 2`

【例子】
```python
print(bin(4))               # 0b100
print(bin(5))               # 0b101
print(bin(~4), ~4)          # -0b101 -5
print(bin(4 & 5), 4 & 5)    # 0b100 4
print(bin(4 | 5), 4 | 5)    # 0b101 5
print(bin(4 ^ 5), 4 ^ 5)    # 0b1 1
print(bin(4 << 2), 4 << 2)  # 0b10000 16
print(bin(4 >> 2), 4 >> 2)  # 0b1 1
```

**三元运算符**

【例子】

```python
x, y = 4, 5
if x < y:
    small = x
else:
    small = y

print(small)  # 4
x, y = 4, 5
```

有了三元操作符的条件表达式，你可以使用一条语句来完成以上的条件判断和赋值操作。
【例子】

```python
x, y = 4, 5
small = x if x < y else y
print(small)  # 4
```

**其他运算符**

操作符 | 名称 | 示例
:---:|:---:|:---:
`in`|存在| `'A' in ['A', 'B', 'C']`
`not in`|不存在|`'h' not in ['A', 'B', 'C']`
`is`|是| `"hello" is "hello"`
`not is`|不是|`"hello" is not "hello"`

【例子】

```python
letters = ['A', 'B', 'C']
if 'A' in letters:
    print('A' + ' exists')
if 'h' not in letters:
    print('h' + ' not exists')
# A exists
# h not exists
```

【例子】比较的两个变量均指向不可变类型。

```python
a = "hello"
b = "hello"
print(a is b, a == b)           # True True
print(a is not b, a != b)       # False False
```

【例子】比较的两个变量均指向可变类型。

```python
a = ["hello"]
b = ["hello"]
print(a is b, a == b)       # False True
print(a is not b, a != b)   # True False
```

注意：
- is, is not 对比的是两个变量的内存地址
- ==, != 对比的是两个变量的值
- 比较的两个变量，指向的都是地址不可变的类型（str等），那么is，is not 和 ==，！= 是完全等价的。
- 对比的两个变量，指向的是地址可变的类型（list，dict，tuple等），则两者是有区别的。

**运算符的优先级**

- 一元运算符优于二元运算符。例如`3 ** -2`等价于`3 ** (-2)`。
- 先算术运算，后移位运算，最后位运算。例如 `1 << 3 + 2 & 7`等价于 `(1 << (3 + 2)) & 7`。
- 逻辑运算最后结合。例如`3 < 4 and 4 < 5`等价于`(3 < 4) and (4 < 5)`。

【例子】

```python
print(-3 ** 2)              # -9
print(3 ** -2)              # 0.1111111111111111
print(1 << 3 + 2 & 7)       # 0
print(-3 * 2 + 5 / -2 - 4)  # -12.5
print(3 < 4 and 4 < 5)      # True
```

### 3. 变量和赋值

- 在使用变量之前，需要对其先赋值。
- 变量名可以包括字母、数字、下划线、但变量名不能以数字开头。
- Python 变量名是大小写敏感的，foo != Foo。

【例子】

```python
teacher = "老马的程序人生"
print(teacher)  # 老马的程序人生

first = 2
second = 3
third = first + second
print(third)  # 5

myTeacher = "老马的程序人生"
yourTeacher = "小马的程序人生"
ourTeacher = myTeacher + ',' + yourTeacher
print(ourTeacher)  # 老马的程序人生,小马的程序人生
```

### 4. 数据类型与转换


类型 | 名称 | 示例
:---:|:---:|:---:
int | 整型 `<class 'int'>`| `-876, 10`
float | 浮点型`<class 'float'>`| `3.149, 11.11`
bool | 布尔型`<class 'bool'>` | `True, False`

**整型**

【例子】通过 `print()` 可看出 `a` 的值，以及类 (class) 是`int`。

```python
a = 1031
print(a, type(a))
# 1031 <class 'int'>
```

Python 里面万物皆对象（object），整型也不例外，只要是对象，就有相应的属性 （attributes） 和方法（methods）。

```python
b = dir(int)
print(b)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
# '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
# '__float__', '__floor__', '__floordiv__', '__format__', '__ge__',
# '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
# '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
# '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
# '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__',
# '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__',
# '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
# '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
# '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
# 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
# 'numerator', 'real', 'to_bytes']
```
对它们有个大概印象就可以了，具体怎么用，需要哪些参数 （argument），还需要查文档。看个`bit_length()`的例子。

【例子】找到一个整数的二进制表示，再返回其长度。
```python
a = 1031
print(bin(a))           # 0b10000000111
print(a.bit_length())   # 11
```

**浮点型**

【例子】
```python
print(1, type(1))
# 1 <class 'int'>

print(1., type(1.))
# 1.0 <class 'float'>

a = 0.00000023
b = 2.3e-7
print(a)  # 2.3e-07
print(b)  # 2.3e-07
```

有时候我们想保留浮点型的小数点后 `n` 位。可以用 `decimal` 包里的 `Decimal` 对象和 `getcontext()` 方法来实现。

```python
import decimal
from decimal import Decimal
```
Python 里面有很多用途广泛的包 (package)，用什么你就引进 (import) 什么。包也是对象，也可以用上面提到的`dir(decimal)` 来看其属性和方法。

【例子】`getcontext()` 显示了 `Decimal` 对象的默认精度值是 28 位 (`prec=28`)。
```python
import decimal
from decimal import Decimal

decimal.getcontext().prec = 4
b = Decimal(1) / Decimal(3)

print(b)

decimal.getcontext().prec = 4
c = Decimal(1012) / Decimal(3)
print(c)
```

**布尔型**

布尔 (boolean) 型变量只能取两个值，`True` 和 `False`。当把布尔型变量用在数字运算中，用 `1` 和 `0` 代表 `True` 和 `False`。

【例子】
```python
print(True + True)  # 2
print(True + False)  # 1
print(True * False)  # 0
```

除了直接给变量赋值 `True` 和 `False`，还可以用 `bool(X)` 来创建变量，其中 `X` 可以是

- 基本类型：整型、浮点型、布尔型
- 容器类型：字符串、元组、列表、字典和集合

【例子】`bool` 作用在基本类型变量：`X` 只要不是整型 `0`、浮点型 `0.0`，`bool(X)` 就是 `True`，其余就是 `False`。




确定`bool(X)` 的值是 `True` 还是 `False`，就看 `X` 是不是空，空的话就是 `False`，不空的话就是 `True`。

- 对于数值变量，`0`, `0.0` 都可认为是空的。
- 对于容器变量，里面没元素就是空的。

**获取类型信息**

- 获取类型信息 `type(object)`

【例子】
```python
print(isinstance(1, int))  # True
print(isinstance(5.2, float))  # True
print(isinstance(True, bool))  # True
print(isinstance('5.2', str))  # True
```


注：
- `type()` 不会认为子类是一种父类类型，不考虑继承关系。
- `isinstance()` 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 `isinstance()`。

**类型转换**

- 转换为整型 `int(x, base=10)`
- 转换为字符串 `str(object='')`
- 转换为浮点型 `float(x)`

【例子】
```python
print(int('520'))  # 520
print(int(520.52))  # 520
print(float('520.52'))  # 520.52
print(float(520))  # 520.0
print(str(10 + 10))  # 20
print(str(10.1 + 5.2))  # 15.3
```

### 5. print() 函数
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
- 将对象以字符串表示的方式格式化输出到流文件对象file里。其中所有非关键字参数都按`str()`方式进行转换为字符串输出；
- 关键字参数`sep`是实现分隔符，比如多个参数输出时想要输出中间的分隔字符；
- 关键字参数`end`是输出结束时的字符，默认是换行符`\n`；
- 关键字参数`file`是定义流输出的文件，可以是标准的系统输出`sys.stdout`，也可以重定义为别的文件；
- 关键字参数`flush`是立即把内容输出到流文件，不作缓存。

【例子】没有参数时，每次输出后都会换行。

```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed without 'end'and 'sep'.")
for item in shoplist:
    print(item)

# This is printed without 'end'and 'sep'.
# apple
# mango
# carrot
# banana
```

【例子】每次输出结束都用`end`设置的参数`&`结尾，并没有默认换行。
```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'end='&''.")
for item in shoplist:
    print(item, end='&')
print('hello world')

# This is printed with 'end='&''.
# apple&mango&carrot&banana&hello world
```


【例子】`item`值与`'another string'`两个值之间用`sep`设置的参数`&`分割。由于`end`参数没有设置，因此默认是输出解释后换行，即`end`参数的默认值为`\n`。

```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'sep='&''.")
for item in shoplist:
    print(item, 'another string', sep='&')

# This is printed with 'sep='&''.
# apple&another string
# mango&another string
# carrot&another string
# banana&another string
```


## 位运算

### 1. 原码、反码和补码

二进制有三种不同的表示形式：原码、反码和补码，<u>计算机内部使用补码来表示</u>。

**原码**：就是其二进制表示（注意，有一位符号位,第一是符号位，0表示整数，1表示负数）。
```python
00 00 00 11 -> 3
10 00 00 11 -> -3
```
**反码**：正数的反码就是原码，负数的反码是符号位不变，其余位取反（对应正数按位取反）。
```python
00 00 00 11 -> 3
11 11 11 00 -> -3
```
**补码**：正数的补码就是原码，负数的补码是反码+1。
```python
00 00 00 11 -> 3
11 11 11 01 -> -3
```
**符号位**：最高位为符号位，0表示正数，1表示负数。在位运算中符号位也参与运算。

### 2. 按位运算

- 按位非操作 ~

```python
~ 1 = 0
~ 0 = 1
```
`~` 把`num`的补码中的 0 和 1 全部取反（0 变为 1，1 变为 0）有符号整数的符号位在 `~` 运算中同样会取反。

```python
00 00 01 01 -> 5
~
---
11 11 10 10 -> -6

11 11 10 11 -> -5
~
---
00 00 01 00 -> 4
```

- 按位与操作 &  

```python
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
```
只有两个对应位都为 1 时才为 1
```python
00 00 01 01 -> 5
&
00 00 01 10 -> 6
---
00 00 01 00 -> 4
```
- 按位或操作 |


```python
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
```

只要两个对应位中有一个 1 时就为 1
```python
00 00 01 01 -> 5
|
00 00 01 10 -> 6
---
00 00 01 11 -> 7
```
- 按位异或操作 ^



```python
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
```

只有两个对应位不同时才为 1

```python
00 00 01 01 -> 5
^
00 00 01 10 -> 6
---
00 00 00 11 -> 3
```

异或操作的性质：满足交换律和结合律
```python
A: 00 00 11 00
B: 00 00 01 11

A^B: 00 00 10 11
B^A: 00 00 10 11

A^A: 00 00 00 00
A^0: 00 00 11 00

A^B^A: = A^A^B = B = 00 00 01 11
```
- 按位左移操作 <<

`num << i` 将`num`的二进制表示向左移动`i`位所得的值。

```python
00 00 10 11 -> 11
11 << 3
---
01 01 10 00 -> 88 
```

- 按位右移操作 >>

`num >> i` 将`num`的二进制表示向右移动`i`位所得的值。
```python
00 00 10 11 -> 11
11 >> 2
---
00 00 00 10 -> 2 
```

### 3. 利用位运算实现快速计算

通过 `<<`，`>>` 快速计算2的倍数问题。

```python
n << 1 -> 计算 n*2
n >> 1 -> 计算 n/2，负奇数的运算不可用
n << m -> 计算 n*(2^m)，即乘以 2 的 m 次方
n >> m -> 计算 n/(2^m)，即除以 2 的 m 次方
1 << n -> 2^n
```

通过 `^` 快速交换两个整数。（异或交换律）
```python
a ^= b
b ^= a
a ^= b
```

通过 `a & (-a)` 快速获取`a`的最后为 1 位置的整数。

```python
00 00 01 01 -> 5
&
11 11 10 11 -> -5
---
00 00 00 01 -> 1

00 00 11 10 -> 14
&
11 11 00 10 -> -14
---
00 00 00 10 -> 2
```

### 4. 利用位运算实现整数集合

一个数的二进制表示可以看作是一个集合（0 表示不在集合中，1 表示在集合中）。

比如集合 `{1, 3, 4, 8}`，可以表示成 `01 00 01 10 10` 而对应的位运算也就可以看作是对集合进行的操作。

元素与集合的操作：
```python
a | (1<<i)  -> 把 i 插入到集合中
a & ~(1<<i) -> 把 i 从集合中删除
a & (1<<i)  -> 判断 i 是否属于该集合（零不属于，非零属于）
```

集合之间的操作：
```python
a 补   -> ~a
a 交 b -> a & b
a 并 b -> a | b
a 差 b -> a & (~b)
```


注意：整数在内存中是以补码的形式存在的，输出自然也是按照补码输出。

【例子】C#语言输出负数。
```C#
class Program
{
    static void Main(string[] args)
    {
        string s1 = Convert.ToString(-3, 2);
        Console.WriteLine(s1); 
        // 11111111111111111111111111111101
        
        string s2 = Convert.ToString(-3, 16);
        Console.WriteLine(s2); 
        // fffffffd
    }
}
```

【例子】 Python 的`bin()` 输出。
```python
print(bin(3))  # 0b11
print(bin(-3))  # -0b11

print(bin(-3 & 0xffffffff))  
# 0b11111111111111111111111111111101

print(bin(0xfffffffd))       
# 0b11111111111111111111111111111101

print(0xfffffffd)  # 4294967293
```

是不是很颠覆认知，我们从结果可以看出：

- Python中`bin`一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号，巨坑。
- Python中的整型是补码形式存储的。
- Python中整型是不限制长度的不会超范围溢出。

所以为了获得负数（十进制表示）的补码，需要手动将其和十六进制数`0xffffffff`进行按位与操作，再交给`bin()`进行输出，得到的才是负数的补码表示。


## 条件语句

### 1. if 语句
```python
if expression:
    expr_true_suite
```
- if 语句的 `expr_true_suite` 代码块只有当条件表达式 `expression` 结果为真时才执行，否则将继续执行紧跟在该代码块后面的语句。
- 单个 if 语句中的 `expression` 条件表达式可以通过布尔操作符 `and`，`or`和`not` 实现多重条件判断。

【例子】
```python
if 2 > 1 and not 2 > 3:
    print('Correct Judgement!')

# Correct Judgement!
```


### 2. if - else 语句


```python
if expression:
    expr_true_suite
else:
    expr_false_suite
```
- Python 提供与 if 搭配使用的 else，如果 if 语句的条件表达式结果布尔值为假，那么程序将执行 else 语句后的代码。

【例子】
```python
temp = input("猜一猜小姐姐想的是哪个数字？")
guess = int(temp) # input 函数将接收的任何数据类型都默认为 str。
if guess == 666:
    print("你太了解小姐姐的心思了！")
    print("哼，猜对也没有奖励！")
else:
    print("猜错了，小姐姐现在心里想的是666！")
print("游戏结束，不玩儿啦！")
```


`if`语句支持嵌套，即在一个`if`语句中嵌入另一个`if`语句，从而构成不同层次的选择结构。

【例子】Python 使用缩进而不是大括号来标记代码块边界，因此要特别注意`else`的悬挂问题。
``` python
hi = 6
if hi > 2:
    if hi > 7:
        print('好棒!好棒!')
else:
    print('切~')

# 无输出
```
【例子】
```python
temp = input("猜一猜小姐姐想的是哪个数字？")
guess = int(temp)
if guess > 8:
    print("大了，大了")
else:
    if guess == 8:
        print("你太了解小姐姐的心思了！")
        print("哼，猜对也没有奖励！")
    else:
        print("小了，小了")
print("游戏结束，不玩儿啦！")
```

### 3. if - elif - else 语句

```python
if expression1:
    expr1_true_suite
elif expression2:
    expr2_true_suite
    .
    .
elif expressionN:
    exprN_true_suite
else:
    expr_false_suite
```

- elif 语句即为 else if，用来检查多个表达式是否为真，并在为真时执行特定代码块中的代码。

【例子】
```python
temp = input('请输入成绩:')
source = int(temp)
if 100 >= source >= 90:
    print('A')
elif 90 > source >= 80:
    print('B')
elif 80 > source >= 60:
    print('C')
elif 60 > source >= 0:
    print('D')
else:
    print('输入错误！')
```
### 4. assert 关键词

- `assert`这个关键词我们称之为“断言”，当这个关键词后边的条件为 False 时，程序自动崩溃并抛出`AssertionError`的异常。

【例子】
```python
my_list = ['lsgogroup']
my_list.pop(0)
assert len(my_list) > 0

# AssertionError
```
```python
assert 3 > 7

# AssertionError
```

## 循环语句


### 1. while 循环

`while`语句最基本的形式包括一个位于顶部的布尔表达式，一个或多个属于`while`代码块的缩进语句。

```python
while 布尔表达式:
    代码块
```

`while`循环的代码块会一直循环执行，直到布尔表达式的值为布尔假。

如果布尔表达式不带有`<、>、==、！=、in、not in`等运算符，仅仅给出数值之类的条件，也是可以的。当`while`后写入一个非零整数时，视为真值，执行循环体；写入`0`时，视为假值，不执行循环体。也可以写入`str、list`或任何序列，长度非零则视为真值，执行循环体；否则视为假值，不执行循环体。

【例子】

```python
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
```

---
### 2. while - else 循环

```python
while 布尔表达式:
    代码块
else:
    代码块
```

当`while`循环正常执行完的情况下，执行`else`输出，如果`while`循环中执行了跳出循环的语句，比如 `break`，将不执行`else`代码块的内容。    

【例子】

```python
count = 0
while count < 5:
    print("%d is  less than 5" % count)
    count = count + 1
else:
    print("%d is not less than 5" % count)
    
# 0 is  less than 5
# 1 is  less than 5
# 2 is  less than 5
# 3 is  less than 5
# 4 is  less than 5
# 5 is not less than 5
```

【例子】

```python
count = 0
while count < 5:
    print("%d is  less than 5" % count)
    count = 6
    break
else:
    print("%d is not less than 5" % count)

# 0 is  less than 5
```

---
### 3. for 循环

`for`循环是迭代循环，在Python中相当于一个通用的序列迭代器，可以遍历任何有序序列，如`str、list、tuple`等，也可以遍历任何可迭代对象，如`dict`。

```python
for 迭代变量 in 可迭代对象:
    代码块
```
每次循环，迭代变量被设置为可迭代对象的当前元素，提供给代码块使用。

【例子】

```python
for i in 'ILoveLSGO':
    print(i, end=' ')  # 不换行输出

# I L o v e L S G O
```

【例子】

```python
member = ['张三', '李四', '刘德华', '刘六', '周润发']
for each in member:
    print(each)

# 张三
# 李四
# 刘德华
# 刘六
# 周润发

for i in range(len(member)):
    print(member[i])

# 张三
# 李四
# 刘德华
# 刘六
# 周润发
```

【例子】

```python
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key, value in dic.items():
    print(key, value, sep=':', end=' ')
    
# a:1 b:2 c:3 d:4 
```

【例子】

```python
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for key in dic.keys():
    print(key, end=' ')
    
# a b c d 
```

【例子】

```python
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for value in dic.values():
    print(value, end=' ')
    
# 1 2 3 4
```

---
### 4. for - else 循环

```python
for 迭代变量 in 可迭代对象:
    代码块
else:
    代码块
```

当`for`循环正常执行完的情况下，执行`else`输出，如果`for`循环中执行了跳出循环的语句，比如 `break`，将不执行`else`代码块的内容，与`while - else`语句一样。

【例子】

```python
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

# 10 等于 2 * 5
# 11 是一个质数
# 12 等于 2 * 6
# 13 是一个质数
# 14 等于 2 * 7
# 15 等于 3 * 5
# 16 等于 2 * 8
# 17 是一个质数
# 18 等于 2 * 9
# 19 是一个质数
```

---
### 5. range() 函数

```python
range([start,] stop[, step=1])
```
- 这个BIF（Built-in functions）有三个参数，其中用中括号括起来的两个表示这两个参数是可选的。
- `step=1` 表示第三个参数的默认值是1。
- `range` 这个BIF的作用是生成一个从`start`参数的值开始到`stop`参数的值结束的数字序列，该序列包含`start`的值但不包含`stop`的值。

【例子】

```python
for i in range(2, 9):  # 不包含9
    print(i)

# 2
# 3
# 4
# 5
# 6
# 7
# 8
```

【例子】

```python
for i in range(1, 10, 2):
    print(i)

# 1
# 3
# 5
# 7
# 9
```

---
### 6. enumerate()函数

```python
enumerate(sequence, [start=0])
```
- sequence：一个序列、迭代器或其他支持迭代对象。
- start：下标起始位置。
- 返回 enumerate(枚举) 对象

【例子】

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
lst = list(enumerate(seasons))
print(lst)
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
lst = list(enumerate(seasons, start=1))  # 下标从 1 开始
print(lst)
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

`enumerate()`与 for 循环的结合使用。

```python
for i, a in enumerate(A)
    do something with a  
```
用 `enumerate(A)` 不仅返回了 `A` 中的元素，还顺便给该元素一个索引值 (默认从 0 开始)。此外，用 `enumerate(A, j)` 还可以确定索引起始值为 `j`。

【例子】

```python
languages = ['Python', 'R', 'Matlab', 'C++']
for language in languages:
    print('I love', language)
print('Done!')
# I love Python
# I love R
# I love Matlab
# I love C++
# Done!


for i, language in enumerate(languages, 2):
    print(i, 'I love', language)
print('Done!')
# 2 I love Python
# 3 I love R
# 4 I love Matlab
# 5 I love C++
# Done!
```

---
### 7. break 语句

`break`语句可以跳出当前所在层的循环。

【例子】

```python
import random
secret = random.randint(1, 10) #[1,10]之间的随机数

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
```

---
### 8. continue 语句

`continue`终止本轮循环并开始下一轮循环。

【例子】

```python
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)

# 2
# 1
# 4
# 3
# 6
# 5
# 8
# 7
# 10
# 9
```

---
### 9. pass 语句

`pass` 语句的意思是“不做任何事”，如果你在需要有语句的地方不写任何语句，那么解释器会提示出错，而 `pass` 语句就是用来解决这些问题的。

【例子】
```python
def a_func():

# SyntaxError: unexpected EOF while parsing
```

【例子】

```python
def a_func():
    pass
```
`pass`是空语句，不做任何操作，只起到占位的作用，其作用是为了保持程序结构的完整性。尽管`pass`语句不做任何操作，但如果暂时不确定要在一个位置放上什么样的代码，可以先放置一个`pass`语句，让代码可以正常运行。

---
### 10. 推导式

#### 列表推导式

```python
[ expr for value in collection [if condition] ]
```

【例子】

```python
x = [-4, -2, 0, 2, 4]
y = [a * 2 for a in x]
print(y)
# [-8, -4, 0, 4, 8]
```

【例子】

```python
x = [i ** 2 for i in range(1, 10)]
print(x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

【例子】

```python
x = [(i, i ** 2) for i in range(6)]
print(x)

# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

【例子】

```python
x = [i for i in range(100) if (i % 2) != 0 and (i % 3) == 0]
print(x)

# [3, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 81, 87, 93, 99]
```

【例子】

```python
a = [(i, j) for i in range(0, 3) for j in range(0, 3)]
print(a)

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

【例子】

```python
x = [[i, j] for i in range(0, 3) for j in range(0, 3)]
print(x)
# [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

x[0][0] = 10
print(x)
# [[10, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
```

【例子】

```python
a = [(i, j) for i in range(0, 3) if i < 1 for j in range(0, 3) if j > 1]
print(a)

# [(0, 2)]
```

#### 元组推导式

```python
( expr for value in collection [if condition] )
```

【例子】

```python
a = (x for x in range(10))
print(a)

# <generator object <genexpr> at 0x0000025BE511CC48>

print(tuple(a))

# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

#### 字典推导式

```python
{ key_expr: value_expr for value in collection [if condition] }
```

【例子】

```python
b = {i: i % 2 == 0 for i in range(10) if i % 3 == 0}
print(b)
# {0: True, 3: False, 6: True, 9: False}
```

#### 集合推导式

```python
{ expr for value in collection [if condition] }
```

【例子】

```python
c = {i for i in [1, 2, 3, 4, 5, 5, 6, 4, 3, 2, 1]}
print(c)
# {1, 2, 3, 4, 5, 6}
```

#### 其它

- `next(iterator[, default])` Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising Stop Iteration.

【例子】

```python
e = (i for i in range(10))
print(e)
# <generator object <genexpr> at 0x0000007A0B8D01B0>

print(next(e))  # 0
print(next(e))  # 1

for each in e:
    print(each, end=' ')

# 2 3 4 5 6 7 8 9
```

【例子】

```python
s = sum([i for i in range(101)])
print(s)  # 5050
s = sum((i for i in range(101)))
print(s)  # 5050
```



## 异常处理

异常就是运行期检测到的错误。计算机语言针对可能出现的错误定义了异常类型，某种错误引发对应的异常时，异常处理程序将被启动，从而恢复程序的正常运行。

### 1. Python 标准异常总结

- BaseException：所有异常的 **基类**
- Exception：常规异常的 **基类**
- StandardError：所有的内建标准异常的基类
- ArithmeticError：所有数值计算异常的基类
- FloatingPointError：浮点计算异常
- <u>OverflowError</u>：数值运算超出最大限制
- <u>ZeroDivisionError</u>：除数为零
- <u>AssertionError</u>：断言语句（assert）失败
- <u>AttributeError</u>：尝试访问未知的对象属性
- EOFError：没有内建输入，到达EOF标记
- EnvironmentError：操作系统异常的基类
- IOError：输入/输出操作失败
- <u>OSError</u>：操作系统产生的异常（例如打开一个不存在的文件）
- WindowsError：系统调用失败
- <u>ImportError</u>：导入模块失败的时候
- KeyboardInterrupt：用户中断执行
- LookupError：无效数据查询的基类
- <u>IndexError</u>：索引超出序列的范围
- <u>KeyError</u>：字典中查找一个不存在的关键字
- <u>MemoryError</u>：内存溢出（可通过删除对象释放内存）
- <u>NameError</u>：尝试访问一个不存在的变量
- UnboundLocalError：访问未初始化的本地变量
- ReferenceError：弱引用试图访问已经垃圾回收了的对象
- RuntimeError：一般的运行时异常
- NotImplementedError：尚未实现的方法
- <u>SyntaxError</u>：语法错误导致的异常
- IndentationError：缩进错误导致的异常
- TabError：Tab和空格混用
- SystemError：一般的解释器系统异常
- <u>TypeError</u>：不同类型间的无效操作
- <u>ValueError</u>：传入无效的参数
- UnicodeError：Unicode相关的异常
- UnicodeDecodeError：Unicode解码时的异常
- UnicodeEncodeError：Unicode编码错误导致的异常
- UnicodeTranslateError：Unicode转换错误导致的异常

异常体系内部有层次关系，Python异常体系中的部分关系如下所示：


![](https://gitee.com/niu_dehua/oss/raw/master/uPic/SF51E36otkNDlQ9.png)



---
### 2. Python标准警告总结

- Warning：警告的基类

- DeprecationWarning：关于被弃用的特征的警告

- FutureWarning：关于构造将来语义会有改变的警告

- UserWarning：用户代码生成的警告

- PendingDeprecationWarning：关于特性将会被废弃的警告

- RuntimeWarning：可疑的运行时行为(runtime behavior)的警告

- SyntaxWarning：可疑语法的警告

- ImportWarning：用于在导入模块过程中触发的警告

- UnicodeWarning：与Unicode相关的警告

- BytesWarning：与字节或字节码相关的警告

- ResourceWarning：与资源使用相关的警告

  ---

### 3. try - except 语句
```python
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
```

try 语句按照如下方式工作：
- 首先，执行`try`子句（在关键字`try`和关键字`except`之间的语句）
- 如果没有异常发生，忽略`except`子句，`try`子句执行后结束。
- 如果在执行`try`子句的过程中发生了异常，那么`try`子句余下的部分将被忽略。如果异常的类型和`except`之后的名称相符，那么对应的`except`子句将被执行。最后执行`try - except`语句之后的代码。
- 如果一个异常没有与任何的`except`匹配，那么这个异常将会传递给上层的`try`中。

【例子】

```python
try:
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError:
    print('打开文件出错')

# 打开文件出错
```

【例子】

```python
try:
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError as error:
    print('打开文件出错\n原因是：' + str(error))

# 打开文件出错
# 原因是：[Errno 2] No such file or directory: 'test.txt'
```

【例子】一个`try`语句可能包含多个`except`子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

```python
try:
    int("abc")
    s = 1 + '1'
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError as error:
    print('打开文件出错\n原因是：' + str(error))
except TypeError as error:
    print('类型出错\n原因是：' + str(error))
except ValueError as error:
    print('数值出错\n原因是：' + str(error))

# 数值出错
# 原因是：invalid literal for int() with base 10: 'abc'
```

【例子】`try-except-else`语句尝试查询不在`dict`中的键值对，从而引发了异常。这一异常准确地说应属于`KeyError`，但由于`KeyError`是`LookupError`的子类，且将`LookupError`置于`KeyError`之前，因此程序优先执行该`except`代码块。所以，使用多个`except`代码块时，必须坚持对其规范排序，要从最具针对性的异常到最通用的异常。

```python
dict1 = {'a': 1, 'b': 2, 'v': 22}
try:
    x = dict1['y']
except LookupError:
    print('查询错误')
except KeyError:
    print('键错误')
else:
    print(x)
    
# 查询错误
```

【例子】

```python
dict1 = {'a': 1, 'b': 2, 'v': 22}
try:
    x = dict1['y']
except KeyError:
    print('键错误')
except LookupError:
    print('查询错误')
else:
    print(x)

# 键错误
```

【例子】一个 `except` 子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组。

```python
try:
    s = 1 + '1'
    int("abc")
    f = open('test.txt')
    print(f.read())
    f.close()
except (OSError, TypeError, ValueError) as error:
    print('出错了！\n原因是：' + str(error))

# 出错了！
# 原因是：unsupported operand type(s) for +: 'int' and 'str'
```

---
### 4. try - except - finally 语句
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
finally:
    无论如何都会被执行的代码

不管`try`子句里面有没有发生异常，`finally`子句都会执行。



【例子】如果一个异常在`try`子句里被抛出，而又没有任何的`except`把它截住，那么这个异常会在`finally`子句执行后被抛出。

```python
def divide(x, y):
    try:
        result = x / y
        print("result is", result)
    except ZeroDivisionError:
        print("division by zero!")
    finally:
        print("executing finally clause")


divide(2, 1)
# result is 2.0
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause
divide("2", "1")
# executing finally clause
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

---
### 5. try - except - else 语句

如果在`try`子句执行时没有发生异常，Python将执行`else`语句后的语句。

```python
try:
    检测范围
except:
    出现异常后的处理代码
else:
    如果没有异常执行这块代码
```

使用`except`而不带任何异常类型，这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息，因为它捕获所有的异常。

```python
try:
    检测范围
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
else:
    如果没有异常执行这块代码
    
【例子】
```

```python
try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 内容写入文件成功
```

注意：`else`语句的存在必须以`except`语句的存在为前提，在没有`except`语句的`try`语句中使用`else`语句，会引发语法错误。

---
### 6. raise语句

Python 使用`raise`语句抛出一个指定的异常。

【例子】

```python
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    
# An exception flew by!
```

