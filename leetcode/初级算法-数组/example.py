a = [
    [1,2,3,1,1,2],
    [2,2,3,1,1,2],
    [3,2,3,1,1,2],
    [4,2,3,1,1,2],
]

print(a[0])


dic1 = {3: 2, 5: 2, 2: 1, 50: 1}
dic2 = {3: 2, 5: 2}
news = dict(dic1.items() & dic2.items())


x = (0,1,2)

def consumer():
    while True:
        x = yield
        print("消费",x)
def produce():
    c = consumer()
    next(c)
    for i in range(10):
        print("生产",i)
        c.send(i)
produce()



def dec_to_ter(num):
    l = []
    if num < 0:
        return "- " + dec_to_ter(abs(num))#负数先转为正数，再调用函数主体
    else:
        while True:
            num,reminder = divmod(num,3)#算除法求除数和余数
            l.append(str(reminder))#将余数存入字符串
            if num == 0:
                return "".join(l[::-1])

print(dec_to_ter(100))


print(int("10201",3))

print('0' * -2)
