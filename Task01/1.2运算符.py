""" <b>算术运算符</b>

操作符 | 名称 | 示例
:---:|:---:|:---:
`+` | 加 | `1 + 1`
`-` | 减 | `2 - 1`
`*` | 乘 | `3 * 4`
`/` | 除 | `3 / 4`
`//`| 整除（地板除）| `3 // 4`
`%` | 取余| `3 % 4`
`**`| 幂 | `2 ** 3` """
print(1 + 1)  # 2
print(2 - 1)  # 1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(3 // 4)  # 0
print(3 % 4)  # 3
print(2**3)  # 8
""" <b>比较运算符</b>

操作符 | 名称 | 示例
:---:|:---:|:---:
`>` |大于| `2 > 1`
`>=`|大于等于| `2 >= 4`
`<` |小于| `1 < 2`
`<=`|小于等于| `5 <= 2`
`==`|等于| `3 == 4`
`!=`|不等于| `3 != 5` """
print(2 > 1)  # True
print(2 >= 4)  # False
print(1 < 2)  # True
print(5 <= 2)  # False
print(3 == 4)  # False
print(3 != 5)  # True
""" <b>逻辑运算符</b>

操作符 | 名称 | 示例
:---:|:---:|:---:
`and`|与| `(3 > 2) and (3 < 5)`
`or` |或| `(1 > 3) or (9 < 2)`
`not`|非| `not (2 > 1)` """
print((3 > 2) and (3 < 5))  # True
print((1 > 3) or (9 < 89))  # False
print(not (2 > 1))  # False
""" <b>位运算符</b>

操作符 | 名称 | 示例
:---:|:---:|:---:
`~` |按位取反|`~4`
`&` |按位与  |`4 & 5`
`|` |按位或  |`4 | 5`
`^` |按位异或|`4 ^ 5`
`<<`|左移    |`4 << 2`
`>>`|右移    |`4 >> 2` """
print(bin(4))  # 0b100
print(bin(5))  # 0b101
print(bin(~4), ~4)  # -0b101 -5
print(bin(4 & 5), 4 & 5)  # 0b100 4
print(bin(4 | 5), 4 | 5)  # 0b101 5
print(bin(4 ^ 5), 4 ^ 5)  # 0b1 1
print(bin(4 << 2), 4 << 2)  # 0b10000 16
print(bin(4 >> 2), 4 >> 2)  # 0b1 1
""" <b>三元运算符</b> """
x, y = 4, 5
if x < y:
    small = x
else:
    small = y

print(small)  # 4
x, y = 4, 5
small = x if x < y else y
print(small)  # 4
""" <b>其他运算符</b>

操作符 | 名称 | 示例
:---:|:---:|:---:
`in`|存在| `'A' in ['A', 'B', 'C']`
`not in`|不存在|`'h' not in ['A', 'B', 'C']`
`is`|是| `"hello" is "hello"`
`not is`|不是|`"hello" is not "hello"` """

letters = ['A', 'B', 'C']
if 'A' in letters:
    print('A' + ' exists')
if 'h' not in letters:
    print('h' + ' not exists')

# A exists
# h not exists
# 比较的两个变量均指向不可变类型
a = "hello"
b = "hello"
print(a is b, a == b)  # True True
print(a is not b, a != b)  # False False
# 比较的两个变量均指向可变类型。
a = ["hello"]
b = ["hello"]
print(a is b, a == b)  # False True
print(a is not b, a != b)  # True False
""" 注意：
- is, is not 对比的是两个变量的内存地址
- ==, != 对比的是两个变量的值
- 比较的两个变量，指向的都是地址不可变的类型（str等），那么is，is not 和 ==，！= 是完全等价的。
- 对比的两个变量，指向的是地址可变的类型（list，dict，tuple等），则两者是有区别的。 """
letters2 = ['A', 'B', 'C']
print(letters is letters2, letters == letters2)
""" <b>运算符的优先级</b>

- 一元运算符优于二元运算符。例如`3 ** -2`等价于`3 ** (-2)`。
- 先算术运算，后移位运算，最后位运算。例如 `1 << 3 + 2 & 7`等价于 `(1 << (3 + 2)) & 7`。
- 逻辑运算最后结合。例如`3 < 4 and 4 < 5`等价于`(3 < 4) and (4 < 5)`。 """
print(-3**2)  # -9
print(3**-2)  # 0.1111111111111111
print(1 << 3 + 2 & 7)  # 0
print(-3 * 2 + 5 / -2 - 4)  # -12.5
print(3 < 4 and 4 < 5)  # True
