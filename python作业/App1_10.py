#编写程序，用户输入一个三位以上的整数，输出其百位以上的数字
#例如，用户输入1234，程序输出12
x = input('请输入一个三位以上的整数')
#y = str(x)
print(x[0:-2])
#切片操作返回，输出的仍是一个字符串，而不是输入‘1’，‘2’这样
