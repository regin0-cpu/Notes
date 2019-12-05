list1 = ['a','b','c']
list2 = [101,102,103,104]
def my_zip(list3,list4):
    i = 0
    l = min(len(list3),len(list4))
    while i < l:
        yield (list3[i],list4[i])
        i += 1
#
# for k in zip(list1,list2,list1,list2):
#     print(k)


for j in my_zip(list1,list2):
    print(j)