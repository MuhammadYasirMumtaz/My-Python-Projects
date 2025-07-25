def EvenOdd(x):
    if x%2 == 0:
        return "Even" 
    else:
        return "Odd"

x = int(input("Enter a Number: "))

result = EvenOdd(x)
print("The Give Number", x , "is", result)
    


