'''
yield:就像是一个迭代器
有它的函数就是一个生成器函数
'''


def my_rshu(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            yield l[i]
        i += 1


if __name__ == '__main__':
    list1 = [1, 3, 2, 4, 8, 3, 6, 10, 13, 24]
    n = my_rshu(list1)
    for j in n:
        print(j)
