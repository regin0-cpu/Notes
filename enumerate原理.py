'''
enumerate:枚举函数
生成器,生成元素及其索引
'''


def my_enumerate(l):
    i = 0
    while i < len(l):
        yield (i, l[i])
        i += 1


if __name__ == '__main__':
    list1 = ['a', 'b', 'c']
    for j, k in my_enumerate(list1):
        print(j)
