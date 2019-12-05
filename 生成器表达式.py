# def fun01(list1):
#     i = 0
#     while i < len(list1):
#         if type(list1[i]) == str:
#             yield list1[i]
#         i += 1
list2 = [1,2,'3',True,'a']
# for j in fun01(list2):
#     print(j)30
re = (i for i in list2 if type(i) == str)
for j in re:
    print(j)