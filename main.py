lst = [1, 2, 3, 4, 5, 6]


for x in lst[:]:
    if x % 2 == 0:
        lst.remove(x) 
        print(f"Removed {x}, current list: {lst}")
    else:
        print(f"Odd number {x}, current list: {lst}")