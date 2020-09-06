# 简介

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

# 变量、运算符与数据类型

## 1.注释

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

## 2.运算符
<b>算术运算符</b>

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

<b>比较运算符</b>

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

<b>逻辑运算符</b>

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

<b>位运算符</b>

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

<b>三元运算符</b>

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
small = x if x < y else y
print(small)  # 4
```


<b>其他运算符</b>

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


<b>运算符的优先级</b>

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

## 3. 变量和赋值

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

## 4. 数据类型与转换


类型 | 名称 | 示例
:---:|:---:|:---:
int | 整型 `<class 'int'>`| `-876, 10`
float | 浮点型`<class 'float'>`| `3.149, 11.11`
bool | 布尔型`<class 'bool'>` | `True, False`

<b>整型</b>

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


<b>浮点型</b>

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
decimal.getcontext().prec = 4
b = Decimal(1) / Decimal(3)

print(b)

decimal.getcontext().prec = 4
c = Decimal(1012) / Decimal(3)
print(c)
```

<b>布尔型</b>

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


<b>获取类型信息</b>

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

## 5. print() 函数
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


# 位运算

## 1. 原码、反码和补码

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

## 2. 按位运算

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

## 3. 利用位运算实现快速计算

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

## 4. 利用位运算实现整数集合

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


