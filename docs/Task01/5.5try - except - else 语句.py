# try - except - else 语句
# 如果在try子句执行时没有发生异常，Python将执行else语句后的语句。
"""
try:
    检测范围
except:
    出现异常后的处理代码
else:
    如果没有异常执行这块代码
"""
# 使用except而不带任何异常类型，这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息，因为它捕获所有的异常。
"""
try:
    检测范围
except(Exception1[, Exception2[, ...ExceptionN]]]):
    发生以上多个异常中的一个，执行这块代码
else:
如果没有异常执行这块代码
"""
""" 例子 """
# 注意：else语句的存在必须以except语句的存在为前提，在没有except语句的try语句中使用else语句，会引发语法错误。
try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 内容写入文件成功
