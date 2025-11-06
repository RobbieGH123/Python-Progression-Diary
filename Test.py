lower_number = int(input("Give me a lower number: "))
higher_number = int(input("Give me a higher number: "))

custom_list = []

for i in range(lower_number, higher_number):
    if i % 3 == 0 and i % 5 == 0:
     custom_list.append('Fizzbuzz')
    elif i % 3 == 0:
     custom_list.append('Fizz')
    elif i % 5 == 0:
     custom_list.append('Buzz')
    else:
     custom_list.append(i)
print(custom_list)

number = 1248
print(str(number)[1])


