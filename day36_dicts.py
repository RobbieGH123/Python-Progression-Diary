## day36_dicts.py

print(f"{'DICTIONARIES & HASH MAPS PRACTICE:':^200}")

Protein_per_hundred_grams = {             # Initalizing with Mulitple Values
"Mozzarella": 18,
"Pumpkin_seeds": 30,
"Peanuts": 27,
"Edam": 27,
"Cheddar": 25,
"Almonds": 21,
"Pistachios": 20,
"Tempeh": 20,
"Cashew_nuts": 18
}

Protein_per_hundred_grams.update({         # Adding Multiple Items at once
    "Greek Yoghurt": 10,       
    "Cottage Cheese": 10,
    "Quinoa": 4
})


# Safer way of calling Key Values, does not crash if they key does not exist in your dictionary



# Updating existing keys
print()
Protein_per_hundred_grams["Mozzarella"] += 1    # Adds to an existing Key/Value Pairs' value
print(Protein_per_hundred_grams["Mozzarella"])  # Prints a Keys' Value
print()
Protein_per_hundred_grams["Mozzarella"] = 18    # Overwriting an existing Key/Value Pair's value
print(Protein_per_hundred_grams["Mozzarella"])

del Protein_per_hundred_grams["Pistachios"]     # Deletes a Key/Value Pair

# Retrieving Values
print(Protein_per_hundred_grams.get("Tempeh"))                  # returns 20
print(Protein_per_hundred_grams.get("Avocados"))                # returns None instead of crashing
print(Protein_per_hundred_grams.get("Egg", "Key not found"))    # returns "Key not found" instead of None (default value)

# Displaying the Dictionary
print()
print(Protein_per_hundred_grams.keys())       # Displays Dictionaries Keys only
print()
print(Protein_per_hundred_grams.values())     # Displays Dictionaries Values only
print()
print(Protein_per_hundred_grams)              # Prints Key/Value Pairs
print()
print(Protein_per_hundred_grams.items())      # Displays Key/Value Pairs as Tuples
print()

#======================================================================================================================================================================#
print(f"{'Default Dictionaries:':^200}")

print()
from collections import defaultdict     # Requires importing
letters = defaultdict(int)              # Establishes letters as a default dictionary recording integer values
for ch in "abracadabra":                # For each character in abracadabra
    letters[ch] += 1                    # Add 1 to its value, even if the key does not currently exist, it will initialise it with the value 1
print(letters)                          # Print the dictionary
print()

#======================================================================================================================================================================#
print(f"{'Dictionary Functions:':^200}")
print()
def vowscons(str):                            # Rewriting this function, using a dictionary to hold both counters

    counts = {                                # Initalises the dictionary counts with 2 key value pairs 
        "vowels": 0,
        "consonants": 0
    }

    for i in str:                             # Iterate through each character in stringh
        if i.isalpha():                       # If the character is a letter
            if i.lower() in "aeiou":
                counts["vowels"] += 1         # Adding to the dictionaries' vowels keys value
            else:
                counts["consonants"] += 1     # Adding to the dictionaries' consonants keys value
    return counts
print(vowscons("Hello how are you?"))
print()

def MostOcc(str):
    
    Character_count = {}

    for char in str:                          # For each character in the inputted string
        if char.isalpha():                    # If character is a LETTER
            char = char.lower()               # Convert to lowercase
            if char not in Character_count:   # If it is not yet in the dictionary
                Character_count[char] = 1     # Initialise it with the value 1
            else:           
                Character_count[char] += 1    # If it has been seen, add 1 
    
    max_count = max(Character_count.values()) # Returns the highest Value

    most_common_characters = []               

    for key, value in Character_count.items(): # Iterate through each tuples(Character_count.items()), key and value
        if value == int(max_count):            # If it is joint with the highest value
            most_common_characters.append(key) # Add it to the list
    return most_common_characters
print(MostOcc("Hello I am called James"))

#=======================================================================================================================================================================#
print()
print(f"{'WORD FREQUENCY COUNTER:':^200}")

sentence = "banana apple orange banana banana apple"

# 1. Manual Frequency Counter using a Plain Dictionary

def word_counter(str):

    word_counter = {}
    for word in str.split():
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter
print(word_counter(sentence))

# 2. Automatic Frequency Counter Using Library Functions

from collections import Counter                                 # Import Counter from the collections module
"""                                                            
Counter automatically counts how many times each item appears in an iterable.
"""
def word_counter_auto(s):                                      
    return Counter(s.split())                                   # Returns a Counter object which behaves like a Dictionary
print(word_counter_auto(sentence))


print()
#=======================================================================================================================================================================#
print(f"{'Solving Key Leetcode Challenges using Dictionaries:':^200}")

print(f"{'TwoSum:'}\n")
from collections import defaultdict
def two_sum(lst, target):

    index = -1
    numbers = {}
    for n in lst:
        index +=1 
        if (target-n) in numbers:
            index_b = numbers[target-n]
            return index_b, index
        else:
            numbers[n] = index
    return None
print(two_sum([2, 7, 11, 15], 9))

print(f"\n{'IsAnagram Function using Counter:'}\n")

def is_anagram(s1, s2):

    if Counter(s1.lower()) == Counter(s2.lower()):
        return True
    return False

print(is_anagram("Secure","Rescue"))

print(f"\n{'First Unique Character Function:'}\n")

def first_unique_character(s3):

    chars = Counter(s3.lower())

    for key in chars:
        if chars[key] == 1:
            index = s3.find(key)
            return(f"The first unique character is {key}, and it is found at index number: {index}")
    return None
print(first_unique_character("loveleetcode"))
    

