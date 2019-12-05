'''
自定义异常类

'''
class AgeError(Exception):
    def __init__(self, ycxx, cwdm, id1):
        self.ycxx = ycxx
        self.cwdm = cwdm
        self.id = id1

