from functools import reduce


lst = [1,2,3,4,6,7,9,5,0]

sum = reduce(lambda x, y: x + y, lst)
print("The Sum is:",sum)
    

