class Next:
    def __init__(self,list2):
        self.list1 = list2
        self.index = -1
    def __next__(self):
        if self.index < len(self.list1)-1:
            self.index += 1
            return self.list1[self.index]
        else:
            raise StopIteration
class GraphiManager:
    def __init__(self):
        self.__gr_list = []
    def setvalue(self,value):
        self.__gr_list.append(value)
    def __iter__(self):
        return Next(self.__gr_list)

g01 = GraphiManager()
g01.setvalue('三角形')
g01.setvalue('圆')
g01.setvalue('正方形')
i01 = g01.__iter__()
while True:
    try:
        im01 = i01.__next__()
        print(im01)
    except StopIteration:
        break
