list1 = ['1','6']
list2 = ['5','4']
dict1 = dict()
for l,k in enumerate(list1):
    dict1[k]= list2[l]
print(dict1)


dict2 = dict(zip(list1,list2))
print(dict2)
