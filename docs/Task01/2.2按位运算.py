""" 按位非操作 ~ """
# `~` 把`num`的补码中的 0 和 1 全部取反（0 变为 1，1 变为 0）有符号整数的符号位在 `~` 运算中同样会取反。
# 00 00 01 01 -> 5
# ~
# ---
# 11 11 10 10 -> -6
# 11 11 10 11 -> -5
# ~
# ---
# 00 00 01 00 -> 4


""" 按位与操作 & """
# 只有两个对应位都为 1 时才为 1
# 00 00 01 01 -> 5
# &
# 00 00 01 10 -> 6
# ---
# 00 00 01 00 -> 4

""" 按位或操作 | """
# 只要两个对应位中有一个 1 时就为 1
# 00 00 01 01 -> 5
# |
# 00 00 01 10 -> 6
# ---
# 00 00 01 11 -> 7

""" 按位异或操作 ^ """
# 只有两个对应位不同时才为 1
# 00 00 01 01 -> 5
# ^
# 00 00 01 10 -> 6
# ---
# 00 00 00 11 -> 3
# 异或操作的性质：满足交换律和结合律
# A: 00 00 11 00
# B: 00 00 01 11

# A^B: 00 00 10 11
# B^A: 00 00 10 11

# A^A: 00 00 00 00
# A^0: 00 00 11 00

# A^B^A: = A^A^B = B = 00 00 01 11

""" 按位左移操作 """
# `num << i` 将`num`的二进制表示向左移动`i`位所得的值。
# 00 00 10 11 -> 11
# 11 << 3
# ---
# 01 01 10 00 -> 88 

""" 按位右移操作 """
# `num >> i` 将`num`的二进制表示向右移动`i`位所得的值。
# 00 00 10 11 -> 11
# 11 >> 2
# ---
# 00 00 00 10 -> 2 