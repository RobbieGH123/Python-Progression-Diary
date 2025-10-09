## String Slicing

print(f"{'STRING SLICING:':^200}")
s = "String Slicing Practice"
print(s[0:2])                             # Prints Indexes 0 and 1, -> St
print(s[-1])                              # Negative Slicing (Starts at end) -> e

print(s[-3:])                             # Last 3 letters -> ice
print(s[0:len(s):2])                      # Starts at Index 0, Stops at the end, moves by 2 each time -> Srn lcn rcie

## f-strings learn/refresh

# Decimal Places
print(f"{'DECIMAL PLACES:':^200}")
import math                               # Imports a Math Library
pi = math.pi                              # Initialises Pi
print(f"pi: {pi}")                        # 3.14159265358... etc
print(f"pi to 2 decimals: {pi:.2f}")      # 3.14 (Prints pi to 2 Decimal Points)

# Expressions

print(f"{'Expressions:':^200}")
print(f"3 x 15: {3 * 15}")                # 45
print(f"26 + 26: {26 + 26}")              # 52

# Padding

print(f"{'Padding:':^200}")
n = 42
print(f"{n:05}")                          # 00042 (pad with zeros to 5 digits)
print(f"{n:03}")                          # 042 (pad with zeros to 3 digits)

# Alignment 

print(f"{'ALIGNMENT:':^200}")
text = "Python"
print(f"{text:<10}|")                     # "Python    |" (left-aligned in 10 spaces)
print(f"{text:>10}|")                     # "    Python|" (right-aligned, also in 10 spaces)
print(f"{text:^10}|")                     # "  Python  |" (centered, in 10)

# f-strings vs .format()

print(f"{'f-Strings Vs. format():':^200}")            
name = input(f"What is your full name?: ")   

try:                                                         # Error Checking Block
    age = int(input("How old are you?: "))
except ValueError:
    print("Your age must be given in number format")
    age = None

if age is not None:                                          # If the age was provided correctly
    print(f"\nMy name is {name} and I am {age} years old.")           # f string
    print("My name is {} and I am {} years old.".format(name, age))   # .format() (f not required, uses wiggly brackets and .format(var) at the end )

print(f"\n3 x 15: {3 * 15}")
print("3 x 15: {}".format(3 * 15))

## 3 Small-medium string problems

# Reverse every word in a string but keep the same word order

print(f"{'STRING REVERSER:':^200}")
def string_reverser(str):                              

    new_string = ''                                         # To store the reversed string
    str = str.split()                                       # Splits the String into a list
    for word in str:                                        # For each iterable in the list
        reversed_word = word[::-1]                          # Reverse and store it
        new_string += reversed_word                         # Add to the PH List
        new_string += ' '                                   # Add a space
    return new_string 

print(string_reverser("Hello my name is Robbie"))

# Count how many Consonants & Vowels are in a String

print(f"{'VOWELS & CONSONANTS FUNCTION:':^200}")
def vowscons(str):
        vowels = 0
        consonants = 0 
        for char in str:                            # For each char in the str
            if char.isalpha():                      # If the character is a letter:
                if char.lower() in "aeiou":         # Check if it is a vowel
                   vowels += 1                      # If it is a vowel, add 1 to the total vowel counter
                else:                               # If it is not a vowel, it must be a consonant
                    consonants += 1                 # Add 1 to the total number of consonants
        return(vowels, consonants)                  # Return as a tuple

result = vowscons("Hello")                          # Store the tuple under the variable 'result'
print(f"In the given string, there are: {result[0]} vowels and {result[1]} consonants")  

# Checking if a string is a palindrome:

print(f"{'PALINDROME CHECKER USING STRING FUNCTIONS:':^200}")
def isPalindrome(str):

    """
    This is a Function that tests whether a given string is Palindrome, it uses string functions, .lower(), .alnum() to ignore Capital letters, spaces and punctuation marks
    
    >>> isPalindrome("Rac,..,ecar")
    True
    >>> isPalindrome("Hello")
    False
    """

    empty_string = ''
    str = str.lower()                                              # Convert to lowercase
    for char in str:                                               # For each character:
        if char.isalnum():                                         # If the character is a letter or a number
            empty_string += char                                   # Add it to the empty string PH
    if empty_string == empty_string[::-1]:                         # Once every character has been iterated over, check if it is the same forward and backwards
        return True
    else:                                                          # If it is not, then it is not a palindrome
        return False

if __name__ == "__main__":                                         # If the file is being ran directly
    import doctest                                                 # Import doctest
    doctest.testmod(verbose=True)                                  # Run doctests, "verbose=True" means that is shows the tests and results

## Find the most frequent character in a string:

print(f"{'FIND THE MOST OCCURING CHARACTER IN A STRING:':^200}")

def MostOcc(str):

    from collections import defaultdict
    characters = defaultdict(int)

    
    for char in str:
        if char.isalnum():
            characters[char] += 1
        MostOccuring = max(characters, key = characters.get)
    return MostOccuring

print(f"The most occuring Character was: {MostOcc("abchdfgehddfefefefddddfffff")}")

## Capitalise the first letter for every word in a string:

print(f"{'CAPITALISE THE FIRST LETTER OF EVERY WORD:':^200}")
def capitaliseWords(str):

    capitalisedWords = ''

    for word in str:
       word = word.replace(word[0],word[0].upper())
       capitalisedWords += word
    return capitalisedWords
#print(f"{capitaliseWords("this is a test of my capitalise words function")}")    

