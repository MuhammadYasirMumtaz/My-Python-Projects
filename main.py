n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
<<<<<<< HEAD
    for j in range(i):
        print("*", end=" ")
    print()
    
=======
    total += i
  
print("Sum of first", n, "natural numbers is:", total)
>>>>>>> e569f65d7eb06fee9383fe7bf2d62ec3dc25b553
