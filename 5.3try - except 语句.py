# try - except 语句
"""
try:
    检测范围
except Exception[as reason]:
    出现异常后的处理代码
"""
"""
try 语句按照如下方式工作：
首先，执行`try`子句（在关键字`try`和关键字`except`之间的语句）
如果没有异常发生，忽略`except`子句，`try`子句执行后结束。
如果在执行`try`子句的过程中发生了异常，那么`try`子句余下的部分将被忽略。如果异常的类型和`except`之后的名称相符，那么对应的`except`子句将被执行。最后执行`try - except`语句之后的代码。
如果一个异常没有与任何的`except`匹配，那么这个异常将会传递给上层的`try`中。
"""
""" 例子 """
try:
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError:
    print('打开文件出错')
# 打开文件出错

""" 例子 """
print()
try:
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError as error:
    print('打开文件出错\t原因是：' + str(error))
# 打开文件出错
# 原因是：[Errno 2] No such file or directory: 'test.txt'

""" 例子 """
print()
try:
    # int("abc")
    # s = 1 + '1'
    f = open('test.txt')
    print(f.read())
    f.close()
except OSError as error:
    print('打开文件出错\t原因是：' + str(error))
except TypeError as error:
    print('类型出错\t原因是：' + str(error))
except ValueError as error:
    print('数值出错\t原因是：' + str(error))
# 数值出错
# 原因是：invalid literal for int() with base 10: 'abc'

""" 例子 """
"""
`try-except-else`语句尝试查询不在`dict`中的键值对，从而引发了异常。这一异常准确地说应属于`KeyError`，但由于`KeyError`是`LookupError`的子类，且将`LookupError`置于`KeyError`之前，因此程序优先执行该`except`代码块。所以，使用多个`except`代码块时，必须坚持对其规范排序，要从最具针对性的异常到最通用的异常。
"""
print()
dict1 = {'a': 1, 'b': 2, 'v': 22}
try:
    x = dict1['y']
except LookupError as error:
    print('查询错误')
except KeyError:
    print('键错误')
else:
    print(x)
# 查询错误

""" 例子 """
print()
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

""" 【例子】一个 `except` 子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组。 """
print()
try:
    s = 1 + '1'
    int("abc")
    f = open('test.txt')
    print(f.read())
    f.close()
except (OSError, TypeError, ValueError) as error:
    print('出错了！\t原因是：' + str(error))
# 出错了！
# 原因是：unsupported operand type(s) for +: 'int' and 'str'
