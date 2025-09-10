def squarelist(a):
    return a ** 2
squared_numbers = []

bulletin = list(range(int(input("What is your number? "))))
for i in bulletin:
    result = squarelist(i)
    squared_numbers.append(result)
print(squared_numbers)
    

    
    

