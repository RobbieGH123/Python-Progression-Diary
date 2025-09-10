import random
secret_number = random.randint(1, 20)
counter_index = 0
guess = int(input("I am thinking of a number between 1 and 20, what do you think it is? "))
while guess != secret_number and counter_index < 4:
    counter_index += 1 
    guess = int(input("You are incorrect, please try again: "))
if guess == secret_number:
        print("Well done, correct!")
else: 
    print(f"\nYou have used all of your attempts, the number I was thinking of was {secret_number} ")
    
    
    