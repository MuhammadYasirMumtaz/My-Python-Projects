n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    
