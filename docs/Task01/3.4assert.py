my_list = ['lsgogroup']
my_list.pop(0)
assert len(my_list) > 0
# AssertionError

# 【例子】在进行单元测试时，可以用来在程序中置入检查点，只有条件为 True 才能让程序正常工作。
assert 3 > 7
# AssertionError
