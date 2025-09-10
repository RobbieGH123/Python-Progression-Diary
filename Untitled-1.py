def double(a):
    return a * 2

users_number = int(input("Please give me a number: "))
print("Now I am going to double your number:")

if users_number != 0:
 result = double(users_number)
 print(f"\nDouble your number is {result}")
else:
   print("You cannot double zero")
