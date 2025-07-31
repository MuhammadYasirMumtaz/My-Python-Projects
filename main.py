lst1 = ['a', 'b', 'c']
lst2 = [10, 20, 30]
d = {}

for i in range(len(lst1)):
    for j in range(len(lst2)):
        d[lst1[i]] = lst2[j] 

print(d)
