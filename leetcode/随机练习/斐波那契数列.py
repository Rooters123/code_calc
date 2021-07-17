# encoding = utf-8
def fib(n):
    sum = 0
    inter = 1
    count = 0
    while count < n :
        print(sum)
        sum,inter = sum+inter,sum
        count += 1
    # return sum
print(fib(10))

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()