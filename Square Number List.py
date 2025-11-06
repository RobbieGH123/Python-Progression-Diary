lst = [0, 1, 2, 3, 4, 5]
if (lst[1]+lst[2]) == 3:
    print("Correct")


def squarelist(a):
    return a ** 2
squared_numbers = []

bulletin = list(range(int(input("What is your number? "))))
for i in bulletin:
    result = squarelist(i)
    squared_numbers.append(result)
print(squared_numbers)
    

    
    

