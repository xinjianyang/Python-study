
d = {'jack':89,'tom':90,'rose':100}
print(d)
print(d['tom'])

d['admin'] = 67
print(len(d))
print(d['admin'])
print(d.get('jack1'))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-100.9))
#ax^2 + bx + c = 0

print("在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。")

print("用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件")
print("浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：")
