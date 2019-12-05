"""
    lambda : 匿名函数
    作用:充当函数
    lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
    lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。
    lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数

"""

# 无参数 无返回值
a = lambda :print("fun01")
a()

def fun02(func):
    print("fun02")
    func()

# 将函数作为参数,建议使用lambda.
fun02(lambda :print("fun01"))


# 有参数lambda
b = lambda a,b,c:print("fun03")


# lambda 函数体只能有一句话
# fun02(lambda :print("fun04++");print("fun04又执行喽"))
# 不支持赋值语句
# fun02(lambda a:a.name = "zs")